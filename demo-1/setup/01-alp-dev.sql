-- Sesi 21 · Setup user ALP_DEV di FREEPDB1
-- Jalankan sebagai SYSDBA di dalam container:
--   docker exec -it oracle-alp sqlplus / as sysdba "@/tmp/01-alp-dev.sql"
-- Aman dijalankan ulang: tablespace dan user hanya dibuat kalau belum ada.
SET VERIFY OFF FEEDBACK OFF
WHENEVER SQLERROR EXIT FAILURE
ALTER SESSION SET CONTAINER = FREEPDB1;
SET SERVEROUTPUT ON

ACCEPT alp_pwd CHAR PROMPT 'Password baru untuk ALP_DEV: ' HIDE

DECLARE
  v_dir   VARCHAR2(400);
  v_count NUMBER;
BEGIN
  SELECT COUNT(*) INTO v_count FROM dba_tablespaces WHERE tablespace_name = 'USERS';
  IF v_count = 0 THEN
    SELECT REGEXP_SUBSTR(file_name, '^.*/') INTO v_dir
      FROM dba_data_files WHERE tablespace_name = 'SYSTEM' FETCH FIRST 1 ROW ONLY;
    EXECUTE IMMEDIATE 'CREATE TABLESPACE users DATAFILE ''' || v_dir || 'users01.dbf'''
                   || ' SIZE 100M AUTOEXTEND ON NEXT 50M MAXSIZE 2G';
    DBMS_OUTPUT.PUT_LINE('Tablespace USERS dibuat.');
  ELSE
    DBMS_OUTPUT.PUT_LINE('Tablespace USERS sudah ada.');
  END IF;
END;
/

CREATE USER IF NOT EXISTS alp_dev IDENTIFIED BY "&alp_pwd"
  DEFAULT TABLESPACE users QUOTA UNLIMITED ON users;
ALTER USER alp_dev IDENTIFIED BY "&alp_pwd";
GRANT DB_DEVELOPER_ROLE TO alp_dev;

SET FEEDBACK ON
COLUMN username FORMAT A12
COLUMN default_tablespace FORMAT A20
COLUMN account_status FORMAT A16
SELECT username, default_tablespace, account_status FROM dba_users WHERE username = 'ALP_DEV';
PROMPT Setup ALP_DEV selesai.
EXIT
