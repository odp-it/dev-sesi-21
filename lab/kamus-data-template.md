# Kamus Data · ERD Kelompok

Lab L.4 · isi satu tabel per bagian, salin bagian "Tabel" untuk setiap entity di ERD kelompok. Kamus ini dipakai langsung di sesi 22 untuk menulis `CREATE TABLE`, jadi lengkapi sampai tidak ada sel kosong.

Kelompok: `<nama-kelompok>` · Tanggal: `<tanggal>`

`cek-erd.py` membaca file ini: judul bagian tetap berbentuk ``## Tabel: `NAMA_TABEL` `` (sama dengan judul tabel di ERD) dan nama kolom tabel markdown tidak diubah.

## Cara mengisi

| Kolom | Isi |
| --- | --- |
| Kolom | Nama kolom `snake_case`, sama persis dengan di ERD |
| Tipe Oracle | `NUMBER`, `NUMBER(15,2)` untuk uang, `VARCHAR2(n)`, `DATE` atau `TIMESTAMP` |
| Wajib diisi? | `YA` (`NOT NULL`) atau `TIDAK` (boleh kosong) |
| Constraint | `PK`, `FK -> TABEL.kolom`, `UQ`, atau `CK` disertai aturannya; kosongkan bila tidak ada |
| Nilai bawaan | `DEFAULT` bila ada, mis. `SYSTIMESTAMP` atau `'AKTIF'` |
| Contoh nilai | Satu contoh data simulasi (pakai `SIM` atau `example.com`) |

## Tabel: `NAMA_TABEL`

Fungsi tabel (satu kalimat): `...`

| Kolom | Tipe Oracle | Wajib diisi? | Constraint | Nilai bawaan | Contoh nilai |
| --- | --- | --- | --- | --- | --- |
| `nama_tabel_id` | `NUMBER` | YA | `PK` | | `1` |
| | | | | | |
| | | | | | |
| | | | | | |

Relasi dari tabel ini: `NAMA_TABEL 1:N TABEL_LAIN` lewat kolom `...`

## Pemeriksaan sebelum sesi 22

- [ ] Setiap tabel di ERD punya satu bagian di kamus ini.
- [ ] Setiap tabel punya tepat satu `PK`.
- [ ] Setiap `FK` menyebut tabel dan kolom yang ditunjuk.
- [ ] Kolom uang memakai `NUMBER(15,2)`, bukan `FLOAT`.
- [ ] Kolom yang nilainya dibatasi (status, jenis, kategori) punya `CK` dengan daftar nilainya.
- [ ] Setiap kolom punya satu contoh nilai simulasi.
