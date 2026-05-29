"""Движок распознавания речи (3iTech bilingual RU+KK Wav2Vec2-CTC).

Общая логика для CLI (transcribe.py) и веб-приложения (app.py).
Длинное аудио нарезается на чанки с перекрытием, чтобы не упираться в память.
"""
from __future__ import annotations

import io
import os
import re
import tempfile
from pathlib import Path

import librosa
import numpy as np
import torch

HERE = Path(__file__).resolve().parent
MODEL_PATH = HERE / "model" / "model.pt"
TOKENS_PATH = HERE / "model" / "tokens.lst"

SR = 16000
# Нарезка длинных файлов: окно 25с с перекрытием 2с (Wav2Vec2 хорошо держит ~30с)
CHUNK_S = 25.0
OVERLAP_S = 2.0


class ASREngine:
    def __init__(self, model_path=MODEL_PATH, tokens_path=TOKENS_PATH, device="cpu"):
        self.device = device
        self.model = torch.jit.load(str(model_path), map_location=device).eval()
        self.id2tok, self.blank = self._load_tokens(tokens_path)

    @staticmethod
    def _load_tokens(path):
        id2tok = {}
        with open(path) as f:
            for line in f:
                line = line.rstrip("\n")
                if not line:
                    continue
                tok, idx = line.split("\t")
                id2tok[int(idx)] = tok
        blank = max(id2tok.keys()) + 1  # CTC blank сразу после последнего токена
        id2tok[blank] = "<blank>"
        return id2tok, blank

    def _greedy_decode(self, logits: torch.Tensor) -> str:
        ids = logits.argmax(-1).tolist()
        out, prev = [], -1
        for i in ids:
            if i == prev or i == self.blank:
                prev = i
                continue
            tok = self.id2tok.get(i, "")
            if tok in ("|", "_"):
                out.append(" ")
            elif tok == "[UNK]":
                pass
            else:
                out.append(tok)
            prev = i
        return re.sub(r"\s+", " ", "".join(out)).strip()

    def _infer_chunk(self, audio: np.ndarray) -> str:
        x = torch.from_numpy(audio).unsqueeze(0).to(self.device)
        with torch.no_grad():
            (logits,) = self.model(x)
        return self._greedy_decode(logits[0])

    def load_audio(self, path: str | Path) -> np.ndarray:
        """Декодирует mp3/wav/m4a/flac/... в 16 kHz mono FP32."""
        audio, _ = librosa.load(str(path), sr=SR, mono=True)
        return audio.astype(np.float32)

    def load_audio_bytes(self, data: bytes) -> np.ndarray:
        """Декодирует аудио из сырых байтов (загруженный blob) в 16 kHz mono FP32.

        Сначала пробуем быстрый путь в памяти (soundfile: wav/flac/ogg). Браузерный
        MediaRecorder отдаёт webm/opus, который soundfile не понимает — тогда падаем
        на ffmpeg через временный файл (через него librosa умеет webm/m4a/mp3/...).
        """
        try:
            audio, _ = librosa.load(io.BytesIO(data), sr=SR, mono=True)
            return audio.astype(np.float32)
        except Exception:
            with tempfile.NamedTemporaryFile(suffix=".bin", delete=False) as tmp:
                tmp.write(data)
                tmp_path = tmp.name
            try:
                audio, _ = librosa.load(tmp_path, sr=SR, mono=True)
                return audio.astype(np.float32)
            finally:
                try:
                    os.remove(tmp_path)
                except OSError:
                    pass

    def transcribe_bytes(self, data: bytes) -> str:
        """Транскрибирует аудио из сырых байтов (webm/ogg/wav/mp3/...)."""
        return self.transcribe_array(self.load_audio_bytes(data))

    def transcribe_array(self, audio: np.ndarray, progress=None) -> str:
        """Транскрибирует numpy-массив (16k mono). progress(frac, msg) — опц. колбэк."""
        dur = len(audio) / SR
        if dur <= CHUNK_S:
            return self._infer_chunk(audio)

        # длинное аудио — нарезаем с перекрытием и склеиваем
        chunk = int(CHUNK_S * SR)
        overlap = int(OVERLAP_S * SR)
        step = chunk - overlap
        starts = list(range(0, len(audio), step))
        parts = []
        for k, s in enumerate(starts):
            seg = audio[s : s + chunk]
            if len(seg) < int(0.3 * SR):
                continue
            parts.append(self._infer_chunk(seg))
            if progress:
                progress((k + 1) / len(starts), f"чанк {k + 1}/{len(starts)}")
        return self._merge(parts)

    @staticmethod
    def _merge(parts: list[str]) -> str:
        """Грубое склеивание чанков с удалением дубля на стыке перекрытия."""
        text = ""
        for p in parts:
            if not text:
                text = p
                continue
            pw = p.split()
            tw = text.split()
            # ищем максимальное перекрытие хвоста text и головы p (до 6 слов)
            best = 0
            for k in range(min(6, len(pw), len(tw)), 0, -1):
                if tw[-k:] == pw[:k]:
                    best = k
                    break
            text = " ".join(tw + pw[best:])
        return text.strip()

    def transcribe_file(self, path: str | Path, progress=None) -> str:
        audio = self.load_audio(path)
        return self.transcribe_array(audio, progress=progress)


_engine: ASREngine | None = None


def get_engine() -> ASREngine:
    """Ленивая singleton-загрузка (модель грузится один раз)."""
    global _engine
    if _engine is None:
        _engine = ASREngine()
    return _engine
