# Database Schema

### Table: iisk_form_542
Columns:
- id (bigint) | NOT NULL
- row_num (bigint) | NULL
- type_budjet (text) | NULL
- kato (text) | NULL
- repdate (date) | NULL
- god (bigint) | NULL
- mes (bigint) | NULL
- gu (text) | NULL
- func (text) | NULL
- espk (text) | NULL
- sumrg (numeric) | NULL
- curr_sumrg (numeric) | NULL
- delta_sumrg (numeric) | NULL
- client_code (text) | NULL

---
### Table: iisk_form_552
Columns:
- id (bigint) | NOT NULL
- row_num (bigint) | NULL
- type_budjet (text) | NULL
- kato (text) | NULL
- repdate (date) | NULL
- god (bigint) | NULL
- mes (bigint) | NULL
- gu (text) | NULL
- func (text) | NULL
- espk (text) | NULL
- sumrg (numeric) | NULL
- curr_sumrg (numeric) | NULL
- delta_sumrg (numeric) | NULL
- client_code (text) | NULL

---
### Table: iisk_gu_list
Columns:
- id (bigint) | NOT NULL
- source_id (bigint) | NULL
- code (text) | NULL
- summary_flag (text) | NULL
- name_rus (text) | NULL
- name_kz (text) | NULL
- gu_bin (text) | NULL
- gu_rnn (text) | NULL
- id_region (text) | NULL
- id_budget_type (text) | NULL
- address (text) | NULL
- date_start (date) | NULL
- date_end (date) | NULL
- kato (text) | NULL
- budget_type (text) | NULL
- rucov (text) | NULL
- buhgal (text) | NULL
- last_update_date (date) | NULL

---
### Table: iisk_form_534
Columns:
- id (bigint) | NOT NULL
- row_num (bigint) | NULL
- type_bud (text) | NULL
- kato (text) | NULL
- iik (text) | NULL
- ddate (date) | NULL
- fin (text) | NULL
- acc_sld_beg (numeric) | NULL
- acc_ob_dt (numeric) | NULL
- acc_ob_ct (numeric) | NULL
- sld_day (numeric) | NULL
- acc_sld_end (numeric) | NULL
- description (text) | NULL
- client_code (text) | NULL

---
### Table: databasechangelog
Columns:
- id (character varying) | NOT NULL
- id (character varying) | NOT NULL
- author (character varying) | NOT NULL
- author (character varying) | NOT NULL
- filename (character varying) | NOT NULL
- filename (character varying) | NOT NULL
- dateexecuted (timestamp without time zone) | NOT NULL
- dateexecuted (timestamp without time zone) | NOT NULL
- orderexecuted (integer) | NOT NULL
- orderexecuted (integer) | NOT NULL
- exectype (character varying) | NOT NULL
- exectype (character varying) | NOT NULL
- md5sum (character varying) | NULL
- md5sum (character varying) | NULL
- description (character varying) | NULL
- description (character varying) | NULL
- comments (character varying) | NULL
- comments (character varying) | NULL
- tag (character varying) | NULL
- tag (character varying) | NULL
- liquibase (character varying) | NULL
- liquibase (character varying) | NULL
- contexts (character varying) | NULL
- contexts (character varying) | NULL
- labels (character varying) | NULL
- labels (character varying) | NULL
- deployment_id (character varying) | NULL
- deployment_id (character varying) | NULL

---
### Table: databasechangeloglock
Columns:
- id (integer) | NOT NULL
- id (integer) | NOT NULL
- locked (boolean) | NOT NULL
- locked (boolean) | NOT NULL
- lockgranted (timestamp without time zone) | NULL
- lockgranted (timestamp without time zone) | NULL
- lockedby (character varying) | NULL
- lockedby (character varying) | NULL

---
### Table: file
Columns:
- id (bigint) | NOT NULL
- path (text) | NOT NULL
- in_out (boolean) | NOT NULL
- integration (text) | NOT NULL
- data_type (text) | NOT NULL
- message_id (text) | NULL
- request (bigint) | NULL
- storage_volume (text) | NULL
- load_time (timestamp with time zone) | NOT NULL
- region (text) | NULL

---
### Table: file_prop
Columns:
- id (bigint) | NOT NULL
- file (bigint) | NOT NULL
- prop (text) | NOT NULL
- value_text (text) | NULL
- value_bigint (bigint) | NULL
- value_double (double precision) | NULL
- value_datetime (timestamp with time zone) | NULL

---
### Table: iisk_form_219
Columns:
- id (bigint) | NOT NULL
- row_num (bigint) | NULL
- type_budjet (text) | NULL
- kato (text) | NULL
- dspk (text) | NULL
- gu (text) | NULL
- god (bigint) | NULL
- mes (bigint) | NULL
- repdate (date) | NULL
- sumrg (numeric) | NULL
- delta_sumrg (numeric) | NULL
- client_code (text) | NULL

---
### Table: iisk_form_243
Columns:
- id (bigint) | NOT NULL
- row_num (bigint) | NULL
- code_tpk (text) | NULL
- valuedate (date) | NULL
- specific (text) | NULL
- description (text) | NULL
- senderbin (text) | NULL
- senderbik (text) | NULL
- senderiik (text) | NULL
- amount (numeric) | NULL
- ppo (numeric) | NULL
- paymentdate (date) | NULL
- paymentnumber (text) | NULL
- sendername (text) | NULL
- client_code (text) | NULL

---
### Table: iisk_form_409
Columns:
- id (bigint) | NOT NULL
- po_header_id (bigint) | NULL
- dt_reg (date) | NULL
- nom_za (text) | NULL
- nom_dog (text) | NULL
- dt_dog (text) | NULL
- rnn_supplier (text) | NULL
- supplier (text) | NULL
- nom_uved (text) | NULL
- item_description (text) | NULL
- summa_dog (numeric) | NULL
- invnum (text) | NULL
- pay_date (date) | NULL
- pay_amount (numeric) | NULL
- type_budjet (text) | NULL
- kod_tpk (text) | NULL
- gu (text) | NULL
- func (text) | NULL
- espk (text) | NULL
- client_code (text) | NULL

---
### Table: table1
Columns:
- id (bigint) | NULL
- code (text) | NULL
- data (text) | NULL

---
### Table: iisk_form_420
Columns:
- id (bigint) | NOT NULL
- row_num (bigint) | NULL
- type_budjet (text) | NULL
- kato (text) | NULL
- func (text) | NULL
- espk (text) | NULL
- gu (text) | NULL
- god (bigint) | NULL
- mes (bigint) | NULL
- repdate (date) | NULL
- plg (numeric) | NULL
- plat (numeric) | NULL
- obaz (numeric) | NULL
- sumrg (numeric) | NULL
- curr_sumrg (numeric) | NULL
- registrob (numeric) | NULL
- notexec (numeric) | NULL
- delta_sumrg (numeric) | NULL
- client_code (text) | NULL

---
### Table: iisk_form_211
Columns:
- id (bigint) | NOT NULL
- row_num (bigint) | NULL
- type_budjet (text) | NULL
- kato (text) | NULL
- dspk (text) | NULL
- gu (text) | NULL
- god (bigint) | NULL
- mes (bigint) | NULL
- repdate (date) | NULL
- sumrg (numeric) | NULL
- delta_sumrg (numeric) | NULL
- client_code (text) | NULL

---
### Table: iisk_forced_data_loading
Columns:
- id (bigint) | NOT NULL
- client_code (text) | NOT NULL
- form_code (text) | NOT NULL
- report_date (date) | NOT NULL

---
