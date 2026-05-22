# Database Schema

### Table: dict_st_rep_form_col
Columns:
- id (bigint) | NOT NULL
- col_group (bigint) | NOT NULL
- order_number (integer) | NOT NULL
- name_kk (text) | NOT NULL
- name_ru (text) | NOT NULL
- unit_name_kk (text) | NULL
- unit_name_ru (text) | NULL
- aggregation (character varying) | NULL
- width (integer) | NOT NULL
- data_source (character varying) | NOT NULL
- col_type (character varying) | NULL
- subprog_dist_editable (boolean) | NOT NULL
- detailed_report_only (boolean) | NOT NULL
- remove_if_no_data (boolean) | NOT NULL
- fractional_digit_count (integer) | NULL
- for_total (boolean) | NOT NULL
- debug (boolean) | NOT NULL
- report_types (ARRAY) | NOT NULL

---
### Table: budget_request_form_01_361
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- type (character varying) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- summa (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_execution_application12_14
Columns:
- id (bigint) | NOT NULL
- region (character varying) | NULL
- func (character varying) | NULL
- expence_code (character varying) | NULL
- year (integer) | NULL
- month (integer) | NULL
- refined_plan (numeric) | NULL
- adjusted_plan (numeric) | NULL
- allocated_budget (numeric) | NULL
- finance_plan (numeric) | NULL
- expected_plan (numeric) | NULL
- user_id (character varying) | NULL
- update_date (timestamp without time zone) | NULL
- form_id (bigint) | NOT NULL

---
### Table: dict_mb_bc
Columns:
- id (integer) | NOT NULL
- code (character varying) | NULL
- name_kk (text) | NULL
- name_ru (text) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: mb_bc
Columns:
- id (integer) | NOT NULL
- code (character varying) | NULL
- year (integer) | NULL
- cur_year (integer) | NULL
- id_budget_version (character varying) | NULL
- credit_amount (double precision) | NULL
- debt (double precision) | NULL
- credit_receipt (double precision) | NULL
- repayment (double precision) | NULL
- reward_credited (double precision) | NULL
- reward_paid (double precision) | NULL

---
### Table: admin_mode_order_user
Columns:
- id (bigint) | NOT NULL
- admin_mode_order_id (bigint) | NOT NULL
- is_aggregate (boolean) | NOT NULL
- iin_c (bytea) | NULL
- firstname_c (bytea) | NULL
- lastname_c (bytea) | NULL
- patronymic_c (bytea) | NULL
- phone_c (bytea) | NULL
- email_c (bytea) | NULL
- iin_hash (bytea) | NULL

---
### Table: budget_execution_ipf_obligations
Columns:
- id (integer) | NOT NULL
- region (character varying) | NOT NULL
- year (integer) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- user_id (character varying) | NOT NULL
- date_creation (timestamp with time zone) | NOT NULL
- spf (integer) | NOT NULL
- bip_code (character varying) | NULL
- month (integer) | NOT NULL
- amount (numeric) | NOT NULL
- form (bigint) | NULL
- expense_code (character varying) | NULL

---
### Table: summary_report_files
Columns:
- id (bigint) | NOT NULL
- queues_info_id (bigint) | NOT NULL
- file_name (character varying) | NOT NULL

---
### Table: budget_request_form_01_139
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- summa (double precision) | NULL
- term (integer) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_paid_418_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- unit (character varying) | NOT NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_331_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- code (character varying) | NOT NULL
- category_id (character varying) | NOT NULL
- recipient_ru (character varying) | NULL
- recipient_kk (character varying) | NULL
- purpose_ru (character varying) | NULL
- purpose_kk (character varying) | NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_421_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- summa (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_421_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- summa (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_421_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_419_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- unit (character varying) | NOT NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: project_bank_locations
Columns:
- id (bigint) | NOT NULL
- project_id (bigint) | NOT NULL
- location (character varying) | NULL
- created_at (timestamp without time zone) | NULL

---
### Table: budget_execution_application12_14_reasons
Columns:
- id (bigint) | NOT NULL
- region (character varying) | NULL
- year (integer) | NULL
- month (integer) | NULL
- func (character varying) | NULL
- expence_code (character varying) | NULL
- reason_id (integer) | NULL
- reason_sum (numeric) | NULL
- reason_type (integer) | NULL
- form_id (bigint) | NOT NULL

---
### Table: budget_request_form_gkkp_331_v2_decode
Columns:
- id (integer) | NOT NULL
- category_id (character varying) | NOT NULL
- expense_code (character varying) | NOT NULL
- summa (numeric) | NOT NULL
- recipient_ru (character varying) | NULL
- recipient_kk (character varying) | NULL
- purpose_ru (character varying) | NULL
- purpose_kk (character varying) | NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_hash (character varying) | NULL

---
### Table: budget_request_form_gkkp_421_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_423_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- summa (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_423_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- summa (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_423_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_422_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: dict_budget_regions
Columns:
- id (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- source_id (integer) | NULL
- code (character varying) | NULL
- kazn_dep_name (character varying) | NULL
- kazn_dep_address (character varying) | NULL
- kazn_dep_rnn (character varying) | NULL
- kazn_dep_bin (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL
- obl (character varying) | NULL
- obl_ru (character varying) | NULL
- obl_kk (character varying) | NULL
- budget_level (integer) | NULL

---
### Table: budget_request_form_01_149_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_01_361
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- type (character varying) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- summa (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_paid_418_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_331_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- code (character varying) | NOT NULL
- category_id (character varying) | NOT NULL
- recipient_ru (character varying) | NULL
- recipient_kk (character varying) | NULL
- purpose_ru (character varying) | NULL
- purpose_kk (character varying) | NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_312
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- article_subsidy (character varying) | NOT NULL
- summa (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_331_v2_decode
Columns:
- id (integer) | NOT NULL
- category_id (character varying) | NOT NULL
- expense_code (character varying) | NOT NULL
- summa (numeric) | NOT NULL
- recipient_ru (character varying) | NULL
- recipient_kk (character varying) | NULL
- purpose_ru (character varying) | NULL
- purpose_kk (character varying) | NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_hash (character varying) | NULL

---
### Table: budget_request_form_gkkp_312
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- article_subsidy (character varying) | NOT NULL
- summa (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: project_bank_concepts
Columns:
- id (bigint) | NOT NULL
- project_id (bigint) | NOT NULL
- concept (character varying) | NULL
- created_at (timestamp without time zone) | NULL

---
### Table: budget_request_form_312_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_422_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_429_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- summa (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_01_361_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: reports_constructor_access_level
Columns:
- report_name (character varying) | NOT NULL
- name_ru (text) | NULL
- is_income (boolean) | NULL
- is_expense (boolean) | NULL
- is_uo (boolean) | NULL
- is_abp (boolean) | NULL
- is_gu (boolean) | NULL
- name_kk (character varying) | NOT NULL
- name_en (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_312_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_212_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- summa (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: bip_files_type
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: alteration_journal
Columns:
- id (bigint) | NOT NULL
- creation_timestamp (timestamp without time zone) | NOT NULL
- source_tab (character varying) | NOT NULL
- region (text) | NOT NULL
- abp (character varying) | NULL
- gu (character varying) | NULL
- number (smallint) | NULL
- request_type (character varying) | NULL
- certificate_date (date) | NOT NULL
- certificate_status (text) | NOT NULL
- name (text) | NOT NULL
- user_id (character varying) | NOT NULL
- progress (smallint) | NOT NULL
- parameters (jsonb) | NOT NULL
- file (bytea) | NULL
- report_key (text) | NOT NULL
- filename (text) | NOT NULL
- gu261 (character varying) | NULL

---
### Table: budget_request_form_gkkp_01_361_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: dict_srs_status
Columns:
- id (integer) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NOT NULL
- name_en (character varying) | NOT NULL
- sort_order (integer) | NOT NULL
- status_code (integer) | NOT NULL
- ate_code (ARRAY) | NOT NULL
- status_code_ckr (character varying) | NULL

---
### Table: budget_request_form_02_149_v2_decode
Columns:
- id (integer) | NOT NULL
- category_id (character varying) | NOT NULL
- enstru_code (character varying) | NOT NULL
- add_detail (character varying) | NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_hash (character varying) | NULL

---
### Table: budget_request_form_gkkp_02_149_v2_decode
Columns:
- id (integer) | NOT NULL
- category_id (character varying) | NOT NULL
- enstru_code (character varying) | NOT NULL
- add_detail (character varying) | NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_hash (character varying) | NULL

---
### Table: budget_request_form_514_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- branch (character varying) | NOT NULL
- type_credit (character varying) | NOT NULL
- category_id (character varying) | NOT NULL
- period_ru (character varying) | NULL
- period_kk (character varying) | NULL
- recipient_ru (character varying) | NULL
- recipient_kk (character varying) | NULL
- purpose_ru (character varying) | NULL
- purpose_kk (character varying) | NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_514_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- branch (character varying) | NOT NULL
- type_credit (character varying) | NOT NULL
- category_id (character varying) | NOT NULL
- period_ru (character varying) | NULL
- period_kk (character varying) | NULL
- recipient_ru (character varying) | NULL
- recipient_kk (character varying) | NULL
- purpose_ru (character varying) | NULL
- purpose_kk (character varying) | NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_514_v2_decode
Columns:
- id (integer) | NOT NULL
- category_id (character varying) | NOT NULL
- bc_goal (character varying) | NOT NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_hash (character varying) | NULL

---
### Table: budget_request_form_gkkp_514_v2_decode
Columns:
- id (integer) | NOT NULL
- category_id (character varying) | NOT NULL
- bc_goal (character varying) | NOT NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_hash (character varying) | NULL

---
### Table: budget_request_form_513_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- branch (character varying) | NOT NULL
- type_credit (character varying) | NOT NULL
- category_id (character varying) | NOT NULL
- period_ru (character varying) | NULL
- period_kk (character varying) | NULL
- recipient_ru (character varying) | NULL
- recipient_kk (character varying) | NULL
- purpose_ru (character varying) | NULL
- purpose_kk (character varying) | NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_513_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- branch (character varying) | NOT NULL
- type_credit (character varying) | NOT NULL
- category_id (character varying) | NOT NULL
- period_ru (character varying) | NULL
- period_kk (character varying) | NULL
- recipient_ru (character varying) | NULL
- recipient_kk (character varying) | NULL
- purpose_ru (character varying) | NULL
- purpose_kk (character varying) | NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_513_v2_decode
Columns:
- id (integer) | NOT NULL
- category_id (character varying) | NOT NULL
- bc_goal (character varying) | NOT NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_hash (character varying) | NULL

---
### Table: budget_request_form_gkkp_513_v2_decode
Columns:
- id (integer) | NOT NULL
- category_id (character varying) | NOT NULL
- bc_goal (character varying) | NOT NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_hash (character varying) | NULL

---
### Table: srs_indicator_to_ate_data
Columns:
- id (integer) | NOT NULL
- indicator_code (character varying) | NOT NULL
- ate_code (character varying) | NOT NULL

---
### Table: dict_article_subsidy
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- parent_code (character varying) | NULL
- order_num (integer) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL
- comment (character varying) | NULL

---
### Table: budget_consolidate_calc_expens_income
Columns:
- id (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- income_cat (character varying) | NOT NULL
- kass_sum (double precision) | NULL
- fact_sum (double precision) | NULL
- utoch_plan (double precision) | NULL
- plan_val0 (double precision) | NULL
- plan_val1 (double precision) | NULL
- plan_val2 (double precision) | NULL
- region (character varying) | NULL
- user_id (character varying) | NULL
- update_date (timestamp without time zone) | NULL
- variant (character varying) | NOT NULL

---
### Table: dict_gu_income
Columns:
- id (bigint) | NOT NULL
- code (text) | NOT NULL
- name_ru (text) | NOT NULL
- name_kk (text) | NOT NULL
- beg_date (date) | NOT NULL
- end_date (date) | NOT NULL

---
### Table: budget_request_form_168
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_313_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_313
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- summa (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_313
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- summa (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_313_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_168
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_execution_isgp_response
Columns:
- id (bigint) | NOT NULL
- message_id (character varying) | NOT NULL
- message_date (timestamp without time zone) | NOT NULL
- status_code (character varying) | NOT NULL
- status_message (character varying) | NULL
- budget_execution_alteration_request_id (bigint) | NOT NULL

---
### Table: budget_request_form_612_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- summa (numeric) | NOT NULL
- period_ru (character varying) | NULL
- period_kk (character varying) | NULL
- recipient_ru (character varying) | NULL
- recipient_kk (character varying) | NULL
- purpose_ru (character varying) | NULL
- purpose_kk (character varying) | NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_168_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_168_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: srs_form_status
Columns:
- id (integer) | NOT NULL
- year (integer) | NOT NULL
- code_kato3 (character varying) | NOT NULL
- direction_code (character varying) | NOT NULL
- status (integer) | NOT NULL
- comment (text) | NULL
- user_id (character varying) | NULL
- created_at (timestamp without time zone) | NOT NULL
- updated_at (timestamp without time zone) | NOT NULL

---
### Table: srs_form_status_history
Columns:
- id (integer) | NOT NULL
- kato_direction_id (integer) | NOT NULL
- status (integer) | NOT NULL
- comment (text) | NULL
- user_id (character varying) | NOT NULL
- created_at (timestamp without time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_612_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- summa (numeric) | NOT NULL
- period_ru (character varying) | NULL
- period_kk (character varying) | NULL
- recipient_ru (character varying) | NULL
- recipient_kk (character varying) | NULL
- purpose_ru (character varying) | NULL
- purpose_kk (character varying) | NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_612_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: dict_st_rep_form_col_group
Columns:
- id (bigint) | NOT NULL
- parent (bigint) | NULL
- form (character varying) | NOT NULL
- name_kk (text) | NOT NULL
- name_ru (text) | NOT NULL
- order_number (integer) | NOT NULL
- hiddable_cell (boolean) | NULL
- report_types (ARRAY) | NOT NULL

---
### Table: budget_request_form_gkkp_612_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_fact302
Columns:
- id (integer) | NOT NULL
- region (character varying) | NOT NULL
- year (integer) | NOT NULL
- date (date) | NOT NULL
- func (character varying) | NULL
- month (integer) | NOT NULL
- amount (numeric) | NULL
- plan_type (integer) | NULL
- user_id (character varying) | NOT NULL
- update_date (timestamp without time zone) | NOT NULL

---
### Table: budget_fact304
Columns:
- id (integer) | NOT NULL
- region (character varying) | NOT NULL
- year (integer) | NOT NULL
- date (date) | NOT NULL
- abp (integer) | NULL
- gu (character varying) | NULL
- prg (integer) | NULL
- ppr (integer) | NULL
- spf (integer) | NULL
- month (integer) | NOT NULL
- amount (numeric) | NULL
- plan_type (integer) | NOT NULL
- user_id (character varying) | NOT NULL
- update_date (timestamp without time zone) | NOT NULL

---
### Table: budget_request_form_157_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- summa (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_157_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- summa (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_157_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_157_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: dict_account_breakdown
Columns:
- id (integer) | NOT NULL
- operation_code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NOT NULL
- name_en (character varying) | NOT NULL
- beg_date (date) | NOT NULL
- end_date (date) | NULL
- created_at (timestamp without time zone) | NOT NULL
- updated_at (timestamp without time zone) | NOT NULL

---
### Table: budget_execution_alteration_gu_fact_region
Columns:
- id (bigint) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- region (character varying) | NOT NULL
- fact_region (character varying) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: budget_execution_alteration_request
Columns:
- id (bigint) | NOT NULL
- number (bigint) | NOT NULL
- gu (character varying) | NULL
- date (timestamp without time zone) | NOT NULL
- request_type (character varying) | NULL
- budget_version (character varying) | NULL
- user_id (character varying) | NOT NULL
- create_date (timestamp without time zone) | NULL
- update_date (timestamp without time zone) | NULL
- delete_date (timestamp without time zone) | NULL
- region (character varying) | NOT NULL
- description (character varying) | NULL
- budget_execution_alteration_abp_request_id (bigint) | NULL
- abp (integer) | NULL
- level (character varying) | NULL
- fact_region (character varying) | NULL

---
### Table: um_audit_event
Columns:
- id (bigint) | NOT NULL
- created_at (timestamp with time zone) | NULL
- service_name (text) | NULL
- tab (text) | NULL
- action_type (text) | NULL
- admin_user_id (text) | NULL
- target_user_id (text) | NULL

---
### Table: um_audit_event_change
Columns:
- id (bigint) | NOT NULL
- event_id (bigint) | NOT NULL
- field_name (text) | NULL
- old_value (text) | NULL
- new_value (text) | NULL

---
### Table: dict_local_budget_cashflow
Columns:
- id (integer) | NOT NULL
- operation_code (character varying) | NOT NULL
- row_code (ARRAY) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NOT NULL
- name_en (character varying) | NOT NULL
- beg_date (date) | NOT NULL
- end_date (date) | NULL
- created_at (timestamp without time zone) | NOT NULL
- updated_at (timestamp without time zone) | NOT NULL

---
### Table: power_external_frames
Columns:
- id (integer) | NOT NULL
- code (character varying) | NULL
- name_en (character varying) | NULL
- name_kz (character varying) | NULL
- name_ru (character varying) | NULL
- description (character varying) | NULL
- src (character varying) | NULL
- region_instance_code (character varying) | NULL
- module_code (character varying) | NULL
- user_id (character varying) | NULL
- update_time (timestamp without time zone) | NULL

---
### Table: project_bank_goals
Columns:
- id (bigint) | NOT NULL
- project_id (bigint) | NOT NULL
- name_kz (text) | NOT NULL
- name_ru (text) | NOT NULL
- created_at (timestamp without time zone) | NULL

---
### Table: dict_budget_balance_rows
Columns:
- id (integer) | NOT NULL
- row_code2025 (character varying) | NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NOT NULL
- name_en (character varying) | NOT NULL
- beg_date (date) | NOT NULL
- end_date (date) | NULL
- created_at (timestamp without time zone) | NOT NULL
- updated_at (timestamp without time zone) | NOT NULL
- row_code2026 (character varying) | NULL

---
### Table: dict_funding_level
Columns:
- id (bigint) | NOT NULL
- abp (integer) | NULL
- prg (integer) | NULL
- ppr (integer) | NULL
- func (character varying) | NULL
- form (character varying) | NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- name_en (character varying) | NULL
- type (character varying) | NULL
- fin_src_detail_code (character varying) | NULL

---
### Table: budget_execution_application9
Columns:
- id (integer) | NOT NULL
- func (character varying) | NOT NULL
- region (character varying) | NOT NULL
- date (date) | NOT NULL
- expectation (numeric) | NULL
- update_date (timestamp without time zone) | NULL
- status (boolean) | NULL
- user_id (text) | NULL
- ob_subventions (numeric) | NULL
- pl_subventions (numeric) | NULL

---
### Table: project_bank_form_data
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NOT NULL
- budget_region (character varying) | NULL
- name_kz (text) | NOT NULL
- name_ru (text) | NOT NULL
- abp (integer) | NOT NULL
- is_archive (boolean) | NOT NULL
- funding (character varying) | NULL
- project_type (character varying) | NOT NULL
- branch (character varying) | NULL
- prg (integer) | NULL
- begin_date (date) | NULL
- end_date (date) | NULL
- user_id (character varying) | NOT NULL
- created_at (timestamp without time zone) | NULL
- updated_at (timestamp without time zone) | NULL
- is_deleted (boolean) | NULL
- period_start_year (integer) | NULL
- period_end_year (integer) | NULL
- amount_budget (numeric) | NULL
- date_act_commission (date) | NULL
- funding_mixed (jsonb) | NULL

---
### Table: budget_forecast_reporting_form
Columns:
- id (integer) | NOT NULL
- code_form (character varying) | NOT NULL
- update_date (date) | NULL
- user_id (character varying) | NULL
- cur_year (integer) | NULL
- region_code (character varying) | NULL
- data_type (integer) | NULL
- budget_variant (character varying) | NULL
- abp_code (integer) | NULL
- comments_text (text) | NULL
- comments_date (date) | NULL
- comments_user_id (character varying) | NULL
- pkfo_type (character varying) | NULL

---
### Table: appendix_6_forms
Columns:
- id (integer) | NOT NULL
- table_id (character varying) | NOT NULL
- update_date (date) | NULL
- user_id (character varying) | NULL
- cur_year (integer) | NULL
- region_code (character varying) | NULL
- data_type (integer) | NULL
- budget_variant (character varying) | NULL
- comments_text (text) | NULL
- comments_date (date) | NULL
- comments_user_id (character varying) | NULL

---
### Table: dict_movement
Columns:
- id (integer) | NOT NULL
- table_number (character varying) | NULL
- dict_code (character varying) | NULL
- line_code (character varying) | NULL
- name_ru (text) | NULL
- name_kk (text) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: app6_movement
Columns:
- id (integer) | NOT NULL
- year (integer) | NULL
- cur_year (integer) | NULL
- fact_value (double precision) | NULL
- evaluation_value (double precision) | NULL
- forecast_value (double precision) | NULL
- id_budget_version (character varying) | NULL
- dict_code (character varying) | NULL

---
### Table: project_bank_tasks
Columns:
- id (bigint) | NOT NULL
- goal_id (bigint) | NOT NULL
- name_kz (text) | NOT NULL
- name_ru (text) | NOT NULL
- created_at (timestamp without time zone) | NULL

---
### Table: gchp_contracts
Columns:
- id (integer) | NOT NULL
- contract_type (character varying) | NULL
- region (character varying) | NULL
- abp (integer) | NULL
- object_name_ru (text) | NULL
- object_name_kk (text) | NULL
- contract_number (character varying) | NULL
- contract_date (date) | NULL
- registration_number (integer) | NULL
- registration_date (date) | NULL
- period_begin (date) | NULL
- period_end (date) | NULL
- year_beginning (integer) | NULL
- investment_costs (double precision) | NULL
- operating_costs (double precision) | NULL
- other_payments (double precision) | NULL
- transfer_date (date) | NULL
- view (boolean) | NULL
- end_date (date) | NULL

---
### Table: dict_srs_categories
Columns:
- id (integer) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NOT NULL
- name_en (character varying) | NOT NULL
- sort_order (integer) | NOT NULL
- category_code (integer) | NULL
- category_code_ckr (character varying) | NULL

---
### Table: pkfo_3mb
Columns:
- id (integer) | NOT NULL
- line_code (character varying) | NULL
- year (integer) | NULL
- cur_year (integer) | NULL
- fact_value (double precision) | NULL
- evaluation_value (double precision) | NULL
- forecast_value (double precision) | NULL
- id_budget_version (character varying) | NULL

---
### Table: pkfo_2mb
Columns:
- id (integer) | NOT NULL
- line_code (character varying) | NULL
- year (integer) | NULL
- cur_year (integer) | NULL
- fact_value (double precision) | NULL
- evaluation_value (double precision) | NULL
- forecast_value (double precision) | NULL
- id_budget_version (character varying) | NULL

---
### Table: gchp_data
Columns:
- id (integer) | NOT NULL
- contract_id (integer) | NULL
- year (integer) | NULL
- cur_year (integer) | NULL
- id_budget_version (character varying) | NULL
- remined (double precision) | NULL
- paid (double precision) | NULL
- cumulative_paid (double precision) | NULL
- cost_type (character varying) | NULL

---
### Table: dict_balance
Columns:
- id (integer) | NOT NULL
- name_kk (text) | NULL
- name_ru (text) | NULL
- code (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: app6_balance
Columns:
- id (integer) | NOT NULL
- year (integer) | NULL
- cur_year (integer) | NULL
- fact_value (double precision) | NULL
- evaluation_value (double precision) | NULL
- forecast_value (double precision) | NULL
- id_budget_version (character varying) | NULL
- balance_code (character varying) | NULL
- table_num (character varying) | NULL

---
### Table: pkfo_4mb
Columns:
- id (integer) | NOT NULL
- line_code (character varying) | NULL
- year (integer) | NULL
- cur_year (integer) | NULL
- fact_value (double precision) | NULL
- evaluation_value (double precision) | NULL
- forecast_value (double precision) | NULL
- id_budget_version (character varying) | NULL

---
### Table: mb_loans
Columns:
- id (integer) | NOT NULL
- code (character varying) | NULL
- year (integer) | NULL
- cur_year (integer) | NULL
- id_budget_version (character varying) | NULL
- debt (double precision) | NULL
- loan_receipt (double precision) | NULL
- repayment_from_reg (double precision) | NULL
- repayment_from_other (double precision) | NULL
- corrections (double precision) | NULL
- reward_credited (double precision) | NULL
- reward_tb_paid (double precision) | NULL

---
### Table: budget_request_form_418_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- unit (character varying) | NOT NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_418_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- unit (character varying) | NOT NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_418_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_418_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_execution_ipf_request_form
Columns:
- id (bigint) | NOT NULL
- form (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- name_ru (character varying) | NOT NULL
- amount (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region (character varying) | NOT NULL
- create_date (timestamp without time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_423_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_422_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- summa (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_422_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- summa (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_429_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- summa (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_429_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_429_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_212_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- summa (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_212_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_212_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_213_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- summa (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_213_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- summa (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_213_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_213_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_711_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- summa (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_711_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- summa (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_711_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_711_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_712_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- summa (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_712_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- summa (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_712_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_712_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: srs_indicator_rels
Columns:
- id (integer) | NOT NULL
- par_indicator_code (character varying) | NOT NULL
- child_indicator_code (character varying) | NOT NULL
- created_at (timestamp without time zone) | NOT NULL
- updated_at (timestamp without time zone) | NULL

---
### Table: budget_request_form_419_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- unit (character varying) | NOT NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_execution_alteration_request_file
Columns:
- id (bigint) | NOT NULL
- budget_execution_alteration_request_id (bigint) | NOT NULL
- user_id (character varying) | NOT NULL
- name (character varying) | NOT NULL
- file_link (character varying) | NOT NULL
- create_date (timestamp without time zone) | NULL

---
### Table: budget_execution_alteration_request_status
Columns:
- id (bigint) | NOT NULL
- budget_execution_alteration_request_id (bigint) | NOT NULL
- user_id (character varying) | NOT NULL
- comment (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- status (integer) | NOT NULL

---
### Table: stafftab_ead_d_01_29
Columns:
- id (bigint) | NOT NULL
- emp (bigint) | NOT NULL
- conf (bigint) | NOT NULL
- value_bool (boolean) | NULL
- value_text (text) | NULL
- value_number (double precision) | NULL
- value_salary_rate (double precision) | NULL
- value_norm_rate (double precision) | NULL
- value_date (date) | NULL
- value_military_rank (bigint) | NULL
- value_military_title (bigint) | NULL
- budget_program (integer) | NULL
- calc_hint (ARRAY) | NULL
- fact_hours (double precision) | NULL

---
### Table: budget_request_form_339
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- code (character varying) | NOT NULL
- category_id (character varying) | NOT NULL
- recipient_ru (character varying) | NULL
- recipient_kk (character varying) | NULL
- purpose_ru (character varying) | NULL
- purpose_kk (character varying) | NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_fact219
Columns:
- id (integer) | NOT NULL
- region_id (character varying) | NOT NULL
- month (integer) | NOT NULL
- year (integer) | NOT NULL
- code (character varying) | NOT NULL
- plan_reg (double precision) | NOT NULL
- plan_obl (double precision) | NOT NULL
- plan_msu (double precision) | NOT NULL
- update_date (timestamp without time zone) | NOT NULL
- variant (character varying) | NOT NULL
- kat (integer) | NULL
- cls (integer) | NULL
- pcl (integer) | NULL
- spf (integer) | NULL
- repdate (timestamp without time zone) | NULL
- gu (character varying) | NULL
- plan_reg_day (double precision) | NULL
- plan_obl_day (double precision) | NULL
- plan_msu_day (double precision) | NULL

---
### Table: budget_execution_ipf_request_form_dict
Columns:
- id (bigint) | NOT NULL
- table_name (character varying) | NOT NULL
- spf (integer) | NOT NULL
- create_date (timestamp without time zone) | NOT NULL
- col_name (character varying) | NULL

---
### Table: budget_execution_ipf_obligation
Columns:
- id (integer) | NOT NULL
- region (character varying) | NOT NULL
- year (integer) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- january (double precision) | NOT NULL
- february (double precision) | NOT NULL
- april (double precision) | NOT NULL
- march (double precision) | NOT NULL
- may (double precision) | NOT NULL
- june (double precision) | NOT NULL
- july (double precision) | NOT NULL
- august (double precision) | NOT NULL
- september (double precision) | NOT NULL
- october (double precision) | NOT NULL
- november (double precision) | NOT NULL
- december (double precision) | NOT NULL
- user_id (character varying) | NULL
- date_creation (timestamp without time zone) | NULL
- update_date (timestamp without time zone) | NULL
- bip_code (character varying) | NULL

---
### Table: budget_execution_ipf_payment
Columns:
- id (integer) | NOT NULL
- region (character varying) | NOT NULL
- year (integer) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- january (double precision) | NOT NULL
- february (double precision) | NOT NULL
- april (double precision) | NOT NULL
- march (double precision) | NOT NULL
- may (double precision) | NOT NULL
- june (double precision) | NOT NULL
- july (double precision) | NOT NULL
- august (double precision) | NOT NULL
- september (double precision) | NOT NULL
- october (double precision) | NOT NULL
- november (double precision) | NOT NULL
- december (double precision) | NOT NULL
- user_id (character varying) | NULL
- date_creation (timestamp without time zone) | NULL
- update_date (timestamp without time zone) | NULL
- bip_code (character varying) | NULL

---
### Table: budget_fact243
Columns:
- id (integer) | NOT NULL
- region_id (character varying) | NOT NULL
- month (integer) | NOT NULL
- year (integer) | NOT NULL
- code (character varying) | NOT NULL
- org (character varying) | NOT NULL
- sum (double precision) | NOT NULL
- update_date (timestamp without time zone) | NOT NULL
- variant (character varying) | NOT NULL
- kat (integer) | NULL
- cls (integer) | NULL
- pcl (integer) | NULL
- spf (integer) | NULL

---
### Table: stafftab_gu_setting_01_29
Columns:
- id (bigint) | NOT NULL
- key (character varying) | NOT NULL
- v_text (text) | NULL
- v_number (double precision) | NULL
- version (bigint) | NOT NULL

---
### Table: budget_request_form_156_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- summa (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_339
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- code (character varying) | NOT NULL
- category_id (character varying) | NOT NULL
- recipient_ru (character varying) | NULL
- recipient_kk (character varying) | NULL
- purpose_ru (character varying) | NULL
- purpose_kk (character varying) | NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_form_limits_comservices
Columns:
- id (bigint) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- comm_service (character varying) | NULL
- year (integer) | NOT NULL
- forecast_for_year (double precision) | NULL
- forecast_for_two_years (double precision) | NULL
- forecast_for_three_years (double precision) | NULL
- region (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_date (timestamp with time zone) | NULL

---
### Table: budget_request_form_gkkp_156_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- summa (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_156_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_156_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_income_data
Columns:
- id (integer) | NOT NULL
- region (character varying) | NOT NULL
- kat (integer) | NOT NULL
- cls (integer) | NOT NULL
- pcl (integer) | NOT NULL
- spf (integer) | NOT NULL
- amount (double precision) | NOT NULL
- note (character varying) | NULL
- year (integer) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- cur_year (integer) | NOT NULL
- update_date (timestamp without time zone) | NULL
- status (character varying) | NULL
- data_type (integer) | NULL

---
### Table: budget_gkkp_spf
Columns:
- id (bigint) | NOT NULL
- region (character varying) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- gkkp (character varying) | NOT NULL
- spf (integer) | NOT NULL
- form (character varying) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: budget_invest_project
Columns:
- id (integer) | NOT NULL
- region (character varying) | NULL
- year (integer) | NULL
- abp (integer) | NULL
- name_project (character varying) | NULL
- plan_god (double precision) | NULL
- plan_period (double precision) | NULL
- kas_rash (double precision) | NULL
- status (integer) | NULL

---
### Table: budget_project
Columns:
- id (integer) | NOT NULL
- code (integer) | NOT NULL
- obl (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_gu_department_01_29
Columns:
- id (bigint) | NOT NULL
- name_kk (text) | NOT NULL
- name_ru (text) | NOT NULL
- parent (bigint) | NULL
- serial_number (integer) | NULL
- version (bigint) | NOT NULL

---
### Table: budget_request_bp
Columns:
- id (bigint) | NOT NULL
- plan_year (integer) | NULL
- budget_regions (bigint) | NULL
- type_bp_level (bigint) | NULL
- type_bp_content (bigint) | NULL
- type_bp_impl (bigint) | NULL
- type_bp_state (bigint) | NULL
- goal_other (character varying) | NULL
- result_other (character varying) | NULL
- descr_ru (character varying) | NULL
- descr_kk (character varying) | NULL
- goal_other_ru (character varying) | NULL
- goal_other_kk (character varying) | NULL
- goal (bigint) | NULL
- final_result (bigint) | NULL
- abp (integer) | NULL
- prg (integer) | NULL
- ppr (integer) | NULL
- region (text) | NULL
- dri_by_region (boolean) | NULL
- dri_by_project (boolean) | NULL
- text_goal_fr (jsonb) | NULL
- concl_npa_ru (text) | NULL
- concl_bp_type_ru (text) | NULL
- concl_descr_ru (text) | NULL
- concl_goal_ru (text) | NULL
- concl_fr_ru (text) | NULL
- concl_expend_ru (text) | NULL
- concl_descr_infl_ru (text) | NULL
- concl_dri_ru (text) | NULL
- concl_common_ru (text) | NULL
- concl_see_ru (text) | NULL
- concl_pee_ru (text) | NULL
- concl_npa_code (text) | NULL
- concl_bp_type_code (text) | NULL
- concl_descr_code (text) | NULL
- concl_goal_code (text) | NULL
- concl_fr_code (text) | NULL
- concl_expend_code (text) | NULL
- concl_descr_infl_code (text) | NULL
- concl_dri_code (text) | NULL
- concl_common_code (text) | NULL
- concl_see_code (text) | NULL
- concl_pee_code (text) | NULL
- approve_status (text) | NULL
- variant (character varying) | NULL

---
### Table: budget_plan_variants
Columns:
- id (integer) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NOT NULL
- name_en (character varying) | NOT NULL

---
### Table: budget_execution_ipf_payments
Columns:
- id (integer) | NOT NULL
- region (character varying) | NOT NULL
- year (integer) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- user_id (character varying) | NOT NULL
- date_creation (timestamp with time zone) | NOT NULL
- spf (integer) | NOT NULL
- bip_code (character varying) | NULL
- month (integer) | NOT NULL
- amount (numeric) | NOT NULL
- form (bigint) | NULL
- expense_code (character varying) | NULL

---
### Table: queues_info
Columns:
- id (bigint) | NOT NULL
- type (integer) | NOT NULL
- key_name (character varying) | NOT NULL
- status (integer) | NOT NULL
- progress (integer) | NULL
- value (character varying) | NOT NULL
- uid (character varying) | NOT NULL
- create_date (timestamp without time zone) | NOT NULL
- finished_date (timestamp without time zone) | NULL
- sign_file_params_id (bigint) | NULL

---
### Table: budget_plan_fin
Columns:
- id (integer) | NOT NULL
- region_id (character varying) | NOT NULL
- month (integer) | NOT NULL
- code (character varying) | NOT NULL
- sum (double precision) | NOT NULL
- update_date (timestamp without time zone) | NOT NULL
- variant (character varying) | NOT NULL
- year (integer) | NULL
- vid (integer) | NULL
- abp (integer) | NULL
- prg (integer) | NULL
- ppr (integer) | NULL
- spf (integer) | NULL
- repdate (timestamp without time zone) | NULL

---
### Table: budget_request_bp_goal
Columns:
- id (bigint) | NOT NULL
- budget_request_bp (bigint) | NOT NULL
- goal (bigint) | NOT NULL

---
### Table: budget_request_bp_infl
Columns:
- id (bigint) | NOT NULL
- budget_request_bp (bigint) | NOT NULL
- year (integer) | NOT NULL
- descr_ru (character varying) | NULL
- descr_kk (character varying) | NULL

---
### Table: budget_local_post_limit
Columns:
- id (integer) | NOT NULL
- code_local (character varying) | NOT NULL
- code_post (character varying) | NOT NULL
- exception (character varying) | NULL
- limit (integer) | NOT NULL

---
### Table: budget_request_bp_fr
Columns:
- id (bigint) | NOT NULL
- budget_request_bp (bigint) | NOT NULL
- fr (bigint) | NOT NULL

---
### Table: budget_request_bp_driv
Columns:
- id (bigint) | NOT NULL
- owner (bigint) | NOT NULL
- unit (bigint) | NOT NULL
- reporting_year (double precision) | NULL
- corrected_plan (double precision) | NULL
- plan_period_1 (double precision) | NULL
- plan_period_2 (double precision) | NULL
- plan_period_3 (double precision) | NULL

---
### Table: gu_department_position_01_29
Columns:
- id (bigint) | NOT NULL
- name_kk (text) | NOT NULL
- name_ru (text) | NOT NULL
- func_block (character varying) | NULL
- pos_level (integer) | NULL
- legal_act_position (bigint) | NULL
- civil_position (bigint) | NULL
- work_position_rank (integer) | NULL
- mvd_position (bigint) | NULL
- legal_act_mvd_position (bigint) | NULL
- version (bigint) | NOT NULL
- edu_position (bigint) | NULL

---
### Table: budget_request_form_01_134
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- coefficient_salary (double precision) | NULL
- number_of_cases (integer) | NOT NULL
- number_of_jurors (integer) | NOT NULL
- process_duration (integer) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_01_136
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- post_group (character varying) | NOT NULL
- local_category (character varying) | NOT NULL
- kato (character varying) | NOT NULL
- rent_norm (double precision) | NOT NULL
- daily_avg (integer) | NOT NULL
- rent_avg (integer) | NOT NULL
- people_num (integer) | NOT NULL
- cost_avg (double precision) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_01_123_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_01_123
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- transport_type (character varying) | NOT NULL
- under7 (integer) | NOT NULL
- over7 (integer) | NOT NULL
- amount (integer) | NULL
- gu (character varying) | NOT NULL
- cur_year (integer) | NOT NULL
- expenses_amount_under7 (double precision) | NULL
- note (character varying) | NULL
- expenses_amount_over7 (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_01_136_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_01_139_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_01_143
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- recipient (character varying) | NULL
- average (numeric) | NULL
- rate (numeric) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- enstru_code (character varying) | NULL
- add_detail (character varying) | NULL
- unit_code (character varying) | NULL
- file_hash (character varying) | NULL
- category_id (character varying) | NULL
- recipient_kk (character varying) | NULL

---
### Table: budget_request_form_01_151
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- comm_service (character varying) | NOT NULL
- comm_object (character varying) | NOT NULL
- tariff (double precision) | NULL
- power (double precision) | NULL
- rate (double precision) | NULL
- correction_factors (double precision) | NULL
- note (character varying) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- category_id (character varying) | NOT NULL

---
### Table: budget_request_form_01_144_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_01_149
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- ward_type (character varying) | NOT NULL
- medp_count (integer) | NULL
- medp_cost (double precision) | NULL
- bed_amount (integer) | NULL
- price (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_01_151_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_01_144
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- model (character varying) | NOT NULL
- winter (integer) | NOT NULL
- number_cars (integer) | NULL
- engine (double precision) | NULL
- limit_mile (integer) | NULL
- cost_fuel (double precision) | NULL
- cost_coeff (double precision) | NULL
- gu (character varying) | NOT NULL
- cur_year (integer) | NOT NULL
- base_rate (double precision) | NULL
- months (integer) | NULL
- kind_fuel (character varying) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- note (character varying) | NULL

---
### Table: budget_request_form_01_153_decode
Columns:
- id (bigint) | NOT NULL
- category_id (character varying) | NOT NULL
- enstru_code (character varying) | NOT NULL
- add_detail (character varying) | NULL
- amount (numeric) | NOT NULL
- payment (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- file_hash (character varying) | NULL

---
### Table: budget_request_form_339_decode
Columns:
- id (integer) | NOT NULL
- category_id (character varying) | NOT NULL
- expense_code (character varying) | NOT NULL
- summa (numeric) | NOT NULL
- recipient_ru (character varying) | NULL
- recipient_kk (character varying) | NULL
- purpose_ru (character varying) | NULL
- purpose_kk (character varying) | NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_hash (character varying) | NULL

---
### Table: budget_request_form_01_159
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- repair (character varying) | NOT NULL
- amount (numeric) | NULL
- cost_avg (numeric) | NULL
- area (double precision) | NULL
- cost_sqm (double precision) | NULL
- cost_cur (double precision) | NULL
- gu (character varying) | NOT NULL
- cur_year (integer) | NOT NULL
- months (integer) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- enstru_code (character varying) | NULL
- add_detail (character varying) | NULL
- file_hash (character varying) | NULL

---
### Table: budget_request_form_01_169
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- unit (character varying) | NULL
- amount (integer) | NULL
- cost_avg (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_422
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- name_ru (character varying) | NULL
- period (character varying) | NOT NULL
- conclusion (character varying) | NOT NULL
- summa (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_133_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_01_162_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_01_169_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_01_162
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- code_position (character varying) | NOT NULL
- code_ks (character varying) | NOT NULL
- currency (double precision) | NOT NULL
- compensation (double precision) | NOT NULL
- rent_norm (double precision) | NOT NULL
- daily_avg (integer) | NOT NULL
- rent_avg (integer) | NOT NULL
- persons (integer) | NOT NULL
- cost_avg (double precision) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_01_161
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- post_group (character varying) | NOT NULL
- local_category (character varying) | NOT NULL
- kato (character varying) | NOT NULL
- rent_norm (double precision) | NOT NULL
- daily_avg (integer) | NOT NULL
- rent_avg (integer) | NOT NULL
- people_num (integer) | NOT NULL
- cost_avg (double precision) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_01_161_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_422_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_01_414
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- equipment (character varying) | NOT NULL
- amount (numeric) | NULL
- price1 (double precision) | NULL
- price2 (double precision) | NULL
- price3 (double precision) | NULL
- gu (character varying) | NOT NULL
- cur_year (integer) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- enstru_code (character varying) | NULL
- add_detail (character varying) | NULL
- unit_code (character varying) | NULL
- file_hash (character varying) | NULL
- cost (numeric) | NULL

---
### Table: budget_request_form_gkkp_163
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- unit (character varying) | NULL
- amount (integer) | NULL
- amount_days (integer) | NULL
- cost (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_01_416_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_02_111
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- ga (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NOT NULL
- spf (integer) | NOT NULL
- position (character varying) | NOT NULL
- experience (character varying) | NOT NULL
- staff_units (integer) | NOT NULL
- factor (double precision) | NOT NULL
- multi_factor (double precision) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_02_123
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- transport_type (character varying) | NOT NULL
- amount (integer) | NOT NULL
- gu (character varying) | NOT NULL
- cur_year (integer) | NOT NULL
- expenses_amount (double precision) | NULL
- note (character varying) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_01_413
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- code_group (character varying) | NOT NULL
- code_model (character varying) | NOT NULL
- amount_standard (integer) | NULL
- balance (integer) | NULL
- rent (integer) | NULL
- year_exit (integer) | NULL
- wear (integer) | NULL
- cost_budget (integer) | NULL
- amount_plan (integer) | NULL
- cost_unit (integer) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_01_339_regions
Columns:
- id (integer) | NOT NULL
- region (character varying) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- parent_id (integer) | NOT NULL
- count (double precision) | NOT NULL
- price (double precision) | NOT NULL
- total (double precision) | NOT NULL
- variant (character varying) | NULL
- data_type (integer) | NULL

---
### Table: budget_request_form_01_416
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- software (character varying) | NOT NULL
- amount (double precision) | NULL
- price (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_02_123_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_execution_alteration_income
Columns:
- id (integer) | NOT NULL
- budget_execution_alteration_request_id (bigint) | NOT NULL
- region (character varying) | NOT NULL
- year (integer) | NOT NULL
- kat (integer) | NOT NULL
- cls (integer) | NOT NULL
- pcl (integer) | NOT NULL
- spf (integer) | NOT NULL
- month (integer) | NOT NULL
- value (numeric) | NOT NULL
- create_date (timestamp without time zone) | NOT NULL
- update_date (timestamp without time zone) | NULL

---
### Table: budget_request_form_02_149
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- consumable (character varying) | NOT NULL
- amount (numeric) | NULL
- price1 (double precision) | NULL
- price2 (double precision) | NULL
- price3 (double precision) | NULL
- gu (character varying) | NOT NULL
- cur_year (integer) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- cost (numeric) | NOT NULL
- enstru_code (character varying) | NULL
- add_detail (character varying) | NULL
- unit_code (character varying) | NULL
- file_hash (character varying) | NULL

---
### Table: budget_request_form_02_151
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- watering (character varying) | NOT NULL
- comm_object (character varying) | NOT NULL
- tariff (double precision) | NULL
- power (double precision) | NULL
- rate (double precision) | NULL
- correction_factors (double precision) | NULL
- note (character varying) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- category_id (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_422
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- name_ru (character varying) | NULL
- period (character varying) | NOT NULL
- conclusion (character varying) | NOT NULL
- summa (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_02_159_1_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_411_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- unit (character varying) | NOT NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_411_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- unit (character varying) | NOT NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_419_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_419_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_execution_forms
Columns:
- id (bigint) | NOT NULL
- region (character varying) | NOT NULL
- year (integer) | NOT NULL
- month (integer) | NOT NULL
- abp (integer) | NULL
- flk (boolean) | NULL
- parent_id (bigint) | NULL
- budget_execution_forms_code (character varying) | NULL
- description (jsonb) | NULL

---
### Table: srs_form_data
Columns:
- id (integer) | NOT NULL
- year (integer) | NOT NULL
- code_kato1 (character varying) | NOT NULL
- code_kato2 (character varying) | NOT NULL
- code_kato3 (character varying) | NOT NULL
- indicator_code (character varying) | NOT NULL
- category_code (integer) | NULL
- status_code (integer) | NULL
- value_num (numeric) | NULL
- value_text (text) | NULL
- value_boolean (boolean) | NULL
- created_at (timestamp without time zone) | NOT NULL
- updated_at (timestamp without time zone) | NULL
- ate_code (character varying) | NOT NULL

---
### Table: budget_request_form_02_151_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_02_159_1
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- code_project (character varying) | NOT NULL
- code_program (character varying) | NULL
- cost_amount (double precision) | NOT NULL
- note (character varying) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_02_142_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_02_144
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- fuel (character varying) | NOT NULL
- fact_cost (double precision) | NULL
- area (double precision) | NULL
- months (double precision) | NULL
- price (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- enstru_code (character varying) | NULL
- add_detail (character varying) | NULL
- unit_code (character varying) | NULL
- file_hash (character varying) | NULL

---
### Table: budget_request_form_gkkp_422_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_03_141
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- recipient (character varying) | NULL
- average_meals (integer) | NULL
- func_day (integer) | NULL
- cost_meals (double precision) | NULL
- correction_factors (double precision) | NULL
- note (character varying) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- category_id (character varying) | NULL
- recipient_kk (character varying) | NULL

---
### Table: budget_request_form_02_339
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_02_339_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_execution_income
Columns:
- id (integer) | NOT NULL
- region (character varying) | NOT NULL
- year (integer) | NOT NULL
- kat (integer) | NOT NULL
- cls (integer) | NOT NULL
- pcl (integer) | NOT NULL
- spf (integer) | NOT NULL
- amount (numeric) | NOT NULL
- user_name (character varying) | NOT NULL
- user_id (character varying) | NOT NULL
- create_date (timestamp without time zone) | NOT NULL
- close_date (timestamp without time zone) | NULL
- month (integer) | NOT NULL

---
### Table: budget_request_form_02_414
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- code_cabinet (character varying) | NOT NULL
- code_furniture (character varying) | NOT NULL
- standard (integer) | NOT NULL
- amount (integer) | NOT NULL
- made_year (integer) | NOT NULL
- wear (double precision) | NOT NULL
- plan (integer) | NOT NULL
- cost (double precision) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_02_414_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_02_324_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_02_324
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- civil_type (character varying) | NOT NULL
- avg_annual_contingent0 (double precision) | NOT NULL
- amount_months (double precision) | NOT NULL
- state_scholarship (double precision) | NOT NULL
- avg_annual_contingent1 (double precision) | NOT NULL
- percentage_increase1 (double precision) | NOT NULL
- avg_annual_contingent2 (double precision) | NOT NULL
- percentage_increase2 (double precision) | NOT NULL
- avg_annual_contingent3 (double precision) | NOT NULL
- percentage_increase3 (double precision) | NOT NULL
- avg_annual_contingent4 (double precision) | NOT NULL
- size_scholarship (double precision) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_02_322_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_03_149
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- good_type (character varying) | NOT NULL
- amount (numeric) | NULL
- price (numeric) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- enstru_code (character varying) | NULL
- add_detail (character varying) | NULL
- unit_code (character varying) | NULL
- file_hash (character varying) | NULL

---
### Table: budget_request_form_03_151
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- comm_object (character varying) | NOT NULL
- tariff (double precision) | NULL
- power (double precision) | NULL
- rate (double precision) | NULL
- correction_factors (double precision) | NULL
- note (character varying) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- category_id (character varying) | NOT NULL

---
### Table: budget_request_form_03_159
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- area (double precision) | NULL
- rent (double precision) | NULL
- months (integer) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_03_159_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_04_141
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- recipient (character varying) | NOT NULL
- average_meals (double precision) | NULL
- func_day (integer) | NULL
- correction_factors (double precision) | NULL
- note (character varying) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_04_141_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_04_151
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- area (double precision) | NULL
- cost_avg (double precision) | NULL
- season (double precision) | NULL
- correction_factors (double precision) | NULL
- note (character varying) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_03_151_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_income_data_msu
Columns:
- id (bigint) | NOT NULL
- kat (integer) | NOT NULL
- cls (integer) | NOT NULL
- pcl (integer) | NOT NULL
- spf (integer) | NOT NULL
- amount (numeric) | NOT NULL
- note (character varying) | NOT NULL
- region (character varying) | NOT NULL
- year (integer) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- cur_year (integer) | NOT NULL
- update_date (timestamp without time zone) | NULL
- status (character varying) | NULL
- data_type (integer) | NOT NULL

---
### Table: budget_request_form_154
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- amount (integer) | NULL
- cost (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_155
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_execution_261abp_gu
Columns:
- id (integer) | NOT NULL
- gu (character varying) | NOT NULL
- parent_gu (character varying) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: budget_execution_alteration_flk
Columns:
- id_flk (integer) | NOT NULL
- request_type (character varying) | NOT NULL
- class (integer) | NOT NULL
- level (character varying) | NOT NULL
- id (bigint) | NOT NULL
- create_date (timestamp without time zone) | NOT NULL
- update_date (timestamp without time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_339_decode
Columns:
- id (integer) | NOT NULL
- category_id (character varying) | NOT NULL
- expense_code (character varying) | NOT NULL
- summa (numeric) | NOT NULL
- recipient_ru (character varying) | NULL
- recipient_kk (character varying) | NULL
- purpose_ru (character varying) | NULL
- purpose_kk (character varying) | NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_hash (character varying) | NULL

---
### Table: budget_request_form_157_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_154_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_155_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_156_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_212
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_213
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_311
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_321
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- total_employees (integer) | NOT NULL
- number_avg (double precision) | NOT NULL
- area (double precision) | NOT NULL
- price (double precision) | NOT NULL
- number_months (double precision) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_321_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_212_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_213_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_311_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_01_158
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- product_group (character varying) | NULL
- category_id (character varying) | NULL
- inf_sys_ru (character varying) | NULL
- inf_sys_kk (character varying) | NULL
- name_prod_ru (character varying) | NULL
- name_prod_kk (character varying) | NULL
- actual_expens (numeric) | NULL
- revis_plan (numeric) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_338
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_352
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_411
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_338_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_352_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_332_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_331_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_417
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- amount (integer) | NULL
- cost (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_418
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- unit (character varying) | NULL
- amount (integer) | NULL
- cost (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_419
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- amount (integer) | NULL
- cost (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_421_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_417_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_418_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_419_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_513
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_514_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_612_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_513_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_511_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_msu
Columns:
- id (bigint) | NOT NULL
- region (character varying) | NOT NULL
- form (character varying) | NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- value (numeric) | NOT NULL
- cur_year (integer) | NOT NULL
- bip_code (character varying) | NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NULL
- status (character varying) | NULL
- update_date (timestamp without time zone) | NULL
- value_source_link (text) | NULL

---
### Table: budget_request_form_gkkp_01_123
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- transport_type (character varying) | NOT NULL
- under7 (integer) | NOT NULL
- over7 (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- expenses_amount_under7 (double precision) | NULL
- note (character varying) | NULL
- expenses_amount_over7 (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_fact127
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NOT NULL
- kat_fgr (text) | NULL
- kls_fpgr (text) | NULL
- pkl_abp (text) | NULL
- spk_prg (text) | NULL
- pprg (text) | NULL
- spk (text) | NULL
- budget_type (character varying) | NOT NULL
- month (integer) | NOT NULL
- year (integer) | NOT NULL
- date_report (timestamp without time zone) | NOT NULL
- update_date (timestamp without time zone) | NOT NULL
- utv (numeric) | NOT NULL
- utch (numeric) | NOT NULL
- plg (numeric) | NOT NULL
- plgo (numeric) | NOT NULL
- plgp (numeric) | NOT NULL
- obz (numeric) | NOT NULL
- nplobz (numeric) | NOT NULL
- sumrg (numeric) | NOT NULL
- code_currency (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- source (character varying) | NOT NULL

---
### Table: budget_fact420
Columns:
- id (bigint) | NOT NULL
- budget_type (character varying) | NOT NULL
- kato (character varying) | NOT NULL
- func (text) | NULL
- espk (text) | NULL
- gu (text) | NOT NULL
- month (integer) | NOT NULL
- year (integer) | NOT NULL
- repdate (timestamp without time zone) | NOT NULL
- update_date (timestamp without time zone) | NOT NULL
- plg (numeric) | NOT NULL
- obaz (numeric) | NOT NULL
- plat (numeric) | NOT NULL
- registrob (numeric) | NOT NULL
- notexec (numeric) | NOT NULL
- sumrg (numeric) | NOT NULL
- curr_sumrg (numeric) | NOT NULL
- code_currency (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- source (character varying) | NOT NULL

---
### Table: budget_request_form_812
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NOT NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_813
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NOT NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_814
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NOT NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_815
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NOT NULL
- cost_amount (double precision) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- order (integer) | NULL
- file_name (character varying) | NULL
- gu (character varying) | NOT NULL
- file_blob (bytea) | NULL
- file_path (character varying) | NULL
- cur_year (integer) | NOT NULL
- file_type (character varying) | NULL
- change_time (date) | NULL
- user_name (character varying) | NULL
- update_data (timestamp without time zone) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL

---
### Table: budget_request_form_project
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- region (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- unit_code (character varying) | NOT NULL
- distance (double precision) | NULL
- population (integer) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL
- code (character varying) | NULL
- spf (integer) | NULL

---
### Table: budget_request_form_gkkp_01_123_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_02_149_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- category_id (character varying) | NOT NULL
- enstru_code (character varying) | NULL
- add_detail (character varying) | NULL
- staff_num (numeric) | NOT NULL
- norm_employee (integer) | NULL
- norm_division (integer) | NULL
- file_hash (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_total_gkkp
Columns:
- id (bigint) | NOT NULL
- region (character varying) | NOT NULL
- form (character varying) | NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- value (double precision) | NOT NULL
- cur_year (integer) | NOT NULL
- bip_code (character varying) | NULL
- variant (character varying) | NOT NULL
- user_id (character varying) | NULL
- update_date (timestamp without time zone) | NULL
- value_source_link (text) | NULL

---
### Table: budget_request_gchp
Columns:
- id (integer) | NOT NULL
- region (character varying) | NOT NULL
- form (character varying) | NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NOT NULL
- cur_year (integer) | NOT NULL
- variant (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- region_code (character varying) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_133_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_note_target_indicator
Columns:
- id (bigint) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- gu (character varying) | NOT NULL
- data_type_id (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- region (character varying) | NULL
- variant (character varying) | NULL
- forecast_id (bigint) | NOT NULL
- program_id (bigint) | NOT NULL
- goal_id (bigint) | NOT NULL
- indicator_id (bigint) | NOT NULL
- name_kk (text) | NULL
- name_ru (text) | NULL
- user_id (character varying) | NULL
- update_date (timestamp with time zone) | NOT NULL
- gkkp (character varying) | NULL

---
### Table: budget_request_note
Columns:
- id (bigint) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- gu (character varying) | NOT NULL
- data_type_id (integer) | NOT NULL
- year (integer) | NULL
- cur_year (integer) | NOT NULL
- region (character) | NULL
- variant (character) | NULL
- user_id (character) | NULL
- request_note_description_id (bigint) | NOT NULL
- update_date (timestamp with time zone) | NULL

---
### Table: budget_request_gchp_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_note_description
Columns:
- id (bigint) | NOT NULL
- name_kk (text) | NOT NULL
- name_ru (text) | NOT NULL
- title_indicator (character) | NOT NULL
- title_sorting (integer) | NOT NULL
- user_id (character) | NULL
- update_date (timestamp with time zone) | NULL

---
### Table: budget_request_form_gkkp_01_158
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- product_group (character varying) | NULL
- category_id (character varying) | NULL
- inf_sys_ru (character varying) | NULL
- inf_sys_kk (character varying) | NULL
- name_prod_ru (character varying) | NULL
- name_prod_kk (character varying) | NULL
- actual_expens (numeric) | NULL
- revis_plan (numeric) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: dict_answer_option
Columns:
- id (bigint) | NOT NULL
- parent_id (bigint) | NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- name_en (character varying) | NULL
- description (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- update_date (timestamp without time zone) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: dict_bp_conclusion_type1
Columns:
- id (bigint) | NOT NULL
- code (text) | NOT NULL
- name_ru (text) | NOT NULL
- name_kk (text) | NULL

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
### Table: cross_budget_kato
Columns:
- id (integer) | NOT NULL
- code_kato (character varying) | NOT NULL
- code_tax_region (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL
- num_ord (integer) | NULL

---
### Table: dict_bp_conclusion_type2
Columns:
- id (bigint) | NOT NULL
- code (text) | NOT NULL
- name_ru (text) | NOT NULL
- name_kk (text) | NULL

---
### Table: dict_bp_impl
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: dict_bp_dri
Columns:
- id (bigint) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- unit (text) | NULL

---
### Table: budget_request_form_gkkp_01_134
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- coefficient_salary (double precision) | NULL
- number_of_cases (integer) | NOT NULL
- number_of_jurors (integer) | NOT NULL
- process_duration (integer) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: dict_budget_data_types
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_bp_state
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: dict_bp_see
Columns:
- id (bigint) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- unit (text) | NULL

---
### Table: dict_car_groups
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_category
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- description (character varying) | NULL
- link (character varying) | NULL
- name_en (character varying) | NULL
- name_kz (character varying) | NULL
- name_ru (character varying) | NULL
- parent_id (bigint) | NULL
- update_date (timestamp without time zone) | NULL
- icon (character varying) | NULL

---
### Table: budget_request_form_gkkp_01_136
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- rent_norm (double precision) | NOT NULL
- daily_avg (integer) | NOT NULL
- rent_avg (integer) | NOT NULL
- people_num (integer) | NOT NULL
- cost_avg (double precision) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_fact534
Columns:
- id (integer) | NOT NULL
- period (date) | NOT NULL
- region_code (character varying) | NOT NULL
- budget_type (character varying) | NOT NULL
- funding_source (character varying) | NOT NULL
- iik (character varying) | NOT NULL
- opening_balance (numeric) | NOT NULL
- debit (numeric) | NOT NULL
- credit (numeric) | NOT NULL
- closing_balance (numeric) | NOT NULL
- update_date (timestamp without time zone) | NULL

---
### Table: dict_civil_scholars
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_comm_services
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_communications
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- unit_code (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL
- order (integer) | NULL
- par_id (integer) | NULL

---
### Table: dict_comp_equipment
Columns:
- id (integer) | NOT NULL
- par_id (integer) | NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL
- unit_code (character varying) | NULL

---
### Table: budget_request_form_01_322
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- name_ru (character varying) | NULL
- num_people (integer) | NOT NULL
- num_serv (double precision) | NOT NULL
- price (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- name_kk (character varying) | NULL

---
### Table: dict_consumables
Columns:
- id (integer) | NOT NULL
- par_id (integer) | NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL
- unit_code (character varying) | NULL

---
### Table: dict_comm_objects
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_climat_conds
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- zone (character varying) | NOT NULL
- months (integer) | NOT NULL
- begin_day (integer) | NOT NULL
- begin_month (integer) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL
- coefficient (integer) | NOT NULL

---
### Table: dict_files_type
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_enstru
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- name_en (character varying) | NULL
- detail_ru (character varying) | NOT NULL
- detail_kz (character varying) | NULL
- detail_en (character varying) | NULL
- standard (character varying) | NULL
- type (integer) | NOT NULL
- create_date (timestamp without time zone) | NOT NULL
- modify_date (timestamp without time zone) | NOT NULL
- active (boolean) | NOT NULL
- custom_name_ru (character varying) | NULL
- custom_name_kz (character varying) | NULL

---
### Table: dict_ebk_ek
Columns:
- id (bigint) | NOT NULL
- kat (integer) | NULL
- cls (integer) | NULL
- pcl (integer) | NULL
- spf (integer) | NULL
- name_ru (text) | NULL
- type (integer) | NULL
- full_code (text) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL
- short_name_ru (text) | NULL
- short_name_kk (text) | NULL
- name_kk (text) | NULL
- is_reg_4_09 (integer) | NULL

---
### Table: dict_enstru_new_code
Columns:
- id (bigint) | NOT NULL
- enstru_code (character varying) | NOT NULL
- new_code (character varying) | NOT NULL

---
### Table: dict_enstru_unit_code
Columns:
- id (bigint) | NOT NULL
- enstru_code (character varying) | NOT NULL
- unit_code (character varying) | NOT NULL

---
### Table: dict_ebk_doh
Columns:
- id (bigint) | NOT NULL
- kat (integer) | NULL
- cls (integer) | NULL
- pcl (integer) | NULL
- spf (integer) | NULL
- name_ru (text) | NULL
- type (integer) | NULL
- full_code (text) | NULL
- name_kk (text) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL
- budget_levels (character varying) | NULL
- budget_section (integer) | NULL

---
### Table: budget_request_form_gkkp_01_136_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: sign_file_params
Columns:
- id (bigint) | NOT NULL
- type_doc (character varying) | NOT NULL
- budget_level (character varying) | NOT NULL
- variant (character varying) | NOT NULL
- abp (integer) | NULL
- gu (character varying) | NULL
- create_date (timestamp without time zone) | NOT NULL

---
### Table: budget_request_form_01_322_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: dict_govern_officials
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_gsm
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL
- category (integer) | NULL

---
### Table: dict_object_category
Columns:
- id (bigint) | NOT NULL
- code (text) | NOT NULL
- name_ru (text) | NOT NULL
- name_kz (text) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_good_types
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- unit_code (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_furniture
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_military_rank
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NOT NULL
- name_kk (text) | NOT NULL
- name_ru (text) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL
- salary_increase (double precision) | NOT NULL
- cur_year (integer) | NULL

---
### Table: dict_military_title
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NOT NULL
- name_kk (text) | NOT NULL
- name_ru (text) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL
- salary_increase (double precision) | NOT NULL
- cur_year (integer) | NULL

---
### Table: dict_military_scholars
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL
- parent_code (character varying) | NULL

---
### Table: dict_local_categories
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- ab (character varying) | NULL
- cd (character varying) | NULL
- ef (character varying) | NULL
- ghi (character varying) | NULL

---
### Table: sign_file
Columns:
- id (bigint) | NOT NULL
- sign_file_params_id (bigint) | NOT NULL
- create_date (timestamp without time zone) | NOT NULL
- file_name (character varying) | NULL

---
### Table: dict_local_npa
Columns:
- id (bigint) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL
- ref (character varying) | NULL
- active (boolean) | NULL
- description (character varying) | NULL
- act_acceptance_ru (character varying) | NULL
- category_act (character varying) | NULL
- act_acceptance_kk (character varying) | NULL

---
### Table: dict_medical_staff
Columns:
- id (bigint) | NOT NULL
- parent_id (bigint) | NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- name_en (character varying) | NULL
- description (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- update_date (timestamp without time zone) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: budget_request_form_gkkp_01_139
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- summa (double precision) | NULL
- term (integer) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: dict_mutually_redeeming
Columns:
- id (integer) | NOT NULL
- source_id (integer) | NOT NULL
- fullcode (character varying) | NOT NULL
- zdspk12 (character varying) | NOT NULL
- adtype (integer) | NOT NULL
- fkr_id (integer) | NOT NULL
- prg_id (integer) | NOT NULL
- ppr_id (integer) | NOT NULL
- kpb_id (integer) | NOT NULL
- bdate (date) | NOT NULL
- edate (date) | NOT NULL
- nsithade8ey_version (integer) | NOT NULL
- abp (character varying) | NOT NULL
- prg (character varying) | NOT NULL
- ppr (character varying) | NOT NULL
- kat (character varying) | NOT NULL
- kls (character varying) | NOT NULL
- pkl (character varying) | NOT NULL
- spf (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_01_139_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: dict_position_salary
Columns:
- id (bigint) | NOT NULL
- pos_level (integer) | NOT NULL
- experience_min (integer) | NOT NULL
- experience_max (integer) | NOT NULL
- salary (double precision) | NOT NULL
- position_kind (character varying) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL
- cur_year (integer) | NULL

---
### Table: dict_position_mvd_salary
Columns:
- id (integer) | NOT NULL
- pos_level (integer) | NOT NULL
- experience_min (integer) | NOT NULL
- experience_max (integer) | NOT NULL
- salary (double precision) | NOT NULL
- position_kind (character varying) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL
- cur_year (integer) | NULL

---
### Table: budget_request_form_gkkp_01_322_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: dict_gu_kgkp
Columns:
- id (bigint) | NOT NULL
- name_ru (text) | NOT NULL
- name_kk (text) | NULL
- code_gu (character varying) | NULL
- code_gu_owner (character varying) | NULL
- bin (character varying) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL
- user_name (character varying) | NULL
- update_date (timestamp without time zone) | NULL

---
### Table: dict_object_state
Columns:
- id (bigint) | NOT NULL
- parent_id (bigint) | NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- name_en (character varying) | NULL
- description (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- update_date (timestamp without time zone) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: dict_period
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- description (character varying) | NULL
- name_en (character varying) | NULL
- name_kz (character varying) | NULL
- name_ru (character varying) | NULL
- update_date (timestamp without time zone) | NULL
- parent_id (bigint) | NULL

---
### Table: dict_object_and_welfare
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- description (character varying) | NULL
- name_en (character varying) | NULL
- name_kz (character varying) | NULL
- name_ru (character varying) | NULL
- update_date (timestamp without time zone) | NULL
- parent_id (bigint) | NULL

---
### Table: dict_npa
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL
- ref (character varying) | NULL
- active (boolean) | NULL
- description (character varying) | NULL
- act_acceptance_ru (character varying) | NULL
- category_act (character varying) | NULL
- act_acceptance_kk (character varying) | NULL
- code_region (character varying) | NULL

---
### Table: dict_passenger_transport
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- coefficient (double precision) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_organization_type_mvd
Columns:
- id (integer) | NOT NULL
- name_ru (text) | NOT NULL
- name_kk (text) | NOT NULL
- short_name_ru (text) | NULL
- short_name_kk (text) | NULL
- beg_date (date) | NOT NULL
- end_date (date) | NOT NULL

---
### Table: dict_position_category
Columns:
- id (bigint) | NOT NULL
- parent (bigint) | NULL
- type (character varying) | NOT NULL
- code (character varying) | NOT NULL

---
### Table: dict_rating
Columns:
- id (bigint) | NOT NULL
- parent_id (bigint) | NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- name_en (character varying) | NULL
- description (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- update_date (timestamp without time zone) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: dict_repairs
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- unit_code (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_program_goals
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- description (character varying) | NULL
- name_en (character varying) | NULL
- name_kz (character varying) | NULL
- name_ru (character varying) | NULL
- parent_id (bigint) | NULL
- update_date (timestamp without time zone) | NULL

---
### Table: dict_reasons
Columns:
- id (bigint) | NOT NULL
- parent_id (bigint) | NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- name_en (character varying) | NULL
- description (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- update_date (timestamp without time zone) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: dict_refund_allownce
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- daily_allownce (integer) | NOT NULL
- code_currency (character varying) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_refund_residence
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- rate_residence (integer) | NOT NULL
- code_ks (character varying) | NOT NULL
- code_trip_position (character varying) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_signatories
Columns:
- id (integer) | NOT NULL
- code_sign (character varying) | NOT NULL
- name_kz (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- short_name_kz (character varying) | NULL
- short_name_ru (character varying) | NULL
- update_date (timestamp without time zone) | NOT NULL
- user_name (character varying) | NOT NULL
- start_date (timestamp without time zone) | NOT NULL
- end_date (timestamp without time zone) | NULL

---
### Table: dict_program_event_status
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- description (character varying) | NULL
- name_en (character varying) | NULL
- name_kz (character varying) | NULL
- name_ru (character varying) | NULL
- parent_id (bigint) | NULL
- update_date (timestamp without time zone) | NULL

---
### Table: dict_transport_groups
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: budget_request_form_gkkp_01_141
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- recipient (character varying) | NULL
- cur_year (integer) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- category_id (character varying) | NULL
- recipient_kk (character varying) | NULL

---
### Table: dict_translate
Columns:
- code (character varying) | NOT NULL
- en (text) | NOT NULL
- kk (text) | NOT NULL
- ru (text) | NOT NULL
- description (text) | NULL

---
### Table: dict_transport_coefficient_region
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- coefficient (double precision) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_transfer
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- region_id (character varying) | NOT NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: dict_st_ead_dates
Columns:
- id (bigint) | NOT NULL
- ead (bigint) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: budget_request_form_gkkp_01_141_decode
Columns:
- id (bigint) | NOT NULL
- category_id (character varying) | NOT NULL
- enstru_code (character varying) | NOT NULL
- add_detail (character varying) | NULL
- unit_code (character varying) | NOT NULL
- num_day (integer) | NOT NULL
- num_meals (integer) | NOT NULL
- norm_per (double precision) | NOT NULL
- price_cur (double precision) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- file_hash (character varying) | NULL

---
### Table: appointment
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- name_en (character varying) | NULL
- module (character varying) | NOT NULL
- operation (character varying) | NOT NULL
- is_deleted (boolean) | NOT NULL

---
### Table: dict_type_agriculture_product
Columns:
- id (bigint) | NOT NULL
- parent_id (bigint) | NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- name_en (character varying) | NULL
- description (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- update_date (timestamp without time zone) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: dict_type_agriculture_subject
Columns:
- id (bigint) | NOT NULL
- parent_id (bigint) | NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- name_en (character varying) | NULL
- description (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- update_date (timestamp without time zone) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: dict_type_ats
Columns:
- id (bigint) | NOT NULL
- parent_id (bigint) | NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- name_en (character varying) | NULL
- description (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- update_date (timestamp without time zone) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: dict_type_land
Columns:
- id (bigint) | NOT NULL
- parent_id (bigint) | NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- name_en (character varying) | NULL
- description (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- update_date (timestamp without time zone) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: dict_type_medical_institution
Columns:
- id (bigint) | NOT NULL
- parent_id (bigint) | NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- name_en (character varying) | NULL
- description (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- update_date (timestamp without time zone) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: dict_type_need
Columns:
- id (bigint) | NOT NULL
- parent_id (bigint) | NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- name_en (character varying) | NULL
- description (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- update_date (timestamp without time zone) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: dict_type_post_office
Columns:
- id (bigint) | NOT NULL
- parent_id (bigint) | NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- name_en (character varying) | NULL
- description (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- update_date (timestamp without time zone) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: dict_type_agriculture_machine
Columns:
- id (bigint) | NOT NULL
- parent_id (bigint) | NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- name_en (character varying) | NULL
- description (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- update_date (timestamp without time zone) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: dict_trip_position
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_type_workshop
Columns:
- id (bigint) | NOT NULL
- parent_id (bigint) | NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- name_en (character varying) | NULL
- description (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- update_date (timestamp without time zone) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: budget_request_form_gkkp_01_142
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- recipient (character varying) | NULL
- average_patients (integer) | NULL
- func_day (integer) | NULL
- dispensing_rate (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- category_id (character varying) | NULL
- recipient_kk (character varying) | NULL

---
### Table: dict_type_water_source
Columns:
- id (bigint) | NOT NULL
- parent_id (bigint) | NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- name_en (character varying) | NULL
- description (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- update_date (timestamp without time zone) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: dict_user_operations
Columns:
- id (bigint) | NOT NULL
- parent_id (bigint) | NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- name_en (character varying) | NULL
- description (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- update_date (timestamp without time zone) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: dict_utilities_type
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- description (character varying) | NULL
- name_en (character varying) | NULL
- name_kz (character varying) | NULL
- name_ru (character varying) | NULL
- parent_id (bigint) | NULL
- update_date (timestamp without time zone) | NULL
- resource (character varying) | NULL

---
### Table: dict_village_status
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- description (character varying) | NULL
- name_en (character varying) | NULL
- name_kz (character varying) | NULL
- name_ru (character varying) | NULL
- update_date (timestamp without time zone) | NULL
- parent_id (bigint) | NULL

---
### Table: dict_ward
Columns:
- id (bigint) | NOT NULL
- par_id (bigint) | NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: dict_work_position_rank
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NOT NULL
- rank (integer) | NOT NULL
- rate (double precision) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL
- cur_year (integer) | NULL
- rate_remainder (double precision) | NULL

---
### Table: expenditureplan
Columns:
- id (integer) | NOT NULL
- region_id (integer) | NOT NULL
- month (integer) | NOT NULL
- code (character varying) | NOT NULL
- plan (double precision) | NOT NULL
- update_date (timestamp without time zone) | NOT NULL
- variant (integer) | NOT NULL
- year (integer) | NULL

---
### Table: efficiency_mark_zg
Columns:
- id (bigint) | NOT NULL
- abp (integer) | NULL
- fact (double precision) | NULL
- program (character varying) | NULL
- percent_development (double precision) | NULL
- plan (double precision) | NULL
- year (integer) | NULL
- program_id (bigint) | NULL
- apb (integer) | NULL
- create_date (timestamp without time zone) | NULL
- update_date (timestamp without time zone) | NULL
- achievement_ppr (double precision) | NULL
- efficiency (double precision) | NULL
- num (character varying) | NULL
- points_g (double precision) | NULL
- points_z (double precision) | NULL

---
### Table: efficiency_mark_l
Columns:
- id (bigint) | NOT NULL
- abp (integer) | NULL
- bp (integer) | NULL
- covered_funds_by_audit (double precision) | NULL
- create_date (timestamp without time zone) | NULL
- update_date (timestamp without time zone) | NULL
- violations_identified (double precision) | NULL
- year (integer) | NULL
- program_id (bigint) | NULL
- part_of_the_violations (character varying) | NULL
- points (double precision) | NULL
- sheetl_total_id (bigint) | NULL

---
### Table: efficiency_mark_fine_points
Columns:
- id (bigint) | NOT NULL
- create_date (timestamp without time zone) | NULL
- each_recorded_facts (double precision) | NULL
- number_of_facts (double precision) | NULL
- total (double precision) | NULL
- update_date (timestamp without time zone) | NULL
- year (integer) | NULL
- fine_criteria_id (bigint) | NULL
- program_id (bigint) | NULL

---
### Table: efficiency_mark_fine_criteria
Columns:
- id (bigint) | NOT NULL
- fine_name_en (character varying) | NULL
- fine_name_kz (character varying) | NULL
- fine_name_ru (character varying) | NULL

---
### Table: expenditure552
Columns:
- id (integer) | NOT NULL
- region_id (integer) | NOT NULL
- month (integer) | NOT NULL
- year (integer) | NOT NULL
- repdate (timestamp without time zone) | NOT NULL
- fond (character varying) | NOT NULL
- adm (character varying) | NOT NULL
- pr (character varying) | NOT NULL
- pdpr (character varying) | NOT NULL
- spec (character varying) | NOT NULL
- sum (double precision) | NOT NULL
- update_date (timestamp without time zone) | NOT NULL

---
### Table: budget_request_form_01_158_decode
Columns:
- id (integer) | NOT NULL
- category_id (character varying) | NOT NULL
- enstru_code (character varying) | NOT NULL
- add_detail (character varying) | NULL
- inf_sys_ru (character varying) | NULL
- inf_sys_kk (character varying) | NULL
- name_prod_ru (character varying) | NULL
- name_prod_kk (character varying) | NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_hash (character varying) | NULL

---
### Table: forecast_year
Columns:
- id (bigint) | NOT NULL
- fact (double precision) | NULL
- plan (double precision) | NULL
- year (integer) | NULL
- forecast_id (bigint) | NULL
- month (integer) | NULL
- frequency (character varying) | NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_01_158_decode
Columns:
- id (integer) | NOT NULL
- category_id (character varying) | NOT NULL
- enstru_code (character varying) | NOT NULL
- add_detail (character varying) | NULL
- inf_sys_ru (character varying) | NULL
- inf_sys_kk (character varying) | NULL
- name_prod_ru (character varying) | NULL
- name_prod_kk (character varying) | NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_hash (character varying) | NULL

---
### Table: forecast_exec
Columns:
- id (bigint) | NOT NULL
- forecast_id (bigint) | NOT NULL
- dict_ebk_func_abp (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: fulfillment_report_2
Columns:
- id (bigint) | NOT NULL
- form (character varying) | NULL
- date_from (date) | NULL
- date_to (date) | NULL
- region (character varying) | NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- name_en (character varying) | NULL
- repdate (timestamp without time zone) | NULL
- prg (integer) | NULL
- ppr (integer) | NULL
- spf (integer) | NULL
- gu (integer) | NULL

---
### Table: forecast_passport_file
Columns:
- id (bigint) | NOT NULL
- date (timestamp without time zone) | NULL
- name (character varying) | NULL
- size (bigint) | NULL
- program_id (bigint) | NULL

---
### Table: forecast_passport
Columns:
- id (bigint) | NOT NULL
- description (character varying) | NULL
- end_date (timestamp without time zone) | NULL
- name (character varying) | NULL
- start_date (timestamp without time zone) | NULL
- target (character varying) | NULL
- program_id (bigint) | NULL

---
### Table: input_form_data_periodicity
Columns:
- id (bigint) | NOT NULL
- dict_report_frequency_stat_id (bigint) | NULL
- input_form_indicator_id (bigint) | NOT NULL

---
### Table: input_form_data
Columns:
- id (bigint) | NOT NULL
- dict_1_item_id (bigint) | NULL
- dict_2_item_id (bigint) | NULL
- indicator_dict_1_item_id (bigint) | NULL
- indicator_dict_2_item_id (bigint) | NULL
- value (double precision) | NULL
- dict_report_frequency_stat_id (bigint) | NULL
- dict_input_form_data_type_id (bigint) | NULL
- input_form_indicator_id (bigint) | NOT NULL
- kato_stat_id (bigint) | NULL
- date (timestamp without time zone) | NULL
- key_cloak_id (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- update_date (timestamp without time zone) | NULL

---
### Table: input_form_data_type
Columns:
- id (bigint) | NOT NULL
- dict_input_form_data_type_id (bigint) | NULL
- input_form_indicator_id (bigint) | NOT NULL

---
### Table: budget_comm_tariffs
Columns:
- id (integer) | NOT NULL
- comm_service (character varying) | NOT NULL
- comm_object (character varying) | NOT NULL
- rate (double precision) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: justif_budget_adjust
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- is_income (boolean) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL
- correct_type (integer) | NULL

---
### Table: program_passport_file
Columns:
- id (bigint) | NOT NULL
- date (timestamp without time zone) | NULL
- name (character varying) | NULL
- size (bigint) | NULL
- program_id (bigint) | NULL

---
### Table: perform_ind_register
Columns:
- id (integer) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NOT NULL
- region (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- unit_code (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: input_forms
Columns:
- id (bigint) | NOT NULL
- dict_1_items (character varying) | NULL
- dict_2_items (character varying) | NULL
- dict_kato_items (character varying) | NULL
- dict_1_id (bigint) | NULL
- dict_2_id (bigint) | NULL
- name (character varying) | NULL
- dict_report_frequency_stat_id (bigint) | NULL
- link (character varying) | NULL

---
### Table: input_form_watchers
Columns:
- id (bigint) | NOT NULL
- key_cloak_id (character varying) | NULL
- input_form_id (bigint) | NOT NULL

---
### Table: list_gu_staff_pl
Columns:
- id (integer) | NOT NULL
- code_gu (character varying) | NOT NULL
- staff (double precision) | NULL
- no_staff (double precision) | NULL
- num (integer) | NULL
- staff_gov (double precision) | NULL
- staff_civil (double precision) | NULL

---
### Table: program_passport
Columns:
- id (bigint) | NOT NULL
- description (character varying) | NULL
- end_date (timestamp without time zone) | NULL
- name (character varying) | NULL
- start_date (timestamp without time zone) | NULL
- target (character varying) | NULL
- program_id (bigint) | NULL

---
### Table: sic_info_guide
Columns:
- id (integer) | NOT NULL
- sic_module_id (integer) | NOT NULL
- file_path (character varying) | NULL
- video_link (character varying) | NULL
- description (character varying) | NULL
- video_links (ARRAY) | NULL

---
### Table: sic_signatories
Columns:
- id (integer) | NOT NULL
- id_user (character varying) | NOT NULL
- code_modules (ARRAY) | NOT NULL
- code_forms (ARRAY) | NOT NULL
- code_sign (character varying) | NOT NULL
- order_num (integer) | NOT NULL
- name_kz (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- update_date (timestamp without time zone) | NOT NULL
- user_name (character varying) | NOT NULL
- start_date (date) | NOT NULL
- end_date (date) | NULL
- code_prg (ARRAY) | NULL
- code_region (character varying) | NULL
- code_abp (integer) | NULL
- code_gu (character varying) | NULL
- version (integer) | NULL
- code_reports (ARRAY) | NULL

---
### Table: budget_request_form_321_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: sm_data_customization
Columns:
- id (bigint) | NOT NULL
- title (character varying) | NULL
- type (character varying) | NULL
- sizex (integer) | NULL
- sizey (integer) | NULL
- category_id (bigint) | NULL

---
### Table: sm_data
Columns:
- id (bigint) | NOT NULL
- character (smallint) | NULL
- description (character varying) | NULL
- file_name (character varying) | NULL
- indicator_name (character varying) | NULL
- periodicity (character varying) | NULL
- sheet_name (character varying) | NULL
- source (character varying) | NULL
- text (character varying) | NULL
- unit_name (character varying) | NULL
- url (character varying) | NULL
- indicator_id (bigint) | NULL
- kato_stat_id (bigint) | NULL

---
### Table: sm_data_item
Columns:
- id (bigint) | NOT NULL
- date (timestamp without time zone) | NULL
- fact (double precision) | NULL
- plan (double precision) | NULL
- sm_data_id (bigint) | NOT NULL

---
### Table: budget_request_form_gkkp_01_144
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- model (character varying) | NOT NULL
- winter (integer) | NOT NULL
- number_cars (integer) | NULL
- engine (double precision) | NULL
- limit_mile (integer) | NULL
- cost_fuel (double precision) | NULL
- cost_coeff (double precision) | NULL
- cur_year (integer) | NOT NULL
- base_rate (double precision) | NULL
- months (integer) | NULL
- kind_fuel (character varying) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- note (character varying) | NULL

---
### Table: budget_request_form_gkkp_321_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: stafftab_rep2_val
Columns:
- id (bigint) | NOT NULL
- rep_row (bigint) | NOT NULL
- field (text) | NOT NULL
- v_text (text) | NULL
- v_number (double precision) | NULL
- v_moment (timestamp with time zone) | NULL
- v_boolean (boolean) | NULL

---
### Table: stafftab_rep_col
Columns:
- id (bigint) | NOT NULL
- report (bigint) | NOT NULL
- order_number (integer) | NOT NULL
- title_kk (text) | NOT NULL
- title_ru (text) | NOT NULL
- subtitle_kk (text) | NULL
- subtitle_ru (text) | NULL
- field (text) | NOT NULL
- date_field (boolean) | NOT NULL

---
### Table: stafftab_rep2_sheet
Columns:
- id (bigint) | NOT NULL
- report (bigint) | NOT NULL
- title_kk (text) | NOT NULL
- title_ru (text) | NOT NULL
- order_number (integer) | NOT NULL
- year (integer) | NOT NULL
- first_year (boolean) | NULL
- budget_subprogram (integer) | NULL

---
### Table: stafftab_file_storage
Columns:
- id (bigint) | NOT NULL
- region (character varying) | NOT NULL
- org (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- file_name (text) | NOT NULL
- variant_uuid (character varying) | NOT NULL
- cur_year (integer) | NOT NULL
- actual_date (timestamp without time zone) | NOT NULL
- upload_date (timestamp with time zone) | NOT NULL
- keycloak_user_id (character varying) | NOT NULL
- file_size (bigint) | NOT NULL

---
### Table: stafftab_gu_setting
Columns:
- id (bigint) | NOT NULL
- key (character varying) | NOT NULL
- v_text (text) | NULL
- v_number (double precision) | NULL
- version (bigint) | NOT NULL

---
### Table: stafftab_rep2_row
Columns:
- id (bigint) | NOT NULL
- sheet (bigint) | NOT NULL
- order_number (integer) | NOT NULL
- debug_info (text) | NULL

---
### Table: budget_request_form_gkkp_01_144_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: stafftab_repdata_01_121
Columns:
- id (bigint) | NOT NULL
- report (bigint) | NOT NULL
- order_number (integer) | NOT NULL
- debug_info (text) | NULL
- loc__name (text) | NULL
- loc__count (double precision) | NULL
- loc__salary_sum (double precision) | NULL
- loc__social_tax_rate (double precision) | NULL
- loc__social_tax_sum (double precision) | NULL

---
### Table: stafftab_repdata_01_122
Columns:
- id (bigint) | NOT NULL
- report (bigint) | NOT NULL
- order_number (integer) | NOT NULL
- debug_info (text) | NULL
- loc__nfot (double precision) | NULL
- loc__deduction_percent (double precision) | NULL
- loc__deduction_sum (double precision) | NULL

---
### Table: stafftab_repdata_01_124
Columns:
- id (bigint) | NOT NULL
- report (bigint) | NOT NULL
- order_number (integer) | NOT NULL
- debug_info (text) | NULL
- loc__salary_sum (double precision) | NULL
- loc__deduction_percent (double precision) | NULL
- loc__deduction_sum (double precision) | NULL

---
### Table: stafftab_report_total_link
Columns:
- id (bigint) | NOT NULL
- total (integer) | NOT NULL
- report (bigint) | NOT NULL
- send_moment (timestamp with time zone) | NOT NULL
- keycloak_user_id (character varying) | NULL

---
### Table: stafftab_repdata_01_116
Columns:
- id (bigint) | NOT NULL
- report (bigint) | NOT NULL
- order_number (integer) | NOT NULL
- debug_info (text) | NULL
- loc__count (double precision) | NULL
- loc__salary_month_sum (double precision) | NULL
- loc__pension_contribution_percent (double precision) | NULL
- loc__pension_contribution_month_sum (double precision) | NULL
- loc__pension_contribution_year_sum (double precision) | NULL

---
### Table: stafftab_repdata_01_113
Columns:
- id (bigint) | NOT NULL
- report (bigint) | NOT NULL
- order_number (integer) | NOT NULL
- debug_info (text) | NULL
- loc__position_category (text) | NULL
- loc__func_block_and_pos_level (text) | NULL
- loc__salary_month_sum (double precision) | NULL
- loc__bf_wellness (double precision) | NULL
- loc__bf_eco_disaster_health (double precision) | NULL
- loc__bf_year_sum (double precision) | NULL
- loc__bf_movement_lifting (double precision) | NULL
- loc__bf_fired (double precision) | NULL
- loc__cm_harmful_hazardous_conditions (double precision) | NULL
- loc__cm_special_work_conditions (double precision) | NULL
- loc__total (double precision) | NULL

---
### Table: stafftab_repdata_01_112
Columns:
- id (bigint) | NOT NULL
- report (bigint) | NOT NULL
- order_number (integer) | NOT NULL
- debug_info (text) | NULL
- loc__position_category (text) | NULL
- loc__salary_month_sum (double precision) | NULL
- loc__salary_month_increase (double precision) | NULL
- loc__premium (double precision) | NULL
- loc__one_time_payment (double precision) | NULL
- loc__total (double precision) | NULL

---
### Table: ttt
Columns:
- id (bigint) | NOT NULL
- txt (text) | NULL

---
### Table: ttt2
Columns:
- id (bigint) | NOT NULL

---
### Table: user_kat_link
Columns:
- id (integer) | NOT NULL
- user_id (character varying) | NOT NULL
- kat (integer) | NOT NULL

---
### Table: sync_tst
Columns:
- id (bigint) | NOT NULL
- title (text) | NULL

---
### Table: stat_update_setting
Columns:
- id (bigint) | NOT NULL
- stat_setting_link_id (bigint) | NOT NULL
- auto_update (boolean) | NULL
- auto_update_type (character varying) | NULL
- auto_update_week_day (integer) | NULL
- auto_update_day (integer) | NULL
- auto_update_month (integer) | NULL

---
### Table: user_abp_link
Columns:
- id (integer) | NOT NULL
- user_id (character varying) | NOT NULL
- abp (integer) | NOT NULL

---
### Table: user_fgr_link
Columns:
- id (integer) | NOT NULL
- user_id (character varying) | NOT NULL
- fgr (integer) | NOT NULL

---
### Table: user_gu_link
Columns:
- id (integer) | NOT NULL
- user_id (character varying) | NOT NULL
- gu (character varying) | NOT NULL

---
### Table: user_kato_link
Columns:
- id (bigint) | NOT NULL
- user_id (character varying) | NOT NULL
- kato (character varying) | NOT NULL

---
### Table: user_kgkp_link
Columns:
- id (bigint) | NOT NULL
- user_id (character varying) | NOT NULL
- kgkp (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_01_149
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- ward_type (character varying) | NOT NULL
- medp_count (integer) | NULL
- medp_cost (double precision) | NULL
- bed_amount (integer) | NULL
- price (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: user_workplace_link
Columns:
- id (integer) | NOT NULL
- user_id (character varying) | NOT NULL
- workplace (character varying) | NOT NULL
- lead (boolean) | NULL

---
### Table: budget_request_form_133_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: dict_indicator_type
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NOT NULL
- name_en (character varying) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: budget_request_form_gkkp_01_149_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: dict_indicator
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- description (character varying) | NULL
- name_en (character varying) | NULL
- name_kz (character varying) | NULL
- name_ru (character varying) | NULL
- update_date (timestamp without time zone) | NULL
- parent_id (bigint) | NULL
- character (integer) | NULL
- industry_stat_id (bigint) | NULL
- indicator_lvl (integer) | NULL
- num_ind (boolean) | NULL

---
### Table: staffing_table
Columns:
- id (bigint) | NOT NULL
- region (integer) | NULL
- creation_date (date) | NOT NULL
- pos (bigint) | NOT NULL
- admission_date (date) | NULL
- taking_office_date (date) | NOT NULL
- full_name (text) | NULL
- retiree (boolean) | NOT NULL
- time_rate (double precision) | NULL
- cd_date (date) | NULL
- cd_years (integer) | NULL
- cd_months (integer) | NULL
- cd_days (integer) | NULL
- vacancy (boolean) | NULL
- department (bigint) | NOT NULL
- experience_vacancy (double precision) | NULL
- work_start_date (date) | NULL
- work_end_date (date) | NULL
- bonus (boolean) | NULL
- serial_number (integer) | NULL
- edu_level (bigint) | NULL
- edu_subjects (ARRAY) | NULL

---
### Table: dict_civil_position_inc_rate
Columns:
- id (bigint) | NOT NULL
- func_block (character varying) | NULL
- level (bigint) | NULL
- activity_field (character varying) | NULL
- activity_field_exclusion (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL
- rate (double precision) | NOT NULL
- form (character varying) | NULL
- func_gr (integer) | NULL
- edu_hours_code (character varying) | NULL
- edu_org_type_code (character varying) | NULL
- ead_code (character varying) | NULL
- cur_year (integer) | NULL
- rate_remainder (double precision) | NULL

---
### Table: program_variant
Columns:
- id (bigint) | NOT NULL
- variant_uuid (character varying) | NOT NULL
- program_id (bigint) | NOT NULL
- actual (boolean) | NOT NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: budget_request_form_02_141
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- recipient (character varying) | NULL
- average_meals (integer) | NULL
- func_day (integer) | NULL
- cost_meals (double precision) | NULL
- tobacco (double precision) | NULL
- months (integer) | NULL
- correction_factors (double precision) | NULL
- note (character varying) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- category_id (character varying) | NULL
- recipient_kk (character varying) | NULL

---
### Table: budget_request_form_322
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- amount_first (integer) | NULL
- number_months (double precision) | NULL
- cost (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_423
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- period (character varying) | NOT NULL
- conclusion (character varying) | NULL
- summa (double precision) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: dict_budget_level
Columns:
- id (integer) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NOT NULL
- short_name_ru (character varying) | NULL
- short_name_kk (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL
- code (character varying) | NOT NULL
- emf_code (character varying) | NULL
- emf_level (smallint) | NULL

---
### Table: budget_request_bp_approve_history
Columns:
- id (bigint) | NOT NULL
- budget_request_bp (bigint) | NOT NULL
- update_time (timestamp with time zone) | NOT NULL
- approve_status (text) | NOT NULL
- note_ru (text) | NULL
- username (text) | NULL

---
### Table: budget_request_form_01_111
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- ga (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NOT NULL
- spf (integer) | NOT NULL
- job (character varying) | NOT NULL
- position (character varying) | NOT NULL
- experience (character varying) | NOT NULL
- staff_units (integer) | NOT NULL
- factor (double precision) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_01_141_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_02_159_2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- code_project (character varying) | NOT NULL
- code_program (character varying) | NULL
- cost_amount (double precision) | NOT NULL
- note (character varying) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_04_151_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_711_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: dict_bp_content
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: dict_program
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- description (character varying) | NULL
- end_date (timestamp without time zone) | NULL
- name_en (character varying) | NULL
- name_kz (character varying) | NULL
- name_ru (character varying) | NULL
- start_date (timestamp without time zone) | NULL
- update_date (timestamp without time zone) | NULL
- parent_id (bigint) | NULL
- module (character varying) | NULL
- kato_stat_id (bigint) | NULL
- code_kato (character varying) | NULL

---
### Table: dict_cabinets
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- budget_level_id (integer) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_ebk_func
Columns:
- id (integer) | NOT NULL
- gr (integer) | NULL
- pgr (integer) | NULL
- abp (integer) | NULL
- prg (integer) | NULL
- ppr (integer) | NULL
- name_ru (text) | NULL
- full_code (text) | NULL
- type (integer) | NULL
- name_kk (text) | NULL
- short_name_ru (text) | NULL
- short_name_kk (text) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL
- budget_level_id (integer) | NULL
- develop_type (integer) | NULL
- is_sequest (boolean) | NULL
- transfer (integer) | NULL
- budget_section (integer) | NULL

---
### Table: dict_position
Columns:
- id (bigint) | NOT NULL
- name_kk (text) | NOT NULL
- name_ru (text) | NOT NULL
- kind (character varying) | NOT NULL
- gov_level (character varying) | NULL
- func_block (character varying) | NULL
- pos_level (integer) | NOT NULL
- region (integer) | NULL
- category_level (integer) | NOT NULL
- category (bigint) | NULL
- category_number (character varying) | NULL

---
### Table: dict_unit
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- description (character varying) | NULL
- name_en (character varying) | NULL
- name_kz (character varying) | NULL
- name_ru (character varying) | NULL
- update_date (timestamp without time zone) | NULL
- parent_id (bigint) | NULL

---
### Table: dict_st_ead_dropdown_values
Columns:
- id (bigint) | NOT NULL
- ead (bigint) | NOT NULL
- value_number (double precision) | NULL
- value_bool (boolean) | NULL
- value_date (date) | NULL
- name_ru (text) | NOT NULL
- name_kk (text) | NOT NULL
- name_en (text) | NOT NULL
- code_region (character varying) | NULL
- sort_order (character varying) | NOT NULL

---
### Table: event_financing
Columns:
- id (bigint) | NOT NULL
- create_date (timestamp without time zone) | NULL
- event (text) | NULL
- fact (double precision) | NULL
- fact_period (character varying) | NULL
- percent (double precision) | NULL
- plan (double precision) | NULL
- source (character varying) | NULL
- update_date (timestamp without time zone) | NULL
- year (integer) | NULL
- direction_id (bigint) | NULL
- program_id (bigint) | NULL
- sphere_id (bigint) | NULL
- unit_stat_id (bigint) | NULL

---
### Table: sep_download_journal
Columns:
- id (bigint) | NOT NULL
- indicator_id (bigint) | NOT NULL
- file_id (bigint) | NOT NULL
- gu_id (bigint) | NULL
- user_name (character varying) | NULL
- indicator_date (character varying) | NULL
- created_on (timestamp without time zone) | NULL

---
### Table: sep_file
Columns:
- id (bigint) | NOT NULL
- name (character varying) | NOT NULL
- type (character varying) | NOT NULL
- size (bigint) | NOT NULL
- path (character varying) | NULL
- user_id (character varying) | NULL
- created_on (timestamp without time zone) | NULL

---
### Table: stafftab_rep2_col
Columns:
- id (bigint) | NOT NULL
- sheet (bigint) | NOT NULL
- order_number (integer) | NOT NULL
- title_kk (text) | NOT NULL
- title_ru (text) | NOT NULL
- subtitle_kk (text) | NOT NULL
- subtitle_ru (text) | NOT NULL
- field (text) | NOT NULL
- date_field (boolean) | NOT NULL
- spec_type (character varying) | NULL
- subprogram (integer) | NULL
- hidden (boolean) | NULL
- excel_width (integer) | NULL
- use_integer_format (boolean) | NULL
- subprog_dist_group_code (character varying) | NULL
- subprog_dist_group_type (character varying) | NULL
- result_col (boolean) | NOT NULL

---
### Table: bip_agreement
Columns:
- id (integer) | NOT NULL
- bip_code (character varying) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- status (integer) | NOT NULL
- variant (character varying) | NOT NULL
- region (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- cur_year (integer) | NOT NULL
- comment_txt (character varying) | NULL
- user_id (character varying) | NULL
- update_date (timestamp without time zone) | NOT NULL

---
### Table: bip_agreement_hist
Columns:
- id (integer) | NOT NULL
- ba_id (bigint) | NOT NULL
- status (bigint) | NOT NULL
- comment_txt (character varying) | NULL
- user_id (character varying) | NULL
- update_date (timestamp without time zone) | NOT NULL

---
### Table: agreement_status
Columns:
- id (integer) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- name_en (character varying) | NULL
- code (integer) | NOT NULL
- btn_name_ru (character varying) | NULL
- btn_name_kk (character varying) | NULL
- btn_name_en (character varying) | NULL

---
### Table: agreement_mode
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name (character varying) | NULL

---
### Table: agreement_step
Columns:
- id (integer) | NOT NULL
- mode_code (character varying) | NOT NULL
- agr_code (integer) | NOT NULL
- step_code (integer) | NOT NULL
- step_type (integer) | NOT NULL

---
### Table: bip_criteria_values
Columns:
- id (integer) | NOT NULL
- criteria (character varying) | NOT NULL
- link (integer) | NOT NULL
- value (double precision) | NULL
- weight (double precision) | NULL
- max (double precision) | NULL
- min (double precision) | NULL
- year (integer) | NULL
- user_name (character varying) | NULL
- update_time (timestamp without time zone) | NULL

---
### Table: bip_form_data
Columns:
- id (integer) | NOT NULL
- form_data (jsonb) | NULL
- update_date (date) | NULL
- user_name (character varying) | NULL
- region (character varying) | NULL
- variant (character varying) | NULL
- status (character varying) | NULL
- update_time (timestamp without time zone) | NULL
- variant_recipient (character varying) | NULL

---
### Table: pkfo_1
Columns:
- id (integer) | NOT NULL
- line_code (character varying) | NULL
- year (integer) | NULL
- cur_year (integer) | NULL
- evaluation_value (double precision) | NULL
- forecast_value (double precision) | NULL
- id_budget_version (character varying) | NULL
- abp (integer) | NULL

---
### Table: appendix_8
Columns:
- id (integer) | NOT NULL
- code (character varying) | NULL
- year (integer) | NULL
- cur_year (integer) | NULL
- evaluation_value (double precision) | NULL
- forecast_value (double precision) | NULL
- id_budget_version (character varying) | NULL
- abp (integer) | NULL

---
### Table: budget_cross_field
Columns:
- id (integer) | NOT NULL
- kat (integer) | NOT NULL
- cls (integer) | NULL
- pcl (integer) | NULL
- spf (integer) | NULL
- kato (character varying) | NOT NULL
- field (character varying) | NOT NULL
- year (integer) | NOT NULL

---
### Table: budget_request_form_321_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: bip_link_types
Columns:
- id (integer) | NOT NULL
- object_type (character varying) | NOT NULL
- project_type (character varying) | NOT NULL
- place (character varying) | NULL
- begin_date (date) | NOT NULL
- end_date (date) | NULL
- is_deleted (boolean) | NULL
- user_name (character varying) | NULL
- update_time (timestamp without time zone) | NULL

---
### Table: budget_request_form_gkkp_01_151
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- comm_service (character varying) | NOT NULL
- comm_object (character varying) | NOT NULL
- tariff (double precision) | NULL
- power (double precision) | NULL
- rate (double precision) | NULL
- correction_factors (double precision) | NULL
- note (character varying) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- category_id (character varying) | NOT NULL

---
### Table: bip_object_directions
Columns:
- id (integer) | NOT NULL
- code_object (character varying) | NOT NULL
- code_direction (character varying) | NOT NULL

---
### Table: bip_project_status_list
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- name_en (character varying) | NULL
- begin_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: budget_execution_alteration_block
Columns:
- id (bigint) | NOT NULL
- region (character varying) | NULL
- block (boolean) | NOT NULL
- form_4_20 (boolean) | NOT NULL
- prev (boolean) | NOT NULL
- current (boolean) | NOT NULL
- next (boolean) | NOT NULL
- user_id (character varying) | NOT NULL
- user_name (character varying) | NULL
- create_date (timestamp without time zone) | NOT NULL
- type (smallint) | NOT NULL

---
### Table: bip_project_type_list
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- name_en (character varying) | NULL
- begin_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: budget_balance_structure
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- order_nom (integer) | NOT NULL
- type_id (integer) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- description (character varying) | NOT NULL
- condition (character varying) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: budget_execution_alteration
Columns:
- id (integer) | NOT NULL
- budget_execution_alteration_request_id (bigint) | NOT NULL
- region (character varying) | NOT NULL
- year (integer) | NOT NULL
- gu (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- month (integer) | NOT NULL
- value (numeric) | NOT NULL
- create_date (timestamp without time zone) | NOT NULL
- update_date (timestamp without time zone) | NULL
- plan_type (smallint) | NOT NULL
- bip_code (character varying) | NULL
- left_month (integer) | NOT NULL
- expense_code (character varying) | NULL

---
### Table: budget_clarify_rate_bp
Columns:
- id (bigint) | NOT NULL
- variant (character varying) | NOT NULL
- bp_dri_id (bigint) | NOT NULL
- indic_val (double precision) | NULL

---
### Table: budget_cost_project
Columns:
- id (integer) | NOT NULL
- source (integer) | NOT NULL
- region (integer) | NOT NULL
- gr (integer) | NOT NULL
- pgr (integer) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- prj (integer) | NOT NULL
- name_ppi (character varying) | NULL
- ind_value (double precision) | NULL
- amount_correct (double precision) | NOT NULL
- ind_change (integer) | NULL
- amount_obk (double precision) | NULL
- note (character varying) | NULL
- year (integer) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL

---
### Table: budget_distribution_standard
Columns:
- id (integer) | NOT NULL
- kat (integer) | NOT NULL
- cls (integer) | NOT NULL
- pcl (integer) | NULL
- spf (integer) | NULL
- region (character varying) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- region_per (double precision) | NOT NULL
- district_per (double precision) | NOT NULL
- beg_date (date) | NOT NULL
- end_date (date) | NOT NULL
- user_id (character varying) | NULL
- update_date (timestamp without time zone) | NULL

---
### Table: budget_request_form_336
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_336_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: bip_link_criterias
Columns:
- id (integer) | NOT NULL
- link (integer) | NOT NULL
- criteria (character varying) | NOT NULL

---
### Table: budget_execution_ipf
Columns:
- id (integer) | NOT NULL
- region (character varying) | NOT NULL
- year (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- defective (character varying) | NOT NULL
- user_id (character varying) | NULL
- date_creation (timestamp without time zone) | NULL
- gr (integer) | NULL

---
### Table: budget_income_clarif
Columns:
- id (integer) | NOT NULL
- region (character varying) | NOT NULL
- kat (integer) | NOT NULL
- cls (integer) | NOT NULL
- pcl (integer) | NOT NULL
- spf (integer) | NOT NULL
- change (double precision) | NOT NULL
- note (character varying) | NULL
- year (integer) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- amount_obk (double precision) | NULL

---
### Table: budget_income_correct
Columns:
- id (integer) | NOT NULL
- kat (integer) | NOT NULL
- cls (integer) | NOT NULL
- pcl (integer) | NOT NULL
- spf (integer) | NOT NULL
- field (character varying) | NOT NULL
- value (double precision) | NOT NULL
- year (integer) | NOT NULL
- region (character varying) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- is_correct_counted (boolean) | NULL
- note (character varying) | NULL

---
### Table: budget_request_form_gkkp_336_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_411_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_fact552
Columns:
- id (integer) | NOT NULL
- region_id (character varying) | NOT NULL
- month (integer) | NOT NULL
- year (integer) | NOT NULL
- repdate (timestamp without time zone) | NOT NULL
- fond (character varying) | NOT NULL
- abp (character varying) | NOT NULL
- prg (character varying) | NOT NULL
- ppr (character varying) | NOT NULL
- spf (character varying) | NOT NULL
- sum (double precision) | NOT NULL
- update_date (timestamp without time zone) | NOT NULL
- gu (character varying) | NULL
- sum_month (double precision) | NULL
- sum_day (double precision) | NULL

---
### Table: budget_request_form_gkkp_336
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- name_kk (character varying) | NULL

---
### Table: budget_form_balance_structure
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- order_nom (integer) | NOT NULL
- type_id (integer) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- description (character varying) | NOT NULL
- condition (character varying) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL
- conditionP (character varying) | NULL
- budget_section (character varying) | NULL

---
### Table: budget_form_balance_structure_free
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- order_nom (integer) | NOT NULL
- type_id (integer) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- description (character varying) | NOT NULL
- condition (character varying) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL
- conditionP (character varying) | NULL

---
### Table: budget_limit_data
Columns:
- id (integer) | NOT NULL
- kat (integer) | NOT NULL
- cls (integer) | NOT NULL
- pcl (integer) | NOT NULL
- spf (integer) | NOT NULL
- cash (double precision) | NULL
- contingent (double precision) | NULL
- regional (double precision) | NULL
- district (double precision) | NULL
- region (character varying) | NOT NULL
- note (character varying) | NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_date (timestamp without time zone) | NULL

---
### Table: budget_limit_standard
Columns:
- id (integer) | NOT NULL
- kat (integer) | NOT NULL
- cls (integer) | NOT NULL
- pcl (integer) | NOT NULL
- spf (integer) | NOT NULL
- name_ru (text) | NOT NULL
- local (integer) | NULL

---
### Table: budget_form_limits
Columns:
- id (integer) | NOT NULL
- spf (integer) | NOT NULL
- fact_sum (double precision) | NULL
- plan_sum (double precision) | NULL
- one_time_expenses (double precision) | NULL
- forecast_for_year (double precision) | NULL
- forecast_one (boolean) | NOT NULL
- percent_of_growth (double precision) | NULL
- forecast_two (boolean) | NOT NULL
- forecast_for_two_years (double precision) | NULL
- over_expenses (double precision) | NULL
- forecast_three (boolean) | NOT NULL
- forecast_for_three_years (double precision) | NULL
- update_date (timestamp without time zone) | NOT NULL
- year (integer) | NOT NULL
- region_id (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- ga (character varying) | NOT NULL
- user_id (character varying) | NULL
- rb_transfert (double precision) | NULL
- corrected_plan (double precision) | NULL

---
### Table: budget_request_form_519
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_01_151_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_bp_dri
Columns:
- id (bigint) | NOT NULL
- budget_request_bp (bigint) | NOT NULL
- parent (bigint) | NULL
- indicator (bigint) | NOT NULL
- region (text) | NULL
- unit (text) | NULL
- gov_prg (text) | NULL
- report_year (double precision) | NULL
- correct_plan (double precision) | NULL
- plan_period1 (double precision) | NULL
- plan_period2 (double precision) | NULL
- plan_period3 (double precision) | NULL
- project (bigint) | NULL
- bip (text) | NULL
- final_result (text) | NULL
- concl_ru (text) | NULL
- note_ru (text) | NULL

---
### Table: budget_request_form_01_153
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- group (character varying) | NOT NULL
- amount (numeric) | NULL
- payment (numeric) | NULL
- months (integer) | NULL
- gu (character varying) | NOT NULL
- cur_year (integer) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- category_id (character varying) | NULL

---
### Table: budget_request_bp_npa
Columns:
- id (bigint) | NOT NULL
- budget_request_bp (bigint) | NOT NULL
- npa (bigint) | NOT NULL

---
### Table: budget_request_form_519_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_bp_pee
Columns:
- id (bigint) | NOT NULL
- budget_request_bp (bigint) | NOT NULL
- region (text) | NULL
- project (bigint) | NULL
- bip (text) | NULL
- expend_report_year (double precision) | NULL
- expend_correct_plan (double precision) | NULL
- expend_plan_period1 (double precision) | NULL
- expend_plan_period2 (double precision) | NULL
- expend_plan_period3 (double precision) | NULL
- note_ru (text) | NULL

---
### Table: budget_request_bp_see
Columns:
- id (bigint) | NOT NULL
- budget_request_bp (bigint) | NOT NULL
- region (text) | NULL
- project (bigint) | NULL
- bip (text) | NULL
- see (bigint) | NOT NULL
- eff_report_year (double precision) | NULL
- eff_correct_plan (double precision) | NULL
- eff_plan_period1 (double precision) | NULL
- eff_plan_period2 (double precision) | NULL
- eff_plan_period3 (double precision) | NULL
- expend_report_year (double precision) | NULL
- expend_correct_plan (double precision) | NULL
- expend_plan_period1 (double precision) | NULL
- expend_plan_period2 (double precision) | NULL
- expend_plan_period3 (double precision) | NULL
- note_ru (text) | NULL

---
### Table: appendix_9
Columns:
- id (integer) | NOT NULL
- code (character varying) | NULL
- year (integer) | NULL
- cur_year (integer) | NULL
- evaluation_value (double precision) | NULL
- forecast_value (double precision) | NULL
- id_budget_version (character varying) | NULL
- abp (integer) | NULL

---
### Table: budget_request_form_01_141_decode
Columns:
- id (bigint) | NOT NULL
- category_id (character varying) | NOT NULL
- enstru_code (character varying) | NOT NULL
- add_detail (character varying) | NULL
- unit_code (character varying) | NOT NULL
- num_day (integer) | NOT NULL
- num_meals (integer) | NOT NULL
- norm_per (double precision) | NOT NULL
- price_cur (double precision) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- file_hash (character varying) | NULL

---
### Table: budget_request_form_332
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_519_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_01_142
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- recipient (character varying) | NULL
- average_patients (integer) | NULL
- func_day (integer) | NULL
- dispensing_rate (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- category_id (character varying) | NULL
- recipient_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_519
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_01_152_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: dict_items_appendix_7
Columns:
- id (integer) | NOT NULL
- section (integer) | NULL
- subsection (character varying) | NULL
- parent_code (character varying) | NULL
- code (character varying) | NULL
- spf (integer) | NULL
- name_kk (text) | NULL
- name_ru (text) | NULL
- pkfo_1_code (character varying) | NULL
- pkfo_2_code (character varying) | NULL
- pkfo_3_code (character varying) | NULL
- description_ru (text) | NULL
- description_kk (text) | NULL
- reduction (integer) | NULL
- is_calculation (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_items_pkfo1
Columns:
- id (integer) | NOT NULL
- section (integer) | NULL
- subsection (integer) | NULL
- line_code (character varying) | NULL
- name_kk (text) | NULL
- name_ru (text) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: budget_request_form_01_324
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- scholar_type (character varying) | NOT NULL
- avg_annual (double precision) | NOT NULL
- amount_months (double precision) | NOT NULL
- salary (double precision) | NOT NULL
- surcharge (double precision) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_01_339
Columns:
- id (integer) | NOT NULL
- region (character varying) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- total (double precision) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_322_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_01_339_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_321_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: dict_fuel_types
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: budget_request_form_02_141_decode
Columns:
- id (bigint) | NOT NULL
- category_id (character varying) | NOT NULL
- enstru_code (character varying) | NOT NULL
- add_detail (character varying) | NULL
- unit_code (character varying) | NOT NULL
- num_meals (integer) | NOT NULL
- num_day (integer) | NOT NULL
- norm_per (double precision) | NOT NULL
- price_cur (double precision) | NOT NULL
- price_indexed (double precision) | NOT NULL
- index_inf (double precision) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- file_hash (character varying) | NULL

---
### Table: budget_request_form_01_152
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- communication (character varying) | NOT NULL
- amount (integer) | NULL
- abonent (double precision) | NULL
- time_based (double precision) | NULL
- payment (double precision) | NULL
- cost (double precision) | NULL
- months (integer) | NULL
- rent (double precision) | NULL
- traffic (double precision) | NULL
- gu (character varying) | NOT NULL
- cur_year (integer) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- enstru_code (character varying) | NULL
- add_detail (character varying) | NULL
- unit_code (character varying) | NULL

---
### Table: budget_request_form_02_159_2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: copy_stafftab_ead_с
Columns:
- id (bigint) | NULL
- value_bool (boolean) | NULL
- value_text (text) | NULL
- value_number (double precision) | NULL
- value_salary_rate (double precision) | NULL
- value_norm_rate (double precision) | NULL
- value_date (date) | NULL
- ead (bigint) | NULL
- allow_rate (boolean) | NULL
- version (bigint) | NULL
- budget_program (integer) | NULL
- calc_hint (ARRAY) | NULL

---
### Table: copy_dict_st_ead
Columns:
- id (bigint) | NULL
- code (character varying) | NULL
- attr_type (character varying) | NULL
- kind (character varying) | NULL
- name_kk (text) | NULL
- name_ru (text) | NULL
- subtitle_kk (text) | NULL
- subtitle_ru (text) | NULL
- dict_norm_ind_code (character varying) | NULL
- pre_multiplier (double precision) | NULL
- value_column_title_template (text) | NULL
- value_column_title_multiplier (double precision) | NULL
- allow_budget_prog_select (boolean) | NULL
- allow_fact_workload_calc (boolean) | NULL

---
### Table: copy_stafftab_ead_d
Columns:
- id (bigint) | NULL
- emp (bigint) | NULL
- conf (bigint) | NULL
- value_bool (boolean) | NULL
- value_text (text) | NULL
- value_number (double precision) | NULL
- value_salary_rate (double precision) | NULL
- value_norm_rate (double precision) | NULL
- value_date (date) | NULL
- value_military_rank (bigint) | NULL
- value_military_title (bigint) | NULL
- budget_program (integer) | NULL
- calc_hint (ARRAY) | NULL
- fact_hours (double precision) | NULL

---
### Table: budget_request_form_02_142
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- branches (character varying) | NULL
- patients_count (integer) | NULL
- treatment_cost (double precision) | NULL
- average_day (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- branches_kk (character varying) | NULL

---
### Table: budget_request_form_02_322
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_133
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_163
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- unit (character varying) | NULL
- amount (integer) | NULL
- amount_days (integer) | NULL
- cost (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: dict_items_pkfo2
Columns:
- id (integer) | NOT NULL
- line_code (character varying) | NULL
- name_kk (text) | NULL
- name_ru (text) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: budget_request_form_03_142
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- visits_count (integer) | NULL
- cost_visits (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_03_142_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: dict_items_pkfo3
Columns:
- id (integer) | NOT NULL
- section (integer) | NULL
- line_code (character varying) | NULL
- name_kk (text) | NULL
- name_ru (text) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: budget_request_form_133_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: dict_items_pkfo4
Columns:
- id (integer) | NOT NULL
- line_code (character varying) | NULL
- name_kk (text) | NULL
- name_ru (text) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: budget_request_form_02_149_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- category_id (character varying) | NOT NULL
- enstru_code (character varying) | NULL
- add_detail (character varying) | NULL
- staff_num (numeric) | NOT NULL
- norm_employee (integer) | NULL
- norm_division (integer) | NULL
- file_hash (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: dict_wear_rate
Columns:
- id (integer) | NOT NULL
- parent_code (character varying) | NULL
- code (character varying) | NULL
- name_kk (text) | NULL
- name_ru (text) | NULL
- rate (integer) | NULL

---
### Table: dict_items_appendix_8
Columns:
- id (integer) | NOT NULL
- code (character varying) | NULL
- spf (integer) | NULL
- name_kk (text) | NULL
- name_ru (text) | NULL
- pkfo_2_code (character varying) | NULL
- is_calculation (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_items_appendix_9
Columns:
- id (integer) | NOT NULL
- section (integer) | NULL
- code (character varying) | NULL
- spf (integer) | NULL
- pkfo_3_code (character varying) | NULL
- name_kk (text) | NULL
- name_ru (text) | NULL
- is_calculation (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: budget_request_form_163_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_execution_alteration_request_deleted_log
Columns:
- id (bigint) | NOT NULL
- number (bigint) | NOT NULL
- date (timestamp without time zone) | NOT NULL
- user_id (character varying) | NOT NULL
- user_name (character varying) | NULL
- delete_date (timestamp without time zone) | NOT NULL
- request_id (bigint) | NULL
- region (character varying) | NULL
- abp (integer) | NULL
- gu (character varying) | NULL
- request_type (character varying) | NULL
- level (character varying) | NULL
- description (character varying) | NULL

---
### Table: budget_request_form_gkkp_01_152
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- communication (character varying) | NOT NULL
- amount (integer) | NULL
- abonent (double precision) | NULL
- time_based (double precision) | NULL
- payment (double precision) | NULL
- cost (double precision) | NULL
- months (integer) | NULL
- rent (double precision) | NULL
- traffic (double precision) | NULL
- cur_year (integer) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- enstru_code (character varying) | NULL
- add_detail (character varying) | NULL
- unit_code (character varying) | NULL

---
### Table: budget_request_form_gkkp_322_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_322_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_133_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_02_159
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- enstru_code (character varying) | NULL
- add_detail (character varying) | NULL
- unit_code (character varying) | NULL
- file_hash (character varying) | NULL
- amount (numeric) | NULL
- price (numeric) | NULL
- category_id (character varying) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_412_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_411_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_423_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_total_agreement_spf
Columns:
- id (bigint) | NOT NULL
- variant (character varying) | NOT NULL
- region (character varying) | NOT NULL
- cur_year (integer) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- status (integer) | NOT NULL
- user_id (character varying) | NULL
- update_date (timestamp without time zone) | NOT NULL
- data_type (character varying) | NOT NULL
- comment_txt (character varying) | NULL

---
### Table: budget_request_form_total_agreement_spf_hist
Columns:
- id (bigint) | NOT NULL
- brftas_id (bigint) | NOT NULL
- status (integer) | NOT NULL
- comment_txt (character varying) | NULL
- update_date (timestamp without time zone) | NOT NULL
- user_id (character varying) | NULL

---
### Table: budget_bc_payment_schedule_forecast
Columns:
- id (bigint) | NOT NULL
- id_contract (bigint) | NOT NULL
- type_schedule (smallint) | NOT NULL
- sum_payment (double precision) | NULL
- payment_date (date) | NOT NULL
- code (character varying) | NULL
- user_name (character varying) | NULL
- update_date (timestamp without time zone) | NULL
- note (character varying) | NULL
- date_beg (date) | NULL
- date_end (date) | NULL
- day_count (integer) | NULL
- sum_base (double precision) | NULL

---
### Table: budget_request_form_01_141
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- recipient (character varying) | NULL
- average_meals (integer) | NULL
- func_day (integer) | NULL
- cost_meals (double precision) | NULL
- correction_factors (double precision) | NULL
- note (character varying) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- category_id (character varying) | NULL
- recipient_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_01_322
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- name_ru (character varying) | NULL
- num_people (integer) | NOT NULL
- num_serv (double precision) | NOT NULL
- price (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_156
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- amount (integer) | NULL
- cost (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_157
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- amount (integer) | NULL
- cost (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_331
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_412
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- unit (character varying) | NULL
- amount (integer) | NULL
- cost (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_421
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- period (character varying) | NOT NULL
- conclusion (character varying) | NOT NULL
- summa (double precision) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_511
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_total_agreement
Columns:
- id (bigint) | NOT NULL
- variant (character varying) | NOT NULL
- region (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- cur_year (integer) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- gu (character varying) | NULL
- status (integer) | NOT NULL
- user_id (character varying) | NULL
- update_date (timestamp without time zone) | NOT NULL
- comment_txt (character varying) | NULL

---
### Table: budget_watering_tariffs
Columns:
- id (integer) | NOT NULL
- comm_object (character varying) | NOT NULL
- watering (character varying) | NOT NULL
- region_obl (character varying) | NOT NULL
- rate (double precision) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: budget_request_form_514
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_612
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_711
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_712_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_712
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_total_agreement_hist
Columns:
- id (bigint) | NOT NULL
- brfta_id (bigint) | NOT NULL
- status (integer) | NOT NULL
- comment_txt (character varying) | NULL
- update_date (timestamp without time zone) | NOT NULL
- user_id (character varying) | NULL

---
### Table: appendix_7
Columns:
- id (integer) | NOT NULL
- code (character varying) | NULL
- year (integer) | NULL
- cur_year (integer) | NULL
- evaluation_value (double precision) | NULL
- forecast_value (double precision) | NULL
- id_budget_version (character varying) | NULL
- abp (integer) | NULL
- evaluation_date (date) | NULL
- forecast_date (date) | NULL
- forecast_type (character varying) | NULL

---
### Table: budget_request_form_total
Columns:
- id (integer) | NOT NULL
- region (character varying) | NOT NULL
- form (character varying) | NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- value (double precision) | NOT NULL
- gu (character varying) | NOT NULL
- cur_year (integer) | NOT NULL
- bip_code (character varying) | NULL
- variant (character varying) | NULL
- user_name (character varying) | NULL
- status (character varying) | NULL
- update_date (timestamp without time zone) | NULL
- value_source_link (text) | NULL
- type_source (integer) | NOT NULL

---
### Table: budget_request_form_322_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budgetfact
Columns:
- id (integer) | NOT NULL
- region_id (integer) | NOT NULL
- month (integer) | NOT NULL
- code (character varying) | NOT NULL
- sum (double precision) | NOT NULL
- update_date (timestamp without time zone) | NOT NULL
- variant (integer) | NOT NULL
- year (integer) | NULL

---
### Table: kfo_1
Columns:
- id (integer) | NOT NULL
- abp (integer) | NOT NULL
- dateinfo (date) | NOT NULL
- gucode (character varying) | NOT NULL
- sumend (numeric) | NULL
- templ (character varying) | NULL

---
### Table: budget_variants
Columns:
- id (integer) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- name_en (character varying) | NULL
- variant_uuid (character varying) | NOT NULL
- year (integer) | NULL
- data_type (integer) | NULL
- attribute (boolean) | NOT NULL
- status (boolean) | NOT NULL
- basis_ru (text) | NULL
- date_time (date) | NULL
- is_deleted (boolean) | NOT NULL
- prev_variant (character varying) | NULL
- next_variant (character varying) | NULL
- region_code (character varying) | NULL
- date_ueb (date) | NULL
- date_abp (date) | NULL
- basis_kk (text) | NULL
- date_start (date) | NULL
- update_date (timestamp without time zone) | NULL
- user_name (character varying) | NULL

---
### Table: budgetplan
Columns:
- id (integer) | NOT NULL
- region_id (integer) | NOT NULL
- month (integer) | NOT NULL
- code (character varying) | NOT NULL
- plan (double precision) | NOT NULL
- update_date (timestamp without time zone) | NOT NULL
- variant (character varying) | NOT NULL
- year (integer) | NULL
- kat (integer) | NULL
- cls (integer) | NULL
- pcl (integer) | NULL
- spf (integer) | NULL
- repdate (timestamp without time zone) | NULL

---
### Table: budget_request_form_gkkp_513_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: kfo_2
Columns:
- id (integer) | NOT NULL
- abp (integer) | NOT NULL
- dateinfo (date) | NOT NULL
- gucode (character varying) | NOT NULL
- sumend (numeric) | NULL
- sumstart (numeric) | NULL
- templ (character varying) | NULL

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
### Table: kfo_3
Columns:
- id (integer) | NOT NULL
- abp (integer) | NOT NULL
- dateinfo (date) | NOT NULL
- gucode (character varying) | NOT NULL
- sumlastperiod (numeric) | NULL
- sumperiod (numeric) | NULL
- templ (character varying) | NULL

---
### Table: dict_bp_level
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: dict_bp_project
Columns:
- id (bigint) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_total_gkkp_paid
Columns:
- id (bigint) | NOT NULL
- region (character varying) | NOT NULL
- form (character varying) | NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- value (double precision) | NOT NULL
- cur_year (integer) | NOT NULL
- bip_code (character varying) | NULL
- variant (character varying) | NOT NULL
- user_id (character varying) | NULL
- update_date (timestamp without time zone) | NULL
- value_source_link (text) | NULL

---
### Table: dict_cellular_operator
Columns:
- id (bigint) | NOT NULL
- parent_id (bigint) | NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- name_en (character varying) | NULL
- description (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- update_date (timestamp without time zone) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: dict_civil_position
Columns:
- id (bigint) | NOT NULL
- func_block (character varying) | NOT NULL
- level (bigint) | NULL
- level_number (integer) | NULL
- name_kk (text) | NOT NULL
- name_ru (text) | NOT NULL
- pos_level (integer) | NULL
- activity_field (character varying) | NULL

---
### Table: budget_request_form_gkkp_01_152_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: dict_civil_position_level
Columns:
- id (bigint) | NOT NULL
- parent (bigint) | NULL
- type (character varying) | NOT NULL
- code (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_322_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_01_153
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- group (character varying) | NOT NULL
- amount (numeric) | NULL
- payment (numeric) | NULL
- months (integer) | NULL
- cur_year (integer) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- category_id (character varying) | NULL

---
### Table: dict_civil_position_rate
Columns:
- id (bigint) | NOT NULL
- kind (character varying) | NOT NULL
- func_block (character varying) | NOT NULL
- level (bigint) | NULL
- activity_field (character varying) | NULL
- experience_min (integer) | NOT NULL
- experience_max (integer) | NOT NULL
- rate (double precision) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL
- cur_year (integer) | NULL
- rate_remainder (double precision) | NULL

---
### Table: budget_request_form_155_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- summa (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: dict_currency
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- code_ks (character varying) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_dicts
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- description (character varying) | NULL
- name_en (character varying) | NULL
- name_kz (character varying) | NULL
- name_ru (character varying) | NULL
- parent_id (bigint) | NULL
- update_date (timestamp without time zone) | NULL
- resource (character varying) | NULL

---
### Table: dict_direction
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- description (character varying) | NULL
- name_en (character varying) | NULL
- name_kz (character varying) | NULL
- name_ru (character varying) | NULL
- update_date (timestamp without time zone) | NULL
- parent_id (bigint) | NULL

---
### Table: dict_division_names
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- order_num (character varying) | NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: kfo_4
Columns:
- id (integer) | NOT NULL
- abp (integer) | NOT NULL
- dateinfo (date) | NOT NULL
- finans (numeric) | NULL
- finresult (numeric) | NULL
- gucode (character varying) | NOT NULL
- reserve (numeric) | NULL
- sum (numeric) | NULL
- templ (character varying) | NULL

---
### Table: budget_sign_hash
Columns:
- id (bigint) | NOT NULL
- variant (character varying) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NULL
- hash (text) | NOT NULL
- mode_type (character varying) | NOT NULL
- update_date (timestamp without time zone) | NOT NULL

---
### Table: dict_fulfillment_rep
Columns:
- id (integer) | NOT NULL
- code (character varying) | NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- name_en (character varying) | NULL
- full_name_ru (character varying) | NULL
- full_name_kz (character varying) | NULL
- full_name_en (character varying) | NULL
- active (integer) | NULL
- type (integer) | NULL
- level (character varying) | NULL
- bdate (date) | NULL
- edate (date) | NULL

---
### Table: dict_gu_main
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_form
Columns:
- id (bigint) | NOT NULL
- form (character varying) | NOT NULL
- num_pril (character varying) | NOT NULL
- name_form (text) | NOT NULL

---
### Table: dict_gu
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- source_id (character varying) | NOT NULL
- summary_flag (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- gu_bin (character varying) | NULL
- gu_rnn (character varying) | NULL
- id_region (character varying) | NOT NULL
- id_budget_type (character varying) | NULL
- address (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL
- kato (character varying) | NULL
- budget_type (character varying) | NULL
- rucov (character varying) | NULL
- buhgal (character varying) | NULL
- abp_owner (character varying) | NULL
- id_nsi (bigint) | NULL
- id_iisk (numeric) | NULL
- budget_level (character varying) | NULL
- secret (character varying) | NULL
- committee (character varying) | NULL
- minlevel (character varying) | NULL
- id_gbdul (character varying) | NULL
- code_kfs (character varying) | NULL
- code_okpo (character varying) | NULL
- id_egz (character varying) | NULL
- source (character varying) | NULL
- nsithade8ey_version (character varying) | NULL
- short_name_ru (character varying) | NULL
- short_name_kz (character varying) | NULL
- short_name_en (character varying) | NULL
- is_publicity (character varying) | NULL
- budget_manag (character varying) | NULL
- org_attribute (character varying) | NULL
- status (character varying) | NULL
- code_loaded (character varying) | NULL
- last_update_date (timestamp without time zone) | NULL
- subject_kvazi_sector (character varying) | NULL
- code_kopf (character varying) | NULL
- name_en (character varying) | NULL

---
### Table: dict_gu_department
Columns:
- id (bigint) | NOT NULL
- name_kk (text) | NOT NULL
- name_ru (text) | NOT NULL
- parent (bigint) | NULL
- serial_number (integer) | NULL
- version (bigint) | NOT NULL

---
### Table: dict_input_form_data_type
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- description (character varying) | NULL
- name_en (character varying) | NULL
- name_kz (character varying) | NULL
- name_ru (character varying) | NULL
- parent_id (bigint) | NULL
- update_date (timestamp without time zone) | NULL

---
### Table: dict_integration_category
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- description (character varying) | NULL
- link (character varying) | NULL
- name_en (character varying) | NULL
- name_kz (character varying) | NULL
- name_ru (character varying) | NULL
- parent_id (bigint) | NULL
- update_date (timestamp without time zone) | NULL
- icon (character varying) | NULL

---
### Table: budget_request_form_gkkp_155_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- summa (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: project_bank_task_values
Columns:
- id (bigint) | NOT NULL
- task_id (bigint) | NOT NULL
- year (integer) | NOT NULL
- value (numeric) | NOT NULL
- created_at (timestamp without time zone) | NULL

---
### Table: budget_limit_gu
Columns:
- id (bigint) | NOT NULL
- variant (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- gu (character varying) | NOT NULL
- cur_year (integer) | NOT NULL
- value1 (double precision) | NOT NULL
- value2 (double precision) | NOT NULL
- value3 (double precision) | NOT NULL
- user_id (character varying) | NOT NULL
- update_date (timestamp without time zone) | NOT NULL
- ppr (integer) | NULL

---
### Table: dict_mvd_pos_coefficient
Columns:
- id (integer) | NOT NULL
- kind (character varying) | NOT NULL
- category (character varying) | NOT NULL
- id_type_org (integer) | NOT NULL
- id_bud_lev (integer) | NOT NULL
- experience_min (integer) | NOT NULL
- experience_max (integer) | NOT NULL
- coefficient (double precision) | NOT NULL
- beg_date (date) | NOT NULL
- end_date (date) | NULL
- cur_year (integer) | NULL

---
### Table: dict_reasons_apps
Columns:
- id (integer) | NOT NULL
- type (integer) | NULL
- name_ru (text) | NULL
- name_kk (text) | NULL
- name_en (text) | NULL
- gr_pl_id (integer) | NULL
- gr_ob_id (integer) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_post_groups
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL

---
### Table: app9_spf_reason_dependency
Columns:
- id (integer) | NOT NULL
- spf (integer) | NOT NULL
- reason_id (integer) | NULL

---
### Table: dict_st_ead_acv
Columns:
- id (bigint) | NOT NULL
- ead (bigint) | NOT NULL
- value (double precision) | NOT NULL

---
### Table: dict_org
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NOT NULL
- gu (integer) | NULL
- kgkp (bigint) | NULL

---
### Table: dict_potential_snp
Columns:
- id (bigint) | NOT NULL
- parent_id (bigint) | NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- name_en (character varying) | NULL
- description (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- update_date (timestamp without time zone) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: budget_request_form_gkkp_01_153_decode
Columns:
- id (bigint) | NOT NULL
- category_id (character varying) | NOT NULL
- enstru_code (character varying) | NOT NULL
- add_detail (character varying) | NULL
- amount (numeric) | NOT NULL
- payment (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- file_hash (character varying) | NULL

---
### Table: dict_software
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- unit_code (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_sphere
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- description (character varying) | NULL
- name_en (character varying) | NULL
- name_kz (character varying) | NULL
- name_ru (character varying) | NULL
- update_date (timestamp without time zone) | NULL
- parent_id (bigint) | NULL

---
### Table: dict_mvd_position
Columns:
- id (integer) | NOT NULL
- category (character varying) | NOT NULL
- num_in_categ (integer) | NULL
- name_kk (text) | NOT NULL
- name_ru (text) | NOT NULL
- id_type_org (integer) | NOT NULL
- id_bud_lev (integer) | NOT NULL
- kind (character varying) | NOT NULL
- level (integer) | NULL

---
### Table: dict_normative_inds
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- short_name_ru (character varying) | NOT NULL
- short_name_kk (character varying) | NULL
- value (double precision) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL
- cur_year (integer) | NULL
- year (integer) | NULL

---
### Table: dict_work_position_inc_rate
Columns:
- id (bigint) | NOT NULL
- rate (double precision) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL
- cur_year (integer) | NULL
- rate_remainder (double precision) | NULL

---
### Table: dict_work_exper
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: budget_execution_application9_reasons
Columns:
- id (integer) | NOT NULL
- region (character varying) | NOT NULL
- date (date) | NOT NULL
- func (character varying) | NOT NULL
- reason_id (integer) | NULL
- reason_sum (numeric) | NULL
- type (integer) | NULL

---
### Table: dict_type_road_surface
Columns:
- id (bigint) | NOT NULL
- parent_id (bigint) | NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- name_en (character varying) | NULL
- description (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- update_date (timestamp without time zone) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: budget_request_form_155_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: dict_type_service_area
Columns:
- id (bigint) | NOT NULL
- parent_id (bigint) | NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- name_en (character varying) | NULL
- description (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- update_date (timestamp without time zone) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: dict_transport_models
Columns:
- id (integer) | NOT NULL
- code (character varying) | NULL
- type (character varying) | NOT NULL
- model (character varying) | NOT NULL
- engine (integer) | NULL
- gearbox (character varying) | NULL
- base_rate (double precision) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_type_sport_facility
Columns:
- id (bigint) | NOT NULL
- parent_id (bigint) | NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- name_en (character varying) | NULL
- description (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- update_date (timestamp without time zone) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: dict_transport_service_life
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- coefficient (double precision) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_transport_types
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- coefficient (double precision) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_watering
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: efficiency_mark_criteria
Columns:
- id (bigint) | NOT NULL
- abbreviation (character varying) | NULL
- criteria_for_evaluation_en (character varying) | NULL
- criteria_for_evaluation_kz (character varying) | NULL
- criteria_for_evaluation_ru (character varying) | NULL

---
### Table: budget_execution_settings
Columns:
- id (integer) | NOT NULL
- code (character varying) | NULL
- value (boolean) | NULL

---
### Table: stafftab_action_log
Columns:
- id (integer) | NOT NULL
- module_type (character varying) | NOT NULL
- record_id (integer) | NOT NULL
- user_id (character varying) | NOT NULL
- stafftab_version (bigint) | NOT NULL
- action_type (character varying) | NOT NULL
- create_date (timestamp without time zone) | NOT NULL
- change_details (character varying) | NOT NULL

---
### Table: stafftab_emp_setting_log
Columns:
- id (integer) | NOT NULL
- setting_type (character varying) | NOT NULL
- emp_id (integer) | NOT NULL
- stafftab_version (bigint) | NOT NULL
- action_type (character varying) | NOT NULL
- create_date (timestamp without time zone) | NOT NULL
- user_id (character varying) | NOT NULL
- change_details (character varying) | NOT NULL

---
### Table: efficiency_mark_total_results
Columns:
- id (bigint) | NOT NULL
- audit_total (double precision) | NULL
- create_date (timestamp without time zone) | NULL
- goals_title (character varying) | NULL
- goals_value (integer) | NULL
- part_of_the_violations_total (double precision) | NULL
- points_and_goals_total (double precision) | NULL
- points_total (double precision) | NULL
- update_date (timestamp without time zone) | NULL
- violations_total (double precision) | NULL
- year (integer) | NULL
- criteria_id (bigint) | NULL
- program_id (bigint) | NULL
- final_points (double precision) | NULL
- final_sheet_result (double precision) | NULL
- first_indicator (double precision) | NULL
- second_indicator (double precision) | NULL

---
### Table: fulfillment_form_2_1
Columns:
- id (integer) | NOT NULL
- code (character varying) | NULL
- reasons (character varying) | NULL
- report_id (integer) | NOT NULL
- abp (integer) | NULL
- region (character varying) | NULL
- date_from (date) | NULL
- date_to (date) | NULL
- form (character varying) | NULL

---
### Table: event_execution
Columns:
- id (bigint) | NOT NULL
- create_date (timestamp without time zone) | NULL
- deadline (character varying) | NULL
- event (text) | NULL
- exec_condition (timestamp without time zone) | NULL
- exec_information (text) | NULL
- resp_executors (character varying) | NULL
- update_date (timestamp without time zone) | NULL
- year (integer) | NULL
- direction_id (bigint) | NULL
- program_id (bigint) | NULL
- sphere_id (bigint) | NULL
- status_id (bigint) | NULL
- status (character varying) | NULL

---
### Table: forecast
Columns:
- id (bigint) | NOT NULL
- direction_id (bigint) | NULL
- indicator_id (bigint) | NULL
- program_id (bigint) | NULL
- sphere_id (bigint) | NULL
- kato_stat_id (bigint) | NULL
- unit_stat_id (bigint) | NULL
- stat_setting_id (bigint) | NULL
- coefficient (double precision) | NULL
- executor (character varying) | NULL
- indicator_custom_name (character varying) | NULL
- sm_data_id (bigint) | NULL
- arithmetic_operation (character varying) | NULL
- indicator_custom_name_en (character varying) | NULL
- indicator_custom_name_kz (character varying) | NULL
- program_goals_id (bigint) | NULL
- sgp_parent_doc_id (bigint) | NULL
- macroindicator (boolean) | NULL
- indicator_type_id (bigint) | NULL
- decomp_id (character varying) | NULL
- variant (character varying) | NULL

---
### Table: file_data
Columns:
- id (integer) | NOT NULL
- hash_sum (character varying) | NOT NULL
- file_name (character varying) | NOT NULL
- description (json) | NOT NULL
- username (character varying) | NULL

---
### Table: file_data_upload
Columns:
- id (integer) | NOT NULL
- hash_sum (character varying) | NOT NULL
- file_path (character varying) | NOT NULL
- file_name (character varying) | NOT NULL
- date_upload (timestamp without time zone) | NULL
- date_report (timestamp without time zone) | NULL
- upload_status (integer) | NULL
- cnt (integer) | NULL
- erorr (character varying) | NULL
- description (character varying) | NULL
- username (character varying) | NULL

---
### Table: file_test
Columns:
- id (integer) | NOT NULL
- blob (bytea) | NOT NULL

---
### Table: forecast_ebk_func
Columns:
- id (bigint) | NOT NULL
- gr (integer) | NOT NULL
- pgr (integer) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- forecast (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_155_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: dict_calculation_forms
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL
- spf (integer) | NULL
- num_pril (character varying) | NULL
- req_ord (character varying) | NULL
- gkkp_paid (boolean) | NULL
- docum (boolean) | NULL
- version (integer) | NULL
- cur_year_beg (integer) | NULL
- cur_year_end (integer) | NULL

---
### Table: budget_request_form_815_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: input_form_indicator
Columns:
- id (bigint) | NOT NULL
- dict_1_items (character varying) | NULL
- dict_2_items (character varying) | NULL
- dict_1_id (bigint) | NULL
- dict_2_id (bigint) | NULL
- indicator_id (bigint) | NULL
- input_form_id (bigint) | NOT NULL
- unit_stat_id (bigint) | NULL
- index (integer) | NULL
- sm (boolean) | NULL
- input_form_tab_id (bigint) | NULL

---
### Table: input_form_responsible_executors
Columns:
- id (bigint) | NOT NULL
- key_cloak_id (character varying) | NULL
- input_form_id (bigint) | NOT NULL

---
### Table: input_form_tab
Columns:
- id (bigint) | NOT NULL
- index (integer) | NOT NULL
- name (character varying) | NOT NULL
- create_date (timestamp without time zone) | NULL
- update_date (timestamp without time zone) | NULL
- input_form_id (bigint) | NOT NULL

---
### Table: budget_request_form_gkkp_01_159
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- repair (character varying) | NOT NULL
- amount (numeric) | NULL
- cost_avg (numeric) | NULL
- area (double precision) | NULL
- cost_sqm (double precision) | NULL
- cur_year (integer) | NOT NULL
- months (integer) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- enstru_code (character varying) | NULL
- add_detail (character varying) | NULL
- file_hash (character varying) | NULL

---
### Table: budget_limit_gkkp
Columns:
- id (bigint) | NOT NULL
- variant (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- gu_main (character varying) | NOT NULL
- gkkp (character varying) | NOT NULL
- cur_year (integer) | NOT NULL
- value1 (double precision) | NOT NULL
- value2 (double precision) | NOT NULL
- value3 (double precision) | NOT NULL
- user_id (character varying) | NOT NULL
- update_date (timestamp without time zone) | NOT NULL
- ppr (integer) | NULL

---
### Table: stafftab_rep_val
Columns:
- id (bigint) | NOT NULL
- rep_row (bigint) | NOT NULL
- field (text) | NOT NULL
- v_text (text) | NULL
- v_number (double precision) | NULL
- v_moment (timestamp with time zone) | NULL
- v_boolean (boolean) | NULL

---
### Table: sm_indicator_config
Columns:
- id (bigint) | NOT NULL
- coefficient (double precision) | NULL
- title (character varying) | NULL
- type (character varying) | NULL
- unit_stat_id (bigint) | NULL
- sm_data_id (bigint) | NULL
- sm_data_customization_id (bigint) | NOT NULL
- diff_axis (boolean) | NOT NULL

---
### Table: sep_indicator
Columns:
- id (bigint) | NOT NULL
- gu_id (bigint) | NULL
- name (character varying) | NOT NULL
- active (boolean) | NULL
- created_on (timestamp without time zone) | NULL

---
### Table: sic_guide
Columns:
- id (integer) | NOT NULL
- sic_module_id (integer) | NOT NULL
- file_path (character varying) | NULL
- video_link (character varying) | NULL
- description (character varying) | NULL

---
### Table: budget_request_form_gkkp_815_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: stafftab_ap_form_link
Columns:
- id (bigint) | NOT NULL
- ap (character varying) | NOT NULL
- form (character varying) | NOT NULL

---
### Table: sic_modules
Columns:
- id (integer) | NOT NULL
- par_id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- status (character varying) | NULL

---
### Table: sic_guide_file
Columns:
- id (integer) | NOT NULL
- date (timestamp without time zone) | NULL
- file_path (character varying) | NULL
- name (character varying) | NULL
- size (bigint) | NULL
- sic_module_id (integer) | NOT NULL

---
### Table: stafftab_emp_setting
Columns:
- id (bigint) | NOT NULL
- emp (bigint) | NOT NULL
- key (character varying) | NOT NULL
- v_text (text) | NULL
- v_number (double precision) | NULL

---
### Table: stafftab_repdata_01_111
Columns:
- id (bigint) | NOT NULL
- report (bigint) | NOT NULL
- order_number (integer) | NOT NULL
- debug_info (text) | NULL
- loc__position_category (text) | NULL
- loc__func_block_and_pos_level (text) | NULL
- loc__position_names (text) | NULL
- loc__cnt (double precision) | NULL
- loc__salary_month_sum (double precision) | NULL
- loc__total_salary_month_sum (double precision) | NULL
- loc__total_salary_year_sum (double precision) | NULL
- loc__fact_expense_sum (double precision) | NULL
- al_by_pprk_1193 (double precision) | NULL
- al_by_pprk_1193__cnt (double precision) | NULL
- al_by_pprk_646 (double precision) | NULL
- al_by_pprk_646__cnt (double precision) | NULL
- al_car_with_trailer (double precision) | NULL
- al_car_with_trailer__cnt (double precision) | NULL
- al_grade (double precision) | NULL
- al_grade__cnt (double precision) | NULL
- al_grade_qualification (double precision) | NULL
- al_grade_qualification__cnt (double precision) | NULL
- al_honorary_title (double precision) | NULL
- al_honorary_title__cnt (double precision) | NULL
- al_hqsrrmscl (double precision) | NULL
- al_hqsrrmscl__cnt (double precision) | NULL
- al_law_research (double precision) | NULL
- al_law_research__cnt (double precision) | NULL
- al_prof_excellence (double precision) | NULL
- al_prof_excellence__cnt (double precision) | NULL
- al_seniority (double precision) | NULL
- al_seniority__cnt (double precision) | NULL
- al_special_work_conditions (double precision) | NULL
- al_special_work_conditions__cnt (double precision) | NULL
- al_sport_title (double precision) | NULL
- al_sport_title__cnt (double precision) | NULL
- al_team_leadership (double precision) | NULL
- al_team_leadership__cnt (double precision) | NULL
- al_travel (double precision) | NULL
- al_travel__cnt (double precision) | NULL
- al_troop (double precision) | NULL
- al_troop__cnt (double precision) | NULL
- al_underwater (double precision) | NULL
- al_underwater__cnt (double precision) | NULL
- ap_emergency_standby (double precision) | NULL
- ap_emergency_standby__cnt (double precision) | NULL
- ap_academic_degree (double precision) | NULL
- ap_academic_degree__cnt (double precision) | NULL
- ap_champion_prepare (double precision) | NULL
- ap_champion_prepare__cnt (double precision) | NULL
- ap_check_note_and_works (double precision) | NULL
- ap_check_note_and_works__cnt (double precision) | NULL
- ap_class_group_leadership (double precision) | NULL
- ap_class_group_leadership__cnt (double precision) | NULL
- ap_class_rank (double precision) | NULL
- ap_class_rank__cnt (double precision) | NULL
- ap_class_rank_by_dict (double precision) | NULL
- ap_class_rank_by_dict__cnt (double precision) | NULL
- ap_classroom_management (double precision) | NULL
- ap_classroom_management__cnt (double precision) | NULL
- ap_comb_pos_temp_absent (double precision) | NULL
- ap_comb_pos_temp_absent__cnt (double precision) | NULL
- ap_combining_positions (double precision) | NULL
- ap_combining_positions__cnt (double precision) | NULL
- ap_conducting_extra_sport_activity (double precision) | NULL
- ap_conducting_extra_sport_activity__cnt (double precision) | NULL
- ap_department_management (double precision) | NULL
- ap_department_management__cnt (double precision) | NULL
- ap_edu_process_provision (double precision) | NULL
- ap_edu_process_provision__cnt (double precision) | NULL
- ap_eco_disaster_living (double precision) | NULL
- ap_eco_disaster_living__cnt (double precision) | NULL
- ap_eco_disaster_living_mrp (double precision) | NULL
- ap_eco_disaster_living_mrp__cnt (double precision) | NULL
- ap_fmaamcfmdapupm (double precision) | NULL
- ap_fmaamcfmdapupm__cnt (double precision) | NULL
- ap_hard_danger_work (double precision) | NULL
- ap_hard_danger_work__cnt (double precision) | NULL
- ap_holiday_work (double precision) | NULL
- ap_holiday_work__cnt (double precision) | NULL
- ap_in_depth_teach (double precision) | NULL
- ap_in_depth_teach__cnt (double precision) | NULL
- ap_master_degree_spd (double precision) | NULL
- ap_master_degree_spd__cnt (double precision) | NULL
- ap_medical_care_in_area (double precision) | NULL
- ap_medical_care_in_area__cnt (double precision) | NULL
- ap_mentoring (double precision) | NULL
- ap_mentoring__cnt (double precision) | NULL
- ap_military_rank_salary (double precision) | NULL
- ap_military_rank_salary__cnt (double precision) | NULL
- ap_night_work (double precision) | NULL
- ap_night_work__cnt (double precision) | NULL
- ap_org_ind_training (double precision) | NULL
- ap_org_ind_training__cnt (double precision) | NULL
- ap_overtime_pay (double precision) | NULL
- ap_overtime_pay__cnt (double precision) | NULL
- ap_qualification_category (double precision) | NULL
- ap_qualification_category__cnt (double precision) | NULL
- ap_qualification_level (double precision) | NULL
- ap_qualification_level__cnt (double precision) | NULL
- ap_pprk_1193 (double precision) | NULL
- ap_pprk_1193__cnt (double precision) | NULL
- ap_prof_excellence (double precision) | NULL
- ap_prof_excellence__cnt (double precision) | NULL
- ap_psycho_emo_physical (double precision) | NULL
- ap_psycho_emo_physical__cnt (double precision) | NULL
- ap_rad_risk_living (double precision) | NULL
- ap_rad_risk_living__cnt (double precision) | NULL
- ap_rad_risk_living_mrp (double precision) | NULL
- ap_rad_risk_living_mrp__cnt (double precision) | NULL
- ap_rad_risk_work (double precision) | NULL
- ap_rad_risk_work__cnt (double precision) | NULL
- ap_rad_risk_work_mdi (double precision) | NULL
- ap_rad_risk_work_mdi__cnt (double precision) | NULL
- ap_special_cond_of_serv (double precision) | NULL
- ap_special_cond_of_serv__cnt (double precision) | NULL
- ap_special_title (double precision) | NULL
- ap_special_title__cnt (double precision) | NULL
- ap_special_title_by_dict (double precision) | NULL
- ap_special_title_by_dict__cnt (double precision) | NULL
- ap_special_work_conditions (double precision) | NULL
- ap_special_work_conditions__cnt (double precision) | NULL
- ap_sport_doping_check (double precision) | NULL
- ap_sport_doping_check__cnt (double precision) | NULL
- ap_sport_edu_materials (double precision) | NULL
- ap_sport_edu_materials__cnt (double precision) | NULL
- ap_sport_judge_one_day (double precision) | NULL
- ap_sport_judge_one_day__cnt (double precision) | NULL
- ap_status_main (double precision) | NULL
- ap_status_main__cnt (double precision) | NULL
- ap_status_senior (double precision) | NULL
- ap_status_senior__cnt (double precision) | NULL
- ap_temp_absent_duty (double precision) | NULL
- ap_temp_absent_duty__cnt (double precision) | NULL
- military_rank (double precision) | NULL
- military_rank__cnt (double precision) | NULL
- military_rank_ap_rate (double precision) | NULL
- military_rank_ap_rate__cnt (double precision) | NULL
- military_title (double precision) | NULL
- military_title__cnt (double precision) | NULL
- military_title_ap_rate (double precision) | NULL
- military_title_ap_rate__cnt (double precision) | NULL
- pm_rural (double precision) | NULL
- pm_rural__cnt (double precision) | NULL
- loc__add_payment_total (double precision) | NULL
- loc__allowance_total (double precision) | NULL
- loc__experience_in_years (text) | NULL

---
### Table: stafftab_rep_row
Columns:
- id (bigint) | NOT NULL
- report (bigint) | NOT NULL
- order_number (integer) | NOT NULL
- debug_info (text) | NULL

---
### Table: bip_form_sign
Columns:
- id (bigint) | NOT NULL
- variant (character varying) | NOT NULL
- abp (integer) | NOT NULL
- deleted (boolean) | NOT NULL
- user_id (character varying) | NOT NULL
- sign_date (timestamp without time zone) | NOT NULL
- del_date (timestamp without time zone) | NULL
- del_user_id (character varying) | NULL
- comment (character varying) | NULL
- val1 (double precision) | NULL
- val2 (double precision) | NULL
- val3 (double precision) | NULL
- hash (text) | NOT NULL
- sign (text) | NOT NULL
- cur_year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- region (character varying) | NOT NULL

---
### Table: bip_uebp_sign
Columns:
- id (bigint) | NOT NULL
- variant (character varying) | NOT NULL
- abp (integer) | NOT NULL
- deleted (boolean) | NOT NULL
- user_id (character varying) | NOT NULL
- sign_date (timestamp without time zone) | NOT NULL
- del_date (timestamp without time zone) | NULL
- del_user_id (character varying) | NULL
- comment (character varying) | NULL
- val1 (double precision) | NULL
- val2 (double precision) | NULL
- val3 (double precision) | NULL
- hash (text) | NOT NULL
- sign (text) | NOT NULL
- cur_year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- region (character varying) | NOT NULL

---
### Table: users
Columns:
- id (integer) | NOT NULL
- login (character varying) | NOT NULL
- password (character varying) | NOT NULL
- indicators (jsonb) | NULL
- layoutIndexes (jsonb) | NULL

---
### Table: stafftab_report
Columns:
- id (bigint) | NOT NULL
- report_date (date) | NOT NULL
- creation_moment (timestamp with time zone) | NOT NULL
- form (character varying) | NOT NULL
- debug (boolean) | NOT NULL
- displayed_fields (text) | NOT NULL
- func_group (integer) | NULL
- func_subgroup (integer) | NULL
- budget_program (integer) | NULL
- budget_subprogram (integer) | NULL
- specificity (integer) | NULL
- version (integer) | NULL
- div_by_programs (boolean) | NULL
- source (bigint) | NULL
- subprog_dist (boolean) | NULL
- region (character varying) | NULL
- budget_variant (character varying) | NULL
- save_date_total (timestamp with time zone) | NULL
- st_version (bigint) | NOT NULL

---
### Table: user_modules_link
Columns:
- id (bigint) | NOT NULL
- user_id (character varying) | NOT NULL
- modules (character varying) | NOT NULL
- access_level (integer) | NOT NULL
- operations (ARRAY) | NULL

---
### Table: budget_request_form_gkkp_01_161
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- rent_norm (double precision) | NOT NULL
- daily_avg (integer) | NOT NULL
- rent_avg (integer) | NOT NULL
- people_num (integer) | NOT NULL
- cost_avg (double precision) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: user_msu_link
Columns:
- id (integer) | NOT NULL
- user_id (character varying) | NOT NULL
- msu (character varying) | NOT NULL

---
### Table: stat_setting
Columns:
- id (bigint) | NOT NULL
- create_date (timestamp without time zone) | NULL
- update_date (timestamp without time zone) | NULL
- indicator_id (bigint) | NULL
- unit_id (bigint) | NULL
- filter_text (character varying) | NULL
- link (character varying) | NULL
- stat_periodicity (character varying) | NULL
- stat_unit (character varying) | NULL

---
### Table: user_region_link
Columns:
- id (integer) | NOT NULL
- user_id (character varying) | NOT NULL
- region (character varying) | NOT NULL

---
### Table: stat_setting_link
Columns:
- id (bigint) | NOT NULL
- create_date (timestamp without time zone) | NULL
- filter_text (character varying) | NULL
- link (character varying) | NULL
- stat_periodicity (character varying) | NULL
- stat_unit (character varying) | NULL
- update_date (timestamp without time zone) | NULL
- stat_setting_id (bigint) | NOT NULL
- sm (boolean) | NULL

---
### Table: stat_update_log
Columns:
- id (bigint) | NOT NULL
- stat_setting_link_id (bigint) | NOT NULL
- create_date (timestamp without time zone) | NULL
- status (character varying) | NOT NULL
- text (character varying) | NULL

---
### Table: stafftab_version
Columns:
- id (bigint) | NOT NULL
- org_code (character varying) | NOT NULL
- year (integer) | NOT NULL
- archived (boolean) | NOT NULL
- title (text) | NULL

---
### Table: budget_request_form_714
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- cost_amount (double precision) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: user_roles
Columns:
- id (integer) | NOT NULL
- role_name (character varying) | NULL

---
### Table: budget_request_form_gkkp_01_161_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_01_162
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- code_position (character varying) | NOT NULL
- code_ks (character varying) | NOT NULL
- currency (double precision) | NOT NULL
- compensation (double precision) | NOT NULL
- rent_norm (double precision) | NOT NULL
- daily_avg (integer) | NOT NULL
- rent_avg (integer) | NOT NULL
- persons (integer) | NOT NULL
- cost_avg (double precision) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_gkkp_01_169
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- unit (character varying) | NULL
- amount (integer) | NULL
- cost_avg (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_01_162_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_815_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_714_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_01_169_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_01_339
Columns:
- id (integer) | NOT NULL
- region (character varying) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- total (double precision) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_gkkp_01_339_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_714
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- cost_amount (double precision) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_01_339_regions
Columns:
- id (integer) | NOT NULL
- region (character varying) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- parent_id (integer) | NOT NULL
- count (double precision) | NOT NULL
- price (double precision) | NOT NULL
- total (double precision) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_01_413
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- code_group (character varying) | NOT NULL
- code_model (character varying) | NOT NULL
- amount_standard (integer) | NULL
- balance (integer) | NULL
- rent (integer) | NULL
- year_exit (integer) | NULL
- wear (integer) | NULL
- cost_budget (integer) | NULL
- amount_plan (integer) | NULL
- cost_unit (integer) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_gkkp_714_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_01_416
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- software (character varying) | NOT NULL
- amount (double precision) | NULL
- price (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_gkkp_01_416_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: dict_request_type
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- name_en (character varying) | NULL
- localtext (character varying) | NULL
- beg_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: budget_request_form_429_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL

---
### Table: budget_request_form_417_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- unit (character varying) | NOT NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_417_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- unit (character varying) | NOT NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_417_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_429
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- period (character varying) | NOT NULL
- conclusion (character varying) | NOT NULL
- summa (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_417_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_02_141
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- recipient (character varying) | NULL
- average_meals (integer) | NULL
- func_day (integer) | NULL
- cost_meals (double precision) | NULL
- tobacco (double precision) | NULL
- months (integer) | NULL
- note (character varying) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- category_id (character varying) | NULL
- recipient_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_02_123
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- transport_type (character varying) | NOT NULL
- amount (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- expenses_amount (double precision) | NULL
- note (character varying) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_gkkp_02_142
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- branches (character varying) | NULL
- patients_count (integer) | NULL
- treatment_cost (double precision) | NULL
- average_day (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- branches_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_02_123_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_total_sign
Columns:
- id (bigint) | NOT NULL
- variant (character varying) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NULL
- cur_year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- region (character varying) | NOT NULL
- user_id (character varying) | NOT NULL
- create_date (timestamp without time zone) | NOT NULL
- val0 (double precision) | NULL
- val1 (double precision) | NULL
- val2 (double precision) | NULL
- hash_txt (text) | NOT NULL
- sign_txt (text) | NOT NULL
- deleted (boolean) | NULL
- del_user_id (character varying) | NULL
- del_date (timestamp without time zone) | NULL
- comment_txt (character varying) | NULL

---
### Table: budget_request_form_gkkp_02_141_decode
Columns:
- id (bigint) | NOT NULL
- category_id (character varying) | NOT NULL
- enstru_code (character varying) | NOT NULL
- add_detail (character varying) | NULL
- unit_code (character varying) | NOT NULL
- num_meals (integer) | NOT NULL
- num_day (integer) | NOT NULL
- norm_per (double precision) | NOT NULL
- price_cur (double precision) | NOT NULL
- index_inf (double precision) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- file_hash (character varying) | NULL
- price_indexed (double precision) | NULL

---
### Table: budget_request_form_gkkp_815_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_02_142_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: project_bank_task_results
Columns:
- id (bigint) | NOT NULL
- goal_id (bigint) | NOT NULL
- type (bigint) | NOT NULL
- name_kz (text) | NOT NULL
- name_ru (text) | NOT NULL
- indicator_id (bigint) | NULL
- indicator_ru (text) | NULL
- indicator_kz (text) | NULL
- unit (bigint) | NOT NULL
- created_at (timestamp without time zone) | NULL

---
### Table: dict_position_variants
Columns:
- id (bigint) | NOT NULL
- name_kk (text) | NOT NULL
- name_ru (text) | NOT NULL
- kind (character varying) | NOT NULL
- gov_level (character varying) | NULL
- func_block (character varying) | NULL
- pos_level (integer) | NOT NULL
- region (integer) | NULL
- category_level (integer) | NOT NULL
- category (bigint) | NULL
- category_number (character varying) | NULL
- main (bigint) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL
- cur_year_beg (integer) | NULL
- cur_year_end (integer) | NULL
- closing_year (integer) | NULL

---
### Table: gu_department_position
Columns:
- id (bigint) | NOT NULL
- name_kk (text) | NOT NULL
- name_ru (text) | NOT NULL
- func_block (character varying) | NULL
- pos_level (integer) | NULL
- legal_act_position (bigint) | NULL
- civil_position (bigint) | NULL
- work_position_rank (integer) | NULL
- mvd_position (bigint) | NULL
- legal_act_mvd_position (bigint) | NULL
- version (bigint) | NOT NULL
- edu_position (bigint) | NULL
- legal_act_position_variant (bigint) | NULL

---
### Table: budget_request_form_412_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- unit (character varying) | NOT NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_158
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- category_id (character varying) | NOT NULL
- name_ru (character varying) | NULL
- enstru_code (character varying) | NOT NULL
- add_detail (character varying) | NULL
- amount (numeric) | NOT NULL
- price (numeric) | NOT NULL
- file_hash (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_02_144
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- fuel (character varying) | NOT NULL
- fact_cost (double precision) | NULL
- area (double precision) | NULL
- months (double precision) | NULL
- price (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- enstru_code (character varying) | NULL
- add_detail (character varying) | NULL
- unit_code (character varying) | NULL
- file_hash (character varying) | NULL

---
### Table: budget_request_form_gkkp_02_151
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- watering (character varying) | NOT NULL
- comm_object (character varying) | NOT NULL
- tariff (double precision) | NULL
- power (double precision) | NULL
- rate (double precision) | NULL
- correction_factors (double precision) | NULL
- note (character varying) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- category_id (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_02_151_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: project_bank_task_result_values
Columns:
- id (bigint) | NOT NULL
- result_id (bigint) | NOT NULL
- year (integer) | NOT NULL
- value (numeric) | NOT NULL
- created_at (timestamp without time zone) | NULL

---
### Table: budget_request_form_412_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_412_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_02_149
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- consumable (character varying) | NOT NULL
- amount (numeric) | NULL
- cur_year (integer) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- cost (numeric) | NOT NULL
- enstru_code (character varying) | NULL
- add_detail (character varying) | NULL
- unit_code (character varying) | NULL
- file_hash (character varying) | NULL

---
### Table: budget_request_form_813_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_02_159
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- enstru_code (character varying) | NULL
- add_detail (character varying) | NULL
- file_hash (character varying) | NULL
- amount (numeric) | NULL
- price (numeric) | NULL
- category_id (character varying) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_02_322_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_02_324
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- civil_type (character varying) | NOT NULL
- avg_annual_contingent0 (double precision) | NOT NULL
- amount_months (double precision) | NOT NULL
- state_scholarship (double precision) | NOT NULL
- avg_annual_contingent1 (double precision) | NOT NULL
- percentage_increase1 (double precision) | NOT NULL
- avg_annual_contingent2 (double precision) | NOT NULL
- percentage_increase2 (double precision) | NOT NULL
- avg_annual_contingent3 (double precision) | NOT NULL
- percentage_increase3 (double precision) | NOT NULL
- avg_annual_contingent4 (double precision) | NOT NULL
- size_scholarship (double precision) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_gkkp_02_322
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_02_324_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_02_339
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_165_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_813_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_03_141
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- recipient (character varying) | NULL
- average_meals (integer) | NULL
- func_day (integer) | NULL
- cost_meals (double precision) | NULL
- note (character varying) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- category_id (character varying) | NULL
- recipient_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_02_339_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_02_414
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- code_cabinet (character varying) | NOT NULL
- code_furniture (character varying) | NOT NULL
- standard (integer) | NOT NULL
- amount (integer) | NOT NULL
- made_year (integer) | NOT NULL
- wear (double precision) | NOT NULL
- plan (integer) | NOT NULL
- cost (double precision) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_gkkp_03_141_decode
Columns:
- id (bigint) | NOT NULL
- category_id (character varying) | NOT NULL
- enstru_code (character varying) | NOT NULL
- add_detail (character varying) | NULL
- amount (numeric) | NOT NULL
- price (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- file_hash (character varying) | NULL
- unit_code (character varying) | NULL

---
### Table: budget_request_form_gkkp_02_414_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_fact534a
Columns:
- id (integer) | NOT NULL
- period (date) | NOT NULL
- region_code (character varying) | NOT NULL
- budget_type (character varying) | NOT NULL
- funding_source (character varying) | NOT NULL
- abp_gu (character varying) | NOT NULL
- opening_balance (numeric) | NOT NULL
- debit (numeric) | NOT NULL
- credit (numeric) | NOT NULL
- closing_balance (numeric) | NOT NULL
- update_date (timestamp without time zone) | NULL

---
### Table: budget_fact520_head
Columns:
- id (integer) | NOT NULL
- period (date) | NOT NULL
- region_code (character varying) | NOT NULL
- budget_type (character varying) | NOT NULL
- funding_source (character varying) | NOT NULL
- bik (character varying) | NOT NULL
- iik (character varying) | NOT NULL
- year_beginning_balance (numeric) | NOT NULL
- opening_balance (numeric) | NOT NULL
- closing_balance (numeric) | NOT NULL
- update_date (timestamp without time zone) | NULL

---
### Table: dict_srs_directions
Columns:
- id (integer) | NOT NULL
- direction_code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NOT NULL
- name_en (character varying) | NOT NULL
- sort_order (integer) | NOT NULL
- date_start (timestamp without time zone) | NOT NULL
- date_end (timestamp without time zone) | NULL

---
### Table: dict_srs_ate_types
Columns:
- id (integer) | NOT NULL
- code (character varying) | NULL
- sort_order (integer) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NOT NULL
- name_en (character varying) | NOT NULL
- shortname_ru (character varying) | NULL
- shortname_kz (character varying) | NULL
- shortname_en (character varying) | NULL

---
### Table: srs_report_headers
Columns:
- id (integer) | NOT NULL
- direction_code (character varying) | NOT NULL
- subdirection_code (character varying) | NOT NULL
- indicator_code (character varying) | NOT NULL
- description_ru (text) | NOT NULL
- description_kz (text) | NOT NULL
- description_en (text) | NULL
- num_order (integer) | NULL
- column_range_details (text) | NOT NULL
- indicator_type (character varying) | NULL
- date_start (timestamp without time zone) | NOT NULL
- date_end (timestamp without time zone) | NULL
- unit_code (integer) | NULL

---
### Table: dict_project_bank_unit
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NOT NULL
- code_isgp (character varying) | NOT NULL
- name_kz (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL

---
### Table: budget_separate_specifics
Columns:
- id (integer) | NOT NULL
- spf (integer) | NULL
- dict_indicator_id (bigint) | NOT NULL
- region_id (character varying) | NOT NULL
- status (character varying) | NULL
- input_form_indicator_id (bigint) | NULL
- is_region (boolean) | NOT NULL

---
### Table: dict_product_groups
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: budget_request_form_gkkp_03_151
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- comm_object (character varying) | NOT NULL
- tariff (double precision) | NULL
- power (double precision) | NULL
- rate (double precision) | NULL
- correction_factors (double precision) | NULL
- note (character varying) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- category_id (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_03_151_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_165_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_03_149
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- good_type (character varying) | NOT NULL
- amount (numeric) | NULL
- price (numeric) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- enstru_code (character varying) | NULL
- add_detail (character varying) | NULL
- unit_code (character varying) | NULL
- file_hash (character varying) | NULL

---
### Table: budget_request_form_gkkp_03_159
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- area (double precision) | NULL
- rent (double precision) | NULL
- months (integer) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_03_159_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_04_141
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- recipient (character varying) | NOT NULL
- average_meals (double precision) | NULL
- func_day (integer) | NULL
- correction_factors (double precision) | NULL
- note (character varying) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_gkkp_04_141_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_04_151
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- area (double precision) | NULL
- cost_avg (double precision) | NULL
- season (double precision) | NULL
- correction_factors (double precision) | NULL
- note (character varying) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_gkkp_04_151_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_813_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_165_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_01_414
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- equipment (character varying) | NOT NULL
- amount (numeric) | NULL
- cur_year (integer) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- enstru_code (character varying) | NULL
- add_detail (character varying) | NULL
- unit_code (character varying) | NULL
- file_hash (character varying) | NULL
- cost (numeric) | NULL

---
### Table: budget_request_form_gkkp_133
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_154
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- amount (integer) | NULL
- cost (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_133_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_155
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_163_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_154_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_156
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- amount (integer) | NULL
- cost (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_155_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_157
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- amount (integer) | NULL
- cost (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_156_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_execution_reports_fzp
Columns:
- id (integer) | NOT NULL
- region (character varying) | NOT NULL
- date (date) | NOT NULL
- gr (integer) | NULL
- pgr (integer) | NULL
- abp (character varying) | NULL
- type (integer) | NULL
- count (numeric) | NULL
- tax_soc (numeric) | NULL
- tax_gfcc (numeric) | NULL
- tax_osms (numeric) | NULL
- pension_contrib (numeric) | NULL
- salary (numeric) | NULL
- health (numeric) | NULL
- ecology (numeric) | NULL
- add_vac (numeric) | NULL
- add_health (numeric) | NULL
- add_village (numeric) | NULL
- new (boolean) | NULL
- last_update (timestamp without time zone) | NULL
- user_id (text) | NULL
- rb (boolean) | NULL

---
### Table: budget_request_form_gkkp_163_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_157_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_163_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_212
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_213
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_212_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_213_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_execution_reports_constructor_template
Columns:
- id (bigint) | NOT NULL
- name (character varying) | NOT NULL
- description (text) | NULL
- is_shared (boolean) | NOT NULL
- settings (jsonb) | NOT NULL
- user_id (character varying) | NOT NULL

---
### Table: budget_request_form_01_151_decode
Columns:
- id (integer) | NOT NULL
- category_id (character varying) | NOT NULL
- name_object (character varying) | NULL
- tariff (double precision) | NOT NULL
- power (double precision) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_object_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_311_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_311
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_321
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- total_employees (integer) | NOT NULL
- number_avg (double precision) | NOT NULL
- area (double precision) | NOT NULL
- price (double precision) | NOT NULL
- number_months (double precision) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_322
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- amount_first (integer) | NULL
- number_months (double precision) | NULL
- cost (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_321_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_execution_reports_constructor_journal
Columns:
- id (bigint) | NOT NULL
- name (character varying) | NOT NULL
- description (text) | NULL
- is_shared (boolean) | NOT NULL
- user_id (character varying) | NOT NULL
- settings (jsonb) | NOT NULL
- table_data (text) | NOT NULL
- creation_timestamp (timestamp without time zone) | NOT NULL
- username (character varying) | NOT NULL

---
### Table: user_init_log
Columns:
- id (bigint) | NOT NULL
- user_id (character varying) | NULL
- init_time (timestamp without time zone) | NULL
- host (character varying) | NULL

---
### Table: budget_request_form_gkkp_322_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_02_151_decode
Columns:
- id (integer) | NOT NULL
- category_id (character varying) | NOT NULL
- name_object (character varying) | NULL
- tariff (double precision) | NOT NULL
- power (double precision) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_object_kk (character varying) | NULL

---
### Table: budget_request_form_03_151_decode
Columns:
- id (integer) | NOT NULL
- category_id (character varying) | NOT NULL
- name_object (character varying) | NULL
- tariff (double precision) | NOT NULL
- power (double precision) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_object_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_331
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_331_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_332
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_338
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_332_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_02_169
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- norm (numeric) | NOT NULL
- price (numeric) | NOT NULL
- num_day (numeric) | NOT NULL
- num_per (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_163_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_813_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_01_151_decode
Columns:
- id (integer) | NOT NULL
- category_id (character varying) | NOT NULL
- name_object (character varying) | NULL
- tariff (double precision) | NOT NULL
- power (double precision) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_object_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_338_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_02_151_decode
Columns:
- id (integer) | NOT NULL
- category_id (character varying) | NOT NULL
- name_object (character varying) | NULL
- tariff (double precision) | NOT NULL
- power (double precision) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_object_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_352
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_411
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_352_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_411_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_02_169_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_03_151_decode
Columns:
- id (integer) | NOT NULL
- category_id (character varying) | NOT NULL
- name_object (character varying) | NULL
- tariff (double precision) | NOT NULL
- power (double precision) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_object_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_412_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_412
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- unit (character varying) | NULL
- amount (integer) | NULL
- cost (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_417
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- amount (integer) | NULL
- cost (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_417_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_418
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- unit (character varying) | NULL
- amount (integer) | NULL
- cost (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_02_169
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- norm (numeric) | NOT NULL
- price (numeric) | NOT NULL
- num_day (numeric) | NOT NULL
- num_per (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_418_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_419
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- amount (integer) | NULL
- cost (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_421
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- period (character varying) | NULL
- conclusion (character varying) | NULL
- summa (double precision) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_419_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_423
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- period (character varying) | NULL
- conclusion (character varying) | NULL
- summa (double precision) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_421_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_transfers
Columns:
- id (integer) | NOT NULL
- transfer_group (character varying) | NULL
- expense_code (character varying) | NULL
- direction (integer) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NOT NULL
- region (character varying) | NULL
- year (integer) | NOT NULL
- user_id (character varying) | NOT NULL
- update_date (timestamp without time zone) | NOT NULL
- funding_source (character varying) | NULL
- budget_level (character varying) | NULL

---
### Table: budget_request_form_gkkp_02_169_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_511
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_423_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_513
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_511_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_execution_debit_total
Columns:
- id (bigint) | NOT NULL
- region (character varying) | NOT NULL
- year (bigint) | NOT NULL
- month (bigint) | NOT NULL
- gr (integer) | NULL
- pgr (integer) | NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NULL
- budget_type (character varying) | NULL
- create_date (timestamp with time zone) | NULL
- update_date (date) | NULL
- planfinplat (numeric) | NULL
- planfinobaz (numeric) | NULL
- plat (numeric) | NULL
- obaz (numeric) | NULL
- plan_cost (numeric) | NULL
- oplobaz (numeric) | NULL
- prinobaz (numeric) | NULL
- payments_id (bigint) | NULL
- obligations_id (bigint) | NULL
- form420_id (bigint) | NULL
- status (integer) | NULL
- neoplobaz (numeric) | NULL
- oplobaz_mes (numeric) | NULL

---
### Table: budget_request_form_gkkp_514_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_514
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_612
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_612_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_711
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_711_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_712
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_gkkp_gchp
Columns:
- id (integer) | NOT NULL
- region (character varying) | NOT NULL
- form (character varying) | NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- name_ru (character varying) | NULL
- cost_amount (double precision) | NOT NULL
- cur_year (integer) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_712_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- file_blob (bytea) | NULL
- file_name (character varying) | NULL
- cur_year (integer) | NOT NULL
- file_type (character varying) | NULL
- change_time (date) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL

---
### Table: budget_execution_income_total
Columns:
- id (bigint) | NOT NULL
- region (character varying) | NOT NULL
- year (bigint) | NOT NULL
- month (bigint) | NOT NULL
- kat (integer) | NOT NULL
- cls (integer) | NOT NULL
- pcl (integer) | NOT NULL
- spf (integer) | NOT NULL
- create_date (timestamp without time zone) | NULL
- update_date (date) | NULL
- finplan (numeric) | NULL
- factpost (numeric) | NULL
- income_id (integer) | NULL
- form211_id (bigint) | NULL
- budget_type (character varying) | NULL
- status (integer) | NULL

---
### Table: budget_request_form_gkkp_163_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_gkkp_gchp_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: dict_ebk_func_attr_import
Columns:
- id (bigint) | NOT NULL
- source_id (bigint) | NULL
- fgr (character varying) | NULL
- pgr (character varying) | NULL
- abp (character varying) | NULL
- prg (character varying) | NULL
- ppr (character varying) | NULL
- code_type (character varying) | NULL
- budget_level_code (character varying) | NULL
- budget_level (character varying) | NULL
- accepted_code (character varying) | NULL
- accepted (character varying) | NULL
- method_of_impl_code (character varying) | NULL
- method_of_impl (character varying) | NULL
- financial_assets_code (character varying) | NULL
- financial_assets (character varying) | NULL
- government_level_code (character varying) | NULL
- government_level (character varying) | NULL
- granted_code (character varying) | NULL
- granted (character varying) | NULL
- budget_investment_projects_code (character varying) | NULL
- budget_investment_projects (character varying) | NULL
- investment_programs_code (character varying) | NULL
- investment_programs (character varying) | NULL
- suspended_code (character varying) | NULL
- suspended (character varying) | NULL
- program_content_code (character varying) | NULL
- program_content (character varying) | NULL
- consumption_type_code (character varying) | NULL
- consumption_type (character varying) | NULL
- privacy_level_coed (character varying) | NULL
- privacy_level (character varying) | NULL
- development_type_code (character varying) | NULL
- development_type (character varying) | NULL
- transfers_code (character varying) | NULL
- transfers (character varying) | NULL

---
### Table: stafftab_report_total_kgkp_link
Columns:
- id (bigint) | NOT NULL
- total (integer) | NOT NULL
- report (bigint) | NOT NULL
- send_moment (timestamp with time zone) | NOT NULL
- keycloak_user_id (character varying) | NULL

---
### Table: dict_st_edu_org_type
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NOT NULL
- name_en (text) | NOT NULL
- name_kk (text) | NOT NULL
- name_ru (text) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: budget_request_form_gkkp_411_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_158
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- category_id (character varying) | NOT NULL
- name_ru (character varying) | NULL
- enstru_code (character varying) | NOT NULL
- add_detail (character varying) | NULL
- amount (numeric) | NOT NULL
- price (numeric) | NOT NULL
- file_hash (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- name_kk (character varying) | NULL

---
### Table: appendix_10
Columns:
- id (integer) | NOT NULL
- code (character varying) | NULL
- year (integer) | NULL
- cur_year (integer) | NULL
- balance_initial_cost (double precision) | NULL
- receipt_amount (double precision) | NULL
- disposal_amount (double precision) | NULL
- accumulated_deprication (double precision) | NULL
- id_budget_version (character varying) | NULL
- abp (integer) | NULL
- balance_end (double precision) | NULL
- accumulated_end (double precision) | NULL

---
### Table: dict_st_edu_hours
Columns:
- id (bigint) | NOT NULL
- org_type (bigint) | NOT NULL
- name_en (text) | NOT NULL
- name_kk (text) | NOT NULL
- name_ru (text) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL
- value (double precision) | NOT NULL
- unit_en (text) | NOT NULL
- unit_kk (text) | NOT NULL
- unit_ru (text) | NOT NULL
- code (character varying) | NOT NULL
- order_number (integer) | NULL

---
### Table: dict_st_ead
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NOT NULL
- attr_type (character varying) | NOT NULL
- kind (character varying) | NOT NULL
- name_kk (text) | NOT NULL
- name_ru (text) | NOT NULL
- subtitle_kk (text) | NULL
- subtitle_ru (text) | NULL
- dict_norm_ind_code (character varying) | NULL
- pre_multiplier (double precision) | NULL
- value_column_title_template (text) | NULL
- value_column_title_multiplier (double precision) | NULL
- allow_budget_prog_select (boolean) | NOT NULL
- allow_fact_workload_calc (boolean) | NOT NULL
- allow_period (boolean) | NOT NULL
- code_parent (character varying) | NULL

---
### Table: dict_edu_position
Columns:
- id (bigint) | NOT NULL
- func_block (character varying) | NOT NULL
- level (bigint) | NULL
- level_number (integer) | NULL
- name_en (text) | NOT NULL
- name_kk (text) | NOT NULL
- name_ru (text) | NOT NULL
- pos_level (integer) | NULL

---
### Table: stafftab_edu_wl
Columns:
- id (bigint) | NOT NULL
- emp (bigint) | NOT NULL
- conf (bigint) | NOT NULL
- value (double precision) | NOT NULL

---
### Table: stafftab_edu_wl_c
Columns:
- id (bigint) | NOT NULL
- hours (bigint) | NOT NULL
- version (bigint) | NOT NULL

---
### Table: dict_education_level
Columns:
- id (bigint) | NOT NULL
- parent_id (bigint) | NULL
- code (character varying) | NOT NULL
- name_ru (text) | NOT NULL
- name_kk (text) | NOT NULL
- short_name_ru (text) | NULL
- short_name_kk (text) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_st_edu_subject
Columns:
- id (bigint) | NOT NULL
- parent_id (bigint) | NULL
- code (character varying) | NOT NULL
- name_ru (text) | NOT NULL
- name_kk (text) | NOT NULL
- short_name_ru (text) | NULL
- short_name_kk (text) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL
- region_code (character varying) | NULL
- kind (character varying) | NULL
- org_type_code (ARRAY) | NULL
- kind_name_ru (text) | NOT NULL
- kind_name_kk (text) | NOT NULL

---
### Table: dict_bc_project
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NOT NULL
- region_code (character varying) | NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NOT NULL
- beg_date (date) | NOT NULL
- end_date (date) | NULL
- user_name (character varying) | NOT NULL
- update_date (timestamp without time zone) | NOT NULL

---
### Table: user_workplace_kgkp_link
Columns:
- id (integer) | NOT NULL
- user_id (character varying) | NOT NULL
- workplace (character varying) | NOT NULL

---
### Table: dict_bc_goal
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NOT NULL
- beg_date (date) | NOT NULL
- end_date (date) | NULL
- user_name (character varying) | NULL
- update_date (timestamp without time zone) | NULL

---
### Table: dict_bc_section
Columns:
- id (bigint) | NOT NULL
- section (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NOT NULL
- beg_date (date) | NOT NULL
- end_date (date) | NULL
- user_name (character varying) | NULL
- update_date (timestamp without time zone) | NULL
- code (character varying) | NULL
- budget_level_id (integer) | NULL

---
### Table: dict_bc_status
Columns:
- id (bigint) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NOT NULL
- beg_date (date) | NOT NULL
- end_date (date) | NULL
- user_name (character varying) | NULL
- update_date (timestamp without time zone) | NULL

---
### Table: dict_bc_type_loan
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NOT NULL
- beg_date (date) | NOT NULL
- end_date (date) | NULL
- user_name (character varying) | NULL
- update_date (timestamp without time zone) | NULL

---
### Table: budget_request_form_814_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: dict_upload_status
Columns:
- id (integer) | NOT NULL
- code (integer) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_bc_contractor
Columns:
- id (bigint) | NOT NULL
- bin (character varying) | NOT NULL
- obl (character varying) | NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NOT NULL
- beg_date (date) | NOT NULL
- end_date (date) | NULL
- user_name (character varying) | NULL
- update_date (timestamp without time zone) | NULL
- code (character varying) | NULL

---
### Table: budget_bc_payment_schedule
Columns:
- id (bigint) | NOT NULL
- id_contract (bigint) | NOT NULL
- date_payment (date) | NOT NULL
- sum_payment (double precision) | NULL
- date_beg (date) | NULL
- date_end (date) | NULL
- sum_base (double precision) | NULL
- user_name (character varying) | NULL
- update_date (timestamp without time zone) | NULL
- type_schedule (integer) | NOT NULL
- day_count (integer) | NULL

---
### Table: budget_bc_payment_schedule_fact
Columns:
- id (bigint) | NOT NULL
- id_contract (bigint) | NOT NULL
- type_schedule (smallint) | NOT NULL
- sum_payment_fact (double precision) | NULL
- date_fact (date) | NOT NULL
- code (character varying) | NOT NULL
- user_name (character varying) | NULL
- update_date (timestamp without time zone) | NULL
- note (text) | NULL

---
### Table: budget_bc_file_storage
Columns:
- id (bigint) | NOT NULL
- file_name (character varying) | NOT NULL
- description (character varying) | NULL
- agreement_id (bigint) | NOT NULL

---
### Table: budget_bc_agreement_registration
Columns:
- id (bigint) | NOT NULL
- type (integer) | NOT NULL
- budget_level (integer) | NOT NULL
- region_code (character varying) | NULL
- number_contract (character varying) | NOT NULL
- number_contract_main (bigint) | NULL
- date_contract (date) | NOT NULL
- note_ru (character varying) | NULL
- note_kz (character varying) | NULL
- loan_direction (integer) | NOT NULL
- budget_loan_purpose (character varying) | NOT NULL
- code_project (character varying) | NOT NULL
- creditor (character varying) | NOT NULL
- code_gu (character varying) | NOT NULL
- contractor (character varying) | NOT NULL
- amount (double precision) | NOT NULL
- code_currency (character varying) | NOT NULL
- currency_rate (double precision) | NULL
- rate (double precision) | NOT NULL
- contract_years (smallint) | NOT NULL
- benefit_months (smallint) | NOT NULL
- beg_date (date) | NOT NULL
- end_date (date) | NOT NULL
- penalty (double precision) | NOT NULL
- file (character varying) | NULL
- status_id (bigint) | NOT NULL
- code_prog (character varying) | NULL
- frequency (character varying) | NULL
- user_name (character varying) | NULL
- update_date (timestamp without time zone) | NULL
- frequency_rate (character varying) | NULL
- flag_actual (integer) | NOT NULL
- type_loan (character varying) | NOT NULL
- contract_date_end (date) | NOT NULL
- prg (character varying) | NULL
- frequency_income (character varying) | NULL
- ppr (character varying) | NULL
- flag_error (smallint) | NULL
- left_amount (double precision) | NULL
- initial_interest_repayment_date (date) | NULL
- following_interest_repayment_month (smallint) | NULL
- following_interest_repayment_day (smallint) | NULL
- direct_result (text) | NULL
- final_result (text) | NULL

---
### Table: budget_request_form_gkkp_paid_03_149
Columns:
- id (integer) | NULL
- form (character varying) | NULL
- data_type (character varying) | NULL
- gr (integer) | NULL
- abp (integer) | NULL
- bin (character varying) | NULL
- prg (integer) | NULL
- ppr (integer) | NULL
- spf (integer) | NULL
- year (integer) | NULL
- cur_year (integer) | NULL
- good_type (character varying) | NULL
- amount (numeric) | NULL
- price (numeric) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- enstru_code (character varying) | NULL
- add_detail (character varying) | NULL
- unit_code (character varying) | NULL
- file_hash (character varying) | NULL

---
### Table: budget_request_form_01_142_decode
Columns:
- id (bigint) | NOT NULL
- category_id (character varying) | NOT NULL
- enstru_code (character varying) | NOT NULL
- add_detail (character varying) | NULL
- amount (numeric) | NOT NULL
- price (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- file_hash (character varying) | NULL
- unit_code (character varying) | NULL

---
### Table: budget_request_form_gkkp_814_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: dict_api_service_type
Columns:
- id (bigint) | NOT NULL
- type_params_service (integer) | NOT NULL
- type_service (integer) | NOT NULL
- name_type (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_01_143
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- recipient (character varying) | NULL
- average (numeric) | NULL
- rate (numeric) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- enstru_code (character varying) | NULL
- add_detail (character varying) | NULL
- unit_code (character varying) | NULL
- file_hash (character varying) | NULL
- category_id (character varying) | NULL
- recipient_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_paid_files
Columns:
- id (integer) | NULL
- form (character varying) | NULL
- year (integer) | NULL
- data_type (character varying) | NULL
- gr (integer) | NULL
- abp (integer) | NULL
- bin (character varying) | NULL
- prg (integer) | NULL
- ppr (integer) | NULL
- spf (integer) | NULL
- file_blob (bytea) | NULL
- file_name (character varying) | NULL
- cur_year (integer) | NULL
- file_type (character varying) | NULL
- change_time (date) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL

---
### Table: budget_request_form_gkkp_paid_04_151
Columns:
- id (integer) | NULL
- form (character varying) | NULL
- data_type (character varying) | NULL
- gr (integer) | NULL
- abp (integer) | NULL
- bin (character varying) | NULL
- prg (integer) | NULL
- ppr (integer) | NULL
- spf (integer) | NULL
- year (integer) | NULL
- cur_year (integer) | NULL
- area (double precision) | NULL
- cost_avg (double precision) | NULL
- season (double precision) | NULL
- correction_factors (double precision) | NULL
- note (character varying) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_execution_alteration_history
Columns:
- id (bigint) | NOT NULL
- budget_execution_alteration_uf_request_id (bigint) | NOT NULL
- region (character varying) | NOT NULL
- year (integer) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- month (integer) | NOT NULL
- value (numeric) | NOT NULL
- plan_type (smallint) | NOT NULL
- update_date (timestamp without time zone) | NOT NULL
- gr (integer) | NOT NULL
- budget_execution_alteration_abp_request_id (bigint) | NULL

---
### Table: dict_summary_report_forms
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- ord (integer) | NOT NULL
- is_abp (boolean) | NOT NULL
- spf (integer) | NULL
- link (character varying) | NULL
- type_form (smallint) | NOT NULL
- is_gu (boolean) | NOT NULL
- is_add (boolean) | NOT NULL
- form_level (integer) | NOT NULL
- code_module (character varying) | NULL
- dict_api_service_type (bigint) | NULL
- is_aggregate (boolean) | NULL

---
### Table: dict_api_service_type_params
Columns:
- id (bigint) | NOT NULL
- prefix (character varying) | NULL
- type_params (bigint) | NOT NULL
- name_params (character varying) | NOT NULL
- suffix (character varying) | NULL
- is_list (boolean) | NOT NULL
- def_value (character varying) | NULL
- dict_api_service_type (bigint) | NOT NULL
- with_comma (boolean) | NOT NULL
- ord (integer) | NOT NULL

---
### Table: budget_request_form_165
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- name_ru (character varying) | NULL
- unit (character varying) | NOT NULL
- amount (integer) | NOT NULL
- price (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_165
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- name_ru (character varying) | NULL
- unit (character varying) | NOT NULL
- amount (integer) | NOT NULL
- price (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_165_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_gkkp_paid_04_151_files
Columns:
- id (integer) | NULL
- form (character varying) | NULL
- data_type (character varying) | NULL
- gr (integer) | NULL
- bin (character varying) | NULL
- abp (integer) | NULL
- prg (integer) | NULL
- ppr (integer) | NULL
- spf (integer) | NULL
- year (integer) | NULL
- cur_year (integer) | NULL
- user_name (character varying) | NULL
- update_data (timestamp without time zone) | NULL
- file_type (character varying) | NULL
- file_id (integer) | NULL
- row_id (integer) | NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_165_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_paid_02_159
Columns:
- id (integer) | NULL
- form (character varying) | NULL
- data_type (character varying) | NULL
- gr (integer) | NULL
- bin (character varying) | NULL
- abp (integer) | NULL
- prg (integer) | NULL
- ppr (integer) | NULL
- spf (integer) | NULL
- year (integer) | NULL
- cur_year (integer) | NULL
- name_ru (character varying) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- enstru_code (character varying) | NULL
- add_detail (character varying) | NULL
- file_hash (character varying) | NULL
- amount (numeric) | NULL
- price (numeric) | NULL
- category_id (character varying) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_fact520_data
Columns:
- id (integer) | NOT NULL
- budget_fact520_head_id (integer) | NOT NULL
- transact_nom (character varying) | NOT NULL
- bik (character varying) | NOT NULL
- iik (character varying) | NOT NULL
- debit (numeric) | NOT NULL
- credit (numeric) | NOT NULL
- update_date (timestamp without time zone) | NULL

---
### Table: budget_request_form_gkkp_03_142
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- visits_count (integer) | NULL
- cost_visits (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_gkkp_03_142_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_paid_01_169
Columns:
- id (integer) | NULL
- form (character varying) | NULL
- data_type (character varying) | NULL
- gr (integer) | NULL
- bin (character varying) | NULL
- abp (integer) | NULL
- prg (integer) | NULL
- ppr (integer) | NULL
- spf (integer) | NULL
- year (integer) | NULL
- cur_year (integer) | NULL
- name_ru (character varying) | NULL
- unit (character varying) | NULL
- amount (integer) | NULL
- cost_avg (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_paid_01_169_files
Columns:
- id (integer) | NULL
- form (character varying) | NULL
- data_type (character varying) | NULL
- gr (integer) | NULL
- bin (character varying) | NULL
- abp (integer) | NULL
- prg (integer) | NULL
- ppr (integer) | NULL
- spf (integer) | NULL
- year (integer) | NULL
- cur_year (integer) | NULL
- user_name (character varying) | NULL
- update_data (timestamp without time zone) | NULL
- file_type (character varying) | NULL
- file_id (integer) | NULL
- row_id (integer) | NULL
- variant (character varying) | NULL

---
### Table: budget_request_form_gkkp_paid_418
Columns:
- id (integer) | NULL
- form (character varying) | NULL
- data_type (character varying) | NULL
- gr (integer) | NULL
- bin (character varying) | NULL
- abp (integer) | NULL
- prg (integer) | NULL
- ppr (integer) | NULL
- spf (integer) | NULL
- year (integer) | NULL
- cur_year (integer) | NULL
- name_ru (character varying) | NULL
- unit (character varying) | NULL
- amount (integer) | NULL
- cost (double precision) | NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- name_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_paid_418_files
Columns:
- id (integer) | NULL
- form (character varying) | NULL
- data_type (character varying) | NULL
- gr (integer) | NULL
- bin (character varying) | NULL
- abp (integer) | NULL
- prg (integer) | NULL
- ppr (integer) | NULL
- spf (integer) | NULL
- year (integer) | NULL
- cur_year (integer) | NULL
- user_name (character varying) | NULL
- update_data (timestamp without time zone) | NULL
- file_type (character varying) | NULL
- file_id (integer) | NULL
- row_id (integer) | NULL
- variant (character varying) | NULL

---
### Table: dict_top_description_template
Columns:
- id (integer) | NOT NULL
- content_ru (ARRAY) | NOT NULL
- content_en (ARRAY) | NOT NULL
- content_kk (ARRAY) | NOT NULL
- start_base_year (integer) | NULL
- end_base_year (integer) | NULL

---
### Table: kfo_5_fintbl10
Columns:
- id (integer) | NOT NULL
- abp (integer) | NULL
- dateinfo (date) | NULL
- gucode (character varying) | NULL
- templ (character varying) | NULL
- sum (numeric) | NULL
- land (numeric) | NULL
- building (numeric) | NULL
- others (numeric) | NULL

---
### Table: kfo_5_fintbl9
Columns:
- id (integer) | NOT NULL
- abp (integer) | NULL
- dateinfo (date) | NULL
- gucode (character varying) | NULL
- templ (character varying) | NULL
- sum (numeric) | NULL
- inventar (numeric) | NULL
- land (numeric) | NULL
- oboryd (numeric) | NULL
- peredat (numeric) | NULL
- prochee (numeric) | NULL
- building (numeric) | NULL
- construction (numeric) | NULL
- transport (numeric) | NULL

---
### Table: kfo_5_fintbl11
Columns:
- id (integer) | NOT NULL
- abp (integer) | NULL
- dateinfo (date) | NULL
- gucode (character varying) | NULL
- templ (character varying) | NULL
- sum (numeric) | NULL
- tree (numeric) | NULL
- animal (numeric) | NULL

---
### Table: budget_request_form_812_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_execution_reports_meetings
Columns:
- id (integer) | NOT NULL
- region (character varying) | NOT NULL
- date (date) | NOT NULL
- gatherings (integer) | NULL
- meetings (integer) | NULL
- participants (integer) | NULL
- members (integer) | NULL

---
### Table: budget_request_form_01_144_sm
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- gsm (character varying) | NOT NULL
- enstru_code (character varying) | NOT NULL
- add_detail (character varying) | NULL
- unit_code (character varying) | NOT NULL
- amount (numeric) | NOT NULL
- price (numeric) | NOT NULL
- file_hash (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_01_144_sm
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- gsm (character varying) | NOT NULL
- enstru_code (character varying) | NOT NULL
- add_detail (character varying) | NULL
- unit_code (character varying) | NOT NULL
- amount (numeric) | NOT NULL
- price (numeric) | NOT NULL
- file_hash (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: faq
Columns:
- id (bigint) | NOT NULL
- question_ru (character varying) | NOT NULL
- question_kz (character varying) | NOT NULL
- answer_ru (character varying) | NOT NULL
- answer_kz (character varying) | NOT NULL
- is_top_question (boolean) | NOT NULL
- video_link_ru (character varying) | NOT NULL
- video_link_kz (character varying) | NOT NULL
- module_id (bigint) | NULL

---
### Table: sic_faq
Columns:
- id (bigint) | NOT NULL
- question_ru (character varying) | NOT NULL
- question_kz (character varying) | NOT NULL
- answer_ru (character varying) | NOT NULL
- answer_kz (character varying) | NOT NULL
- is_top_question (boolean) | NOT NULL
- video_link_ru (character varying) | NOT NULL
- video_link_kz (character varying) | NOT NULL
- module_id (bigint) | NULL

---
### Table: budget_execution_reports_count_and_withdrawals
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- date (date) | NOT NULL
- count (integer) | NULL
- withdrawals (numeric) | NULL
- transers_tek (numeric) | NULL

---
### Table: notify_user_status_history
Columns:
- id (bigint) | NOT NULL
- status (integer) | NOT NULL
- notify_user_id (bigint) | NOT NULL
- dt_change (timestamp without time zone) | NOT NULL

---
### Table: keycloak_user
Columns:
- id (character varying) | NOT NULL
- createdtimestamp (character varying) | NULL
- username (character varying) | NULL
- enabled (boolean) | NULL
- firstname (character varying) | NULL
- lastname (character varying) | NULL
- email (character varying) | NULL

---
### Table: notify_user
Columns:
- id (bigint) | NOT NULL
- user_id_src (character varying) | NULL
- dict_notify_theme_id (integer) | NOT NULL
- user_id_dest (character varying) | NOT NULL
- create_date (timestamp without time zone) | NOT NULL
- end_date (date) | NULL
- msg (character varying) | NOT NULL
- link (character varying) | NULL
- status (integer) | NOT NULL
- is_auto_created (boolean) | NULL
- group_id (bigint) | NOT NULL
- sic_modules (character varying) | NULL
- msg_kk (character varying) | NULL

---
### Table: budget_request_form_gkkp_812_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_812_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: kfo_5_fintbl12
Columns:
- id (integer) | NOT NULL
- abp (integer) | NULL
- dateinfo (date) | NULL
- gucode (character varying) | NULL
- templ (character varying) | NULL
- sum (numeric) | NULL
- license (numeric) | NULL
- patent (numeric) | NULL
- po (numeric) | NULL
- author (numeric) | NULL
- prochee (numeric) | NULL

---
### Table: budget_request_form_814_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: stafftab_general_setting_log
Columns:
- id (integer) | NOT NULL
- setting_type (character varying) | NOT NULL
- stafftab_version (bigint) | NOT NULL
- action_type (character varying) | NOT NULL
- create_date (timestamp without time zone) | NOT NULL
- user_id (character varying) | NOT NULL
- change_details (character varying) | NOT NULL

---
### Table: user_settings
Columns:
- id (bigint) | NOT NULL
- user_id (character varying) | NOT NULL
- type_settings (integer) | NOT NULL
- val_string (character varying) | NULL
- val_int (integer) | NULL
- val_boolean (boolean) | NULL

---
### Table: budget_request_form_gkkp_165_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: dict_notify_theme
Columns:
- id (integer) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- name_en (character varying) | NULL

---
### Table: budget_request_form_gkkp_812_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: stafftab_report_2
Columns:
- id (bigint) | NOT NULL
- version (bigint) | NOT NULL
- budget_variant (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- specificity (integer) | NOT NULL
- form (character varying) | NOT NULL
- func_group (integer) | NOT NULL
- func_subgroup (integer) | NOT NULL
- abp (integer) | NOT NULL
- budget_program (integer) | NOT NULL
- detailed_report (boolean) | NOT NULL
- budget_subprogram (integer) | NULL
- region (character varying) | NOT NULL
- creation_moment (timestamp without time zone) | NOT NULL
- y1_budget_subprograms (ARRAY) | NOT NULL
- y1_invalid (boolean) | NOT NULL
- y2_budget_subprograms (ARRAY) | NOT NULL
- y2_invalid (boolean) | NOT NULL
- y3_budget_subprograms (ARRAY) | NOT NULL
- y3_invalid (boolean) | NOT NULL
- submission_date_to_total (timestamp without time zone) | NULL
- y1_budget_subprograms_exist (boolean) | NULL
- y2_budget_subprograms_exist (boolean) | NULL
- y3_budget_subprograms_exist (boolean) | NULL
- report_type (character varying) | NOT NULL

---
### Table: budget_cost_correct
Columns:
- id (integer) | NOT NULL
- region (integer) | NOT NULL
- gr (integer) | NOT NULL
- pgr (integer) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- field (character varying) | NOT NULL
- value (double precision) | NOT NULL
- year (integer) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- is_correct_counted (boolean) | NULL
- note (character varying) | NULL
- spf (integer) | NULL
- bip_code (character varying) | NULL
- cur_year (integer) | NULL

---
### Table: stafftab_rep_gen_task
Columns:
- id (bigint) | NOT NULL
- version (bigint) | NOT NULL
- budget_variant (character varying) | NOT NULL
- status (character varying) | NOT NULL
- progress (double precision) | NULL
- budget_programs (ARRAY) | NULL
- specificity (integer) | NULL
- try_number (integer) | NOT NULL
- task_message (jsonb) | NULL

---
### Table: stafftab_report_total_link_2
Columns:
- id (bigint) | NOT NULL
- total (integer) | NOT NULL
- report (bigint) | NOT NULL
- send_moment (timestamp with time zone) | NOT NULL
- keycloak_user_id (character varying) | NULL

---
### Table: budget_request_form_total_gkkp_agreement
Columns:
- id (bigint) | NOT NULL
- variant (character varying) | NOT NULL
- region (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- cur_year (integer) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- bin (character varying) | NULL
- status (integer) | NOT NULL
- user_id (character varying) | NULL
- update_date (timestamp without time zone) | NOT NULL
- comment_txt (character varying) | NULL

---
### Table: budget_request_form_total_gkkp_agreement_hist
Columns:
- id (bigint) | NOT NULL
- brfta_id (bigint) | NOT NULL
- status (integer) | NOT NULL
- comment_txt (character varying) | NULL
- update_date (timestamp without time zone) | NOT NULL
- user_id (character varying) | NULL

---
### Table: dict_st_ead_parent
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NOT NULL
- kind (character varying) | NOT NULL
- name_kk (text) | NOT NULL
- name_ru (text) | NOT NULL
- name_en (text) | NOT NULL

---
### Table: program_passport_npa
Columns:
- id (bigint) | NOT NULL
- program_passport_id (bigint) | NOT NULL
- dict_npa_id (bigint) | NOT NULL
- variant (character varying) | NULL

---
### Table: program_passport_goal
Columns:
- id (bigint) | NOT NULL
- program_passport_id (bigint) | NOT NULL
- dict_program_goal_id (bigint) | NOT NULL
- variant (character varying) | NULL

---
### Table: stafftab_report_total_kgkp_link_2
Columns:
- id (bigint) | NOT NULL
- total (integer) | NOT NULL
- report (bigint) | NOT NULL
- send_moment (timestamp with time zone) | NOT NULL
- keycloak_user_id (character varying) | NULL

---
### Table: budget_request_form_gkkp_814_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_154_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- summa (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: server_properties
Columns:
- id (integer) | NOT NULL
- property (character varying) | NOT NULL
- value (text) | NOT NULL
- update_date (timestamp without time zone) | NOT NULL

---
### Table: design_estimate_doc
Columns:
- id (integer) | NOT NULL
- report_number (character varying) | NOT NULL
- project (text) | NOT NULL
- report_date (date) | NOT NULL
- object_place (character varying) | NOT NULL
- customer (character varying) | NOT NULL
- planner (text) | NOT NULL
- timelimit (character varying) | NULL
- status (character varying) | NULL
- comment (text) | NULL
- url (character varying) | NULL
- object_category (text) | NULL
- input_report (text) | NULL
- contract_number (text) | NULL
- contract_amount (numeric) | NULL
- amount_plan (numeric) | NULL
- funding_source (text) | NULL
- customer_bin (numeric) | NULL
- planner_bin (numeric) | NULL
- expertise_place (text) | NULL
- expertise_bin (character varying) | NULL
- kato_object (character varying) | NULL
- input_report_file (bytea) | NULL
- project_code (text) | NULL

---
### Table: dict_budget_regions_declined
Columns:
- id (integer) | NOT NULL
- code (character varying) | NULL
- name_ru (character varying) | NULL
- name_ru_declined (character varying) | NULL
- name_kk (character varying) | NULL
- name_kk_declined (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: budget_request_note_status
Columns:
- id (bigint) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- gu (character varying) | NOT NULL
- data_type (smallint) | NOT NULL
- year (smallint) | NULL
- cur_year (smallint) | NOT NULL
- region (character varying) | NULL
- variant (character varying) | NULL
- user_id (character varying) | NULL
- status (smallint) | NOT NULL
- updated_at (timestamp with time zone) | NOT NULL
- gkkp (character varying) | NULL

---
### Table: dict_mvd_pos_level_salary
Columns:
- id (integer) | NOT NULL
- level (integer) | NOT NULL
- experience_min (integer) | NOT NULL
- experience_max (integer) | NOT NULL
- salary (double precision) | NOT NULL
- beg_date (date) | NOT NULL
- end_date (date) | NULL
- cur_year (integer) | NULL

---
### Table: budget_request_form_01_324_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_01_324
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- scholar_type (character varying) | NOT NULL
- avg_annual (numeric) | NOT NULL
- amount_months (numeric) | NOT NULL
- salary (numeric) | NOT NULL
- surcharge (numeric) | NOT NULL
- variant (character varying) | NULL
- region_code (character varying) | NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL

---
### Table: budget_request_form_gkkp_01_324_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_gkkp_154_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- bin (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- summa (numeric) | NOT NULL
- justif_ru (character varying) | NULL
- justif_kk (character varying) | NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_request_form_154_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_154_v2_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL

---
### Table: budget_cost_data_sign
Columns:
- id (bigint) | NOT NULL
- variant (character varying) | NOT NULL
- abp (integer) | NOT NULL
- deleted (boolean) | NOT NULL
- user_id (character varying) | NOT NULL
- sign_date (timestamp without time zone) | NOT NULL
- del_date (timestamp without time zone) | NULL
- del_user_id (character varying) | NULL
- comment (character varying) | NULL
- val1 (double precision) | NULL
- val2 (double precision) | NULL
- val3 (double precision) | NULL
- hash (text) | NOT NULL
- sign (text) | NOT NULL
- cur_year (integer) | NOT NULL
- data_type (character varying) | NOT NULL
- region (character varying) | NOT NULL

---
### Table: dict_project_branch
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NOT NULL
- beg_date (date) | NOT NULL
- end_date (date) | NOT NULL

---
### Table: dict_funding_source
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NOT NULL
- beg_date (date) | NOT NULL
- end_date (date) | NOT NULL

---
### Table: reports_constructor_journal
Columns:
- id (bigint) | NOT NULL
- name (character varying) | NOT NULL
- file (bytea) | NULL
- filter_settings (jsonb) | NOT NULL
- user_id (character varying) | NOT NULL
- creation_timestamp (timestamp without time zone) | NOT NULL
- progress (smallint) | NOT NULL

---
### Table: stafftab_setting
Columns:
- code (character varying) | NOT NULL
- value_text (text) | NULL

---
### Table: dict_memorial_operations
Columns:
- id (integer) | NOT NULL
- order_no (integer) | NULL
- operation_code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NOT NULL
- name_en (character varying) | NOT NULL
- debit_subaccount (character varying) | NULL
- credit_subaccount (character varying) | NULL
- is_active (boolean) | NOT NULL
- beg_date (date) | NOT NULL
- end_date (date) | NULL
- created_at (timestamp without time zone) | NOT NULL
- updated_at (timestamp without time zone) | NOT NULL

---
### Table: budget_execution_forms_status
Columns:
- id (bigint) | NOT NULL
- budget_execution_forms_id (bigint) | NOT NULL
- user_id (character varying) | NOT NULL
- description (text) | NULL
- create_date (timestamp without time zone) | NOT NULL
- status (integer) | NOT NULL

---
### Table: budget_execution_forms_status_hist
Columns:
- id (bigint) | NOT NULL
- budget_execution_forms_id (bigint) | NOT NULL
- user_id (character varying) | NOT NULL
- description (text) | NULL
- create_date (timestamp without time zone) | NOT NULL
- status (integer) | NOT NULL

---
### Table: project_bank_plan_values
Columns:
- id (bigint) | NOT NULL
- project_id (bigint) | NOT NULL
- year (integer) | NOT NULL
- value (numeric) | NOT NULL
- user_id (character varying) | NOT NULL
- created_at (timestamp without time zone) | NULL

---
### Table: stafftab_summary_report_task
Columns:
- id (integer) | NOT NULL
- region (character varying) | NULL
- generator_type (character varying) | NOT NULL
- data_type (character varying) | NULL
- edu_org_type (character varying) | NULL
- code_gu (character varying) | NULL
- sub_gu_codes (ARRAY) | NOT NULL
- abp (integer) | NOT NULL
- variant_uuid (character varying) | NOT NULL
- budget_program (integer) | NULL
- stafftab_version (integer) | NULL
- is_education (boolean) | NULL
- detailed_report (boolean) | NOT NULL
- locale (character varying) | NOT NULL
- include_department (boolean) | NOT NULL
- user_id (character varying) | NOT NULL
- try_number (integer) | NOT NULL
- status (character varying) | NOT NULL
- progress (double precision) | NOT NULL
- task_message (jsonb) | NULL
- year (integer) | NOT NULL
- create_date (timestamp without time zone) | NOT NULL
- export_date (timestamp without time zone) | NULL

---
### Table: budget_request_note_desc
Columns:
- id (bigint) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- gu (character varying) | NOT NULL
- gkkp (character varying) | NULL
- data_type_id (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- region (character) | NOT NULL
- variant_id (character) | NOT NULL
- user_id (character) | NOT NULL
- name_kk (text) | NOT NULL
- name_ru (text) | NOT NULL
- name_en (text) | NOT NULL
- title_indicator (character) | NOT NULL
- title_sorting (integer) | NOT NULL
- update_date (timestamp with time zone) | NULL

---
### Table: budget_request_form_gkkp_429
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- period (character varying) | NOT NULL
- conclusion (character varying) | NOT NULL
- summa (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: budget_project_monitoring
Columns:
- id (integer) | NOT NULL
- nom_za (character varying) | NOT NULL
- expense_code (character varying) | NOT NULL
- year (integer) | NOT NULL
- user_id (character varying) | NOT NULL
- update_date (timestamp without time zone) | NOT NULL
- region (character varying) | NOT NULL
- func (character varying) | NOT NULL

---
### Table: stafftab_ead_c
Columns:
- id (bigint) | NOT NULL
- value_bool (boolean) | NULL
- value_text (text) | NULL
- value_number (double precision) | NULL
- value_salary_rate (double precision) | NULL
- value_norm_rate (double precision) | NULL
- value_date (date) | NULL
- ead (bigint) | NOT NULL
- allow_rate (boolean) | NOT NULL
- version (bigint) | NOT NULL
- budget_program (integer) | NULL
- calc_hint (ARRAY) | NULL
- start_period (date) | NULL
- end_period (date) | NULL
- has_document (boolean) | NOT NULL

---
### Table: stafftab_ead_d
Columns:
- id (bigint) | NOT NULL
- emp (bigint) | NOT NULL
- conf (bigint) | NOT NULL
- value_bool (boolean) | NULL
- value_text (text) | NULL
- value_number (double precision) | NULL
- value_salary_rate (double precision) | NULL
- value_norm_rate (double precision) | NULL
- value_date (date) | NULL
- value_military_rank (bigint) | NULL
- value_military_title (bigint) | NULL
- budget_program (integer) | NULL
- calc_hint (ARRAY) | NULL
- fact_hours (double precision) | NULL
- start_period (date) | NULL
- end_period (date) | NULL
- has_document (boolean) | NOT NULL

---
### Table: budget_request_form_gkkp_412_v2
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- year (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- name_ru (character varying) | NULL
- name_kk (character varying) | NULL
- unit (character varying) | NOT NULL
- amount (numeric) | NOT NULL
- cost (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- region_code (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp with time zone) | NOT NULL

---
### Table: dict_items_appendix_6
Columns:
- id (integer) | NOT NULL
- table_number (character varying) | NULL
- table_type (character varying) | NULL
- table_name_ru (text) | NULL
- table_name_kk (text) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_pkfo_3mb
Columns:
- id (integer) | NOT NULL
- section (integer) | NULL
- note (integer) | NULL
- line_code (character varying) | NULL
- name_kk (text) | NULL
- name_ru (text) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_pkfo_2mb
Columns:
- id (integer) | NOT NULL
- note (integer) | NULL
- line_code (character varying) | NULL
- name_kk (text) | NULL
- name_ru (text) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_pkfo_1mb
Columns:
- id (integer) | NOT NULL
- section (integer) | NULL
- subsection (integer) | NULL
- note (character varying) | NULL
- line_code (character varying) | NULL
- balance_code125 (character varying) | NULL
- balance_code126 (character varying) | NULL
- balance_code124 (character varying) | NULL
- balance_code127 (character varying) | NULL
- name_kk (text) | NULL
- name_ru (text) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_pkfo_4mb
Columns:
- id (integer) | NOT NULL
- line_code (character varying) | NULL
- name_kk (text) | NULL
- name_ru (text) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: dict_fuels
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kk (character varying) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: budget_execution_alteration_request_status_hist
Columns:
- id (integer) | NOT NULL
- budget_execution_alteration_request_id (bigint) | NOT NULL
- user_id (character varying) | NOT NULL
- comment (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- status (integer) | NOT NULL

---
### Table: budget_cost_clarif
Columns:
- id (integer) | NOT NULL
- source (integer) | NOT NULL
- region (integer) | NOT NULL
- gr (integer) | NOT NULL
- pgr (integer) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- name_ppi (integer) | NULL
- ind_value (double precision) | NULL
- amount_correct (double precision) | NOT NULL
- ind_change (integer) | NULL
- amount_obk (double precision) | NULL
- note (character varying) | NULL
- year (integer) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL

---
### Table: budget_cost_data
Columns:
- id (integer) | NOT NULL
- gr (integer) | NULL
- pgr (integer) | NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- value (double precision) | NULL
- year (integer) | NOT NULL
- region (character varying) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NULL
- budget_request (double precision) | NULL
- cur_year (integer) | NULL
- bip_code (character varying) | NULL
- value_obk (double precision) | NULL
- create_date (date) | NULL
- status (character varying) | NULL
- update_date (timestamp without time zone) | NULL
- data_type (integer) | NULL
- spf (integer) | NULL

---
### Table: budget_consolidate_calc_expens
Columns:
- id (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- gr (integer) | NOT NULL
- abp (integer) | NOT NULL
- gu (character varying) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- kass_ras (double precision) | NULL
- fact_ras (double precision) | NULL
- utoch_plan (double precision) | NULL
- region (character varying) | NULL
- update_date (timestamp without time zone) | NULL
- user_id (character varying) | NULL
- variant (character varying) | NULL

---
### Table: budget_consolidate_calc_expens_b_240104
Columns:
- id (integer) | NULL
- cur_year (integer) | NULL
- gr (integer) | NULL
- abp (integer) | NULL
- gu (character varying) | NULL
- prg (integer) | NULL
- ppr (integer) | NULL
- spf (integer) | NULL
- kass_ras (double precision) | NULL
- fact_ras (double precision) | NULL
- utoch_plan (double precision) | NULL
- region (character varying) | NULL
- update_date (timestamp without time zone) | NULL
- user_id (character varying) | NULL

---
### Table: budget_clarify_income
Columns:
- id (bigint) | NOT NULL
- variant (character varying) | NOT NULL
- region (character varying) | NOT NULL
- cur_year (integer) | NOT NULL
- kat (integer) | NOT NULL
- cls (integer) | NOT NULL
- pcl (integer) | NOT NULL
- spf (integer) | NOT NULL
- offer_val (double precision) | NULL
- approv_val (double precision) | NULL
- note (character varying) | NULL

---
### Table: budget_cabinet_furniture
Columns:
- id (integer) | NOT NULL
- code_cabinet (character varying) | NOT NULL
- code_furniture (character varying) | NOT NULL
- amount (integer) | NOT NULL

---
### Table: budget_clarify_rate
Columns:
- id (integer) | NOT NULL
- variant (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- region (character varying) | NOT NULL
- cur_year (integer) | NOT NULL
- optim_val (double precision) | NULL
- econom_val (double precision) | NULL
- add_need_val (double precision) | NULL
- repart_plus_val (double precision) | NULL
- repart_min_val (double precision) | NULL
- note (character varying) | NULL
- is_correct_counted (boolean) | NULL

---
### Table: budget_execution_pf_status
Columns:
- id (bigint) | NOT NULL
- budget_execution_pf_id (bigint) | NOT NULL
- user_id (character varying) | NOT NULL
- comment (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- status (integer) | NOT NULL

---
### Table: budget_execution_pf_status_hist
Columns:
- id (bigint) | NOT NULL
- budget_execution_pf_id (bigint) | NOT NULL
- user_id (character varying) | NOT NULL
- comment (character varying) | NULL
- create_date (timestamp without time zone) | NULL
- status (integer) | NOT NULL

---
### Table: budget_execution_pf
Columns:
- id (bigint) | NOT NULL
- year (integer) | NOT NULL
- region (character varying) | NOT NULL
- abp (integer) | NULL
- gu (character varying) | NULL
- description (character varying) | NULL
- user_id (character varying) | NOT NULL
- level (character varying) | NOT NULL
- parent_id (bigint) | NULL
- create_date (timestamp without time zone) | NULL
- update_date (timestamp without time zone) | NULL
- delete_date (timestamp without time zone) | NULL

---
### Table: staffing_table_01_29
Columns:
- id (bigint) | NOT NULL
- region (integer) | NULL
- creation_date (date) | NOT NULL
- pos (bigint) | NOT NULL
- admission_date (date) | NULL
- taking_office_date (date) | NOT NULL
- full_name (text) | NULL
- retiree (boolean) | NOT NULL
- time_rate (double precision) | NULL
- cd_date (date) | NULL
- cd_years (integer) | NULL
- cd_months (integer) | NULL
- cd_days (integer) | NULL
- vacancy (boolean) | NULL
- department (bigint) | NOT NULL
- experience_vacancy (double precision) | NULL
- work_start_date (date) | NULL
- work_end_date (date) | NULL
- bonus (boolean) | NULL
- serial_number (integer) | NULL
- edu_level (bigint) | NULL
- edu_subjects (ARRAY) | NULL

---
### Table: agreement_operation
Columns:
- id (integer) | NOT NULL
- mode_code (character varying) | NOT NULL
- agr_code (integer) | NOT NULL
- operation_code (character varying) | NOT NULL

---
### Table: stafftab_version_01_29
Columns:
- id (bigint) | NOT NULL
- org_code (character varying) | NOT NULL
- year (integer) | NOT NULL
- archived (boolean) | NOT NULL
- title (text) | NULL

---
### Table: budget_request_form_gkkp_429_files
Columns:
- id (integer) | NOT NULL
- form (character varying) | NOT NULL
- data_type (character varying) | NOT NULL
- gr (integer) | NOT NULL
- bin (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- cur_year (integer) | NOT NULL
- year (integer) | NOT NULL
- file_type (character varying) | NOT NULL
- file_id (integer) | NOT NULL
- row_id (integer) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NOT NULL
- update_data (timestamp without time zone) | NOT NULL

---
### Table: bip_capacity_inds_objects
Columns:
- id (integer) | NOT NULL
- code_capacity (character varying) | NOT NULL
- code_object (character varying) | NOT NULL

---
### Table: bip_contract_list
Columns:
- id (bigint) | NOT NULL
- year (integer) | NOT NULL
- region (character varying) | NOT NULL
- gu (character varying) | NOT NULL
- abp (integer) | NOT NULL
- prg (integer) | NOT NULL
- ppr (integer) | NULL
- spf (integer) | NOT NULL
- supplier (text) | NOT NULL
- bip_code (character varying) | NOT NULL
- po_header_id (bigint) | NOT NULL
- job_code (integer) | NOT NULL

---
### Table: bip_capacity_indicators_facilities_list
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- name_en (character varying) | NULL
- unit (character varying) | NULL
- data_type (character varying) | NULL
- source_type (character varying) | NULL
- calc_type (character varying) | NULL
- criteria_type (character varying) | NULL
- begin_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL
- operator (character varying) | NULL
- is_deleted (boolean) | NULL
- user_name (character varying) | NULL
- update_time (timestamp without time zone) | NULL

---
### Table: budget_fact515
Columns:
- id (integer) | NOT NULL
- region_code (character varying) | NOT NULL
- budget_type (character varying) | NOT NULL
- funding_source (character varying) | NOT NULL
- payment_number (character varying) | NOT NULL
- payment_date (date) | NOT NULL
- amount (numeric) | NOT NULL
- notification_number (character varying) | NULL
- invoice_number (character varying) | NULL
- gu_prg_ppr_code (character varying) | NULL
- gu (character varying) | NULL
- abp (integer) | NULL
- prg (integer) | NULL
- ppr (integer) | NULL
- spf (integer) | NULL
- iin_bin (character varying) | NOT NULL
- name (character varying) | NOT NULL
- bik (character varying) | NOT NULL
- iik (character varying) | NOT NULL
- update_date (timestamp without time zone) | NOT NULL

---
### Table: stafftab_edu_wl_01_29
Columns:
- id (bigint) | NOT NULL
- emp (bigint) | NOT NULL
- conf (bigint) | NOT NULL
- value (double precision) | NOT NULL

---
### Table: stafftab_edu_wl_c_01_29
Columns:
- id (bigint) | NOT NULL
- hours (bigint) | NOT NULL
- version (bigint) | NOT NULL

---
### Table: bip_project_object_list
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- name_en (character varying) | NULL
- begin_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: bip_project_power_list
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- object_type (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- name_en (character varying) | NULL
- begin_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: bip_project_realizing_list
Columns:
- id (integer) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NULL
- name_en (character varying) | NULL
- begin_date (timestamp without time zone) | NULL
- end_date (timestamp without time zone) | NULL

---
### Table: stafftab_ead_c_01_29
Columns:
- id (bigint) | NOT NULL
- value_bool (boolean) | NULL
- value_text (text) | NULL
- value_number (double precision) | NULL
- value_salary_rate (double precision) | NULL
- value_norm_rate (double precision) | NULL
- value_date (date) | NULL
- ead (bigint) | NOT NULL
- allow_rate (boolean) | NOT NULL
- version (bigint) | NOT NULL
- budget_program (integer) | NULL
- calc_hint (ARRAY) | NULL

---
### Table: budget_energy_tariffs
Columns:
- id (integer) | NOT NULL
- comm_object (character varying) | NOT NULL
- energy (character varying) | NOT NULL
- region_obl (character varying) | NOT NULL
- rate (double precision) | NULL
- beg_date (date) | NULL
- end_date (date) | NULL

---
### Table: budget_execution_alteration_request_utoch_link
Columns:
- id (bigint) | NOT NULL
- budget_execution_alteration_request_utoch_id (bigint) | NOT NULL
- budget_execution_alteration_request_id (bigint) | NOT NULL
- create_date (timestamp without time zone) | NULL

---
### Table: budget_execution_artificial_gu
Columns:
- id (bigint) | NOT NULL
- abp (integer) | NOT NULL
- region (character varying) | NOT NULL
- code (character varying) | NOT NULL
- artificial_code (character varying) | NOT NULL

---
### Table: budget_request_form_gkkp_01_142_decode
Columns:
- id (bigint) | NOT NULL
- enstru_code (character varying) | NOT NULL
- add_detail (character varying) | NULL
- amount (numeric) | NOT NULL
- price (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- file_hash (character varying) | NULL
- category_id (character varying) | NULL
- unit_code (character varying) | NULL

---
### Table: budget_request_form_03_141_decode
Columns:
- id (bigint) | NOT NULL
- category_id (character varying) | NOT NULL
- enstru_code (character varying) | NOT NULL
- add_detail (character varying) | NULL
- amount (numeric) | NOT NULL
- price (numeric) | NOT NULL
- variant (character varying) | NOT NULL
- user_name (character varying) | NULL
- update_data (timestamp with time zone) | NULL
- file_hash (character varying) | NULL
- unit_code (character varying) | NULL

---
### Table: reports_constructor_template
Columns:
- id (bigint) | NOT NULL
- name (character varying) | NOT NULL
- description (text) | NULL
- category (character varying) | NULL
- regions (ARRAY) | NOT NULL
- filter_settings (jsonb) | NOT NULL
- user_id (character varying) | NOT NULL

---
### Table: dict_category_report
Columns:
- id (bigint) | NOT NULL
- code (character varying) | NOT NULL
- name_ru (character varying) | NOT NULL
- name_kz (character varying) | NOT NULL
- beg_date (date) | NULL
- end_date (date) | NULL
- name_en (character varying) | NOT NULL

---
### Table: dict_budget_execution_forms
Columns:
- id (integer) | NOT NULL
- form (character varying) | NULL
- code (character varying) | NULL
- type (integer) | NULL
- type_name (character varying) | NULL
- period (integer) | NULL
- operation_code (ARRAY) | NULL
- level (ARRAY) | NULL
- active (boolean) | NULL
- parent_code (character varying) | NULL

---
