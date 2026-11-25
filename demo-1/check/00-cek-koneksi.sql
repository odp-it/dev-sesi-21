-- Sesi 21 · Cek koneksi ALP_DEV (jalankan dari SQL client sebagai ALP_DEV)
COLUMN login_sebagai FORMAT A15
COLUMN database      FORMAT A12
COLUMN service       FORMAT A12
COLUMN banner_full   FORMAT A85

SELECT USER AS login_sebagai,
       SYS_CONTEXT('USERENV', 'CON_NAME') AS database,
       SYS_CONTEXT('USERENV', 'SERVICE_NAME') AS service
FROM dual;

SELECT banner_full FROM v$version;
