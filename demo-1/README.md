# Demo 1 · Setup Oracle & `ALP_DEV`

[Persiapan](../README.md) · [Troubleshooting](../TROUBLESHOOTING.md)

Kerjakan 1.1-1.6: jalankan Oracle di Docker, buat user `ALP_DEV`, sambungkan VS Code, lalu jalankan query cek.

Semua perintah di bagian ini sama untuk Windows (PowerShell), macOS, dan Linux. Docker Desktop (atau Rancher Desktop) harus sudah jalan: ikon paus di menu bar/taskbar berstatus running.

## 1.1 Cek tools

Buka terminal di folder `demo-1`, lalu jalankan:

```bash
docker --version
docker images container-registry.oracle.com/database/free
```

Yang harus terlihat: `Docker version 29...`, dan satu baris image `container-registry.oracle.com/database/free:23.26.4.0-lite` (±1,66 GB di disk). Kalau image belum ada, jalankan `docker pull container-registry.oracle.com/database/free:23.26.4.0-lite` (±1,3 GB download).

## 1.2 Jalankan container Oracle

Ganti `ISI_PASSWORD_ADMIN` dengan password admin database buatan sendiri: minimal 8 karakter, campur huruf besar, huruf kecil, dan angka, tanpa simbol. Catat password ini.

```bash
docker run -d --name oracle-alp -p 1521:1521 -e ORACLE_PWD=ISI_PASSWORD_ADMIN -v oracle-alp-data:/opt/oracle/oradata container-registry.oracle.com/database/free:23.26.4.0-lite
```

| Bagian perintah | Artinya |
| --- | --- |
| `--name oracle-alp` | Nama container, dipakai di semua perintah berikutnya |
| `-p 1521:1521` | Port Oracle di laptop = port di container |
| `-e ORACLE_PWD=...` | Password admin (`SYS`, `SYSTEM`) |
| `-v oracle-alp-data:/opt/oracle/oradata` | Data disimpan di volume, tetap ada walau container dihapus |

## 1.3 Tunggu sampai siap

```bash
docker ps
```

Ulangi sampai kolom `STATUS` container `oracle-alp` menjadi `(healthy)`:

```text
CONTAINER ID   IMAGE                                                        ...   STATUS                   PORTS                                         NAMES
6eb8bea4fff9   container-registry.oracle.com/database/free:23.26.4.0-lite   ...   Up 3 minutes (healthy)   0.0.0.0:1521->1521/tcp, [::]:1521->1521/tcp   oracle-alp
```

Selama database masih menyiapkan diri, status tertulis `(starting)`. Status `(healthy)` muncul ±30-60 detik setelah `run`; pada laptop dengan 2-4 core bisa sampai ±2 menit.

Kalau baris `docker ps` terpotong di terminal yang sempit, maksimalkan panel terminal atau pakai format ringkas:

```bash
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
```

Pengecekan lain: `docker logs oracle-alp` memuat baris `DATABASE IS READY TO USE!` (baris ini bisa tergulung ke atas oleh log berikutnya).

## 1.4 Buat user `ALP_DEV`

Salin script ke container, lalu jalankan sebagai admin:

```bash
docker cp setup/01-alp-dev.sql oracle-alp:/tmp/01-alp-dev.sql
docker exec -it oracle-alp sqlplus / as sysdba "@/tmp/01-alp-dev.sql"
```

Tanda kutip pada `"@/tmp/01-alp-dev.sql"` wajib di Windows PowerShell (tanpa kutip, `@/` dibaca sebagai splatting dan muncul `Unrecognized token in source text`); di bash dan zsh tanda kutip ini tidak mengganggu.

Saat muncul `Password baru untuk ALP_DEV:`, ketik password untuk `ALP_DEV` (tidak tampil di layar), lalu Enter. Catat password ini.

Yang harus terlihat:

```text
Tablespace USERS dibuat.

USERNAME     DEFAULT_TABLESPACE   ACCOUNT_STATUS
------------ -------------------- ----------------
ALP_DEV      USERS                OPEN

1 row selected.

Setup ALP_DEV selesai.
```

Script ini aman dijalankan ulang. Pada percobaan kedua, baris pertama berubah menjadi `Tablespace USERS sudah ada.`, dan password `ALP_DEV` diganti dengan yang baru diketik.

## 1.5 Buat koneksi di SQL Developer for VS Code

1. Klik ikon **SQL Developer** (ikon database) di activity bar kiri VS Code.
2. Di bagian **Connections**, klik **Create Connection** (atau tombol **+**).
3. Isi form **Create Connection**:

| Field | Nilai |
| --- | --- |
| Connection Name | `ALP_DEV @ FREEPDB1` |
| Connection Type | `Basic` (default) |
| Hostname | `localhost` |
| Port | `1521` |
| Type | `Service Name` (default) |
| Service Name | `FREEPDB1` |
| Authentication Type / Role | `Default` (default) |
| Username | `ALP_DEV` |
| Password | password dari 1.4 |
| Save Password | dicentang (database lokal latihan) |

4. Klik **Test**. Di pojok kanan bawah muncul notifikasi singkat:

```text
Test passed for connection: ALP_DEV @ FREEPDB1
```

5. Klik **Save**. Koneksi `ALP_DEV @ FREEPDB1` muncul di bagian **Connections**.

Centang **Save Password** sebelum **Save**; kalau tidak, password ditanya lagi setiap koneksi dibuka. Kalau panel bawah VS Code (terminal) terbuka, form terpotong dan tombol **Test**/**Save** tertutup: tutup panel dulu.

Setelah VS Code pertama kali dibuka, ekstensi butuh ±20 detik (`Activating...` di status bar) sebelum ikon **SQL Developer** muncul di activity bar. Kalau VS Code menampilkan dialog `Do you trust the authors of the files in this folder?` (Restricted Mode), pilih **Trust Folder & Continue**; sebelum itu tombol Run belum aktif.

Kalau muncul pertanyaan `Allow automated usage reporting to Oracle?`, pilih **Decline**.

## 1.6 Jalankan query cek

1. Buka `check/00-cek-koneksi.sql`.
2. Klik ikon **Attach Connection** di kanan atas editor, pilih `ALP_DEV @ FREEPDB1`. Status bar bawah berubah menjadi `(Dedicated) ALP_DEV @ FREEPDB1`.
3. Klik **Run Script (F5)**.

Yang harus terlihat di tab **Script Output**:

```text
LOGIN_SEBAGAI   DATABASE     SERVICE
--------------- ------------ ------------
ALP_DEV         FREEPDB1     freepdb1


BANNER_FULL
-------------------------------------------------------------------------------------
Oracle AI Database 26ai Free Release 23.26.4.0.0 - Develop, Learn, and Run for Free
Version 23.26.4.0.0
```

Tiap file `.sql` baru harus dipasangi koneksi sendiri (langkah 2). Kalau lupa, Run menampilkan `Error: No session associated with the current worksheet`.

Untuk menjalankan satu query saja, taruh kursor di query itu lalu tekan **Run Statement (⌘Enter / Ctrl+Enter)**: hasilnya tampil sebagai tabel di tab **Query Result**.

## Tantangan tambahan Demo 1 (opsional)

1. Buat satu query yang menampilkan tiga hal sekaligus: nama user yang sedang login, nama PDB, dan service name. Petunjuk: fungsi `SYS_CONTEXT` dengan namespace `'USERENV'` dan parameter `SESSION_USER`, `CON_NAME`, `SERVICE_NAME`; ambil dari tabel `dual`. Cocokkan hasilnya dengan status bar.
2. Jalur cadangan tanpa VS Code: login ke database memakai SQL*Plus di dalam container (`docker exec -it oracle-alp sqlplus alp_dev@//localhost:1521/FREEPDB1`), jalankan query dari nomor 1, lalu keluar dengan `exit`.
