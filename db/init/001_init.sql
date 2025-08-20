-- создаём БД под метаданные Airflow и рабочую DWH
CREATE DATABASE airflow_meta;
CREATE DATABASE dwh;

-- учётки
\connect airflow_meta;
CREATE USER airflow WITH PASSWORD 'airflow';
GRANT ALL PRIVILEGES ON DATABASE airflow_meta TO airflow;

\connect dwh;
CREATE SCHEMA IF NOT EXISTS raw;
CREATE SCHEMA IF NOT EXISTS stg;
CREATE SCHEMA IF NOT EXISTS dds;

CREATE USER etl_user WITH PASSWORD 'etl_password';
GRANT USAGE ON SCHEMA raw, stg, dds TO etl_user;
GRANT CREATE, USAGE ON SCHEMA raw, stg TO etl_user;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA raw, stg, dds TO etl_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA raw, stg, dds GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO etl_user;

-- read-only учётка для DBeaver (по желанию)
CREATE USER bi_user WITH PASSWORD 'bi_password';
GRANT USAGE ON SCHEMA raw, stg, dds TO bi_user;
GRANT SELECT ON ALL TABLES IN SCHEMA raw, stg, dds TO bi_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA raw, stg, dds GRANT SELECT ON TABLES TO bi_user;
