# Demo 4 · Kamus Data

[Persiapan](../README.md) · [Troubleshooting](../TROUBLESHOOTING.md)

Kerjakan 4.1-4.3: lengkapi kamus data. `BRANCHES` dan `CUSTOMERS` sudah terisi sebagai contoh.

## 4.1 Samakan nama dan baca contoh

Buka `latihan-kamus-data.md`. Bagian `BRANCHES` dan `CUSTOMERS` sudah lengkap: perhatikan cara menulis `Wajib diisi?`, `FK -> BRANCHES`, dan `CK:`. Samakan nama kolom di ERD dengan nama di file ini (nama baku untuk DDL sesi 22), lalu simpan ERD.

## 4.2 Isi `ACCOUNTS` dan `TRANSACTIONS`

Ganti setiap `TODO` di kolom **Tipe Oracle**, **Wajib diisi?**, dan **Constraint** (15 baris). Kolom tanpa constraint: hapus `TODO`, biarkan kosong.

## 4.3 Cek kamus terhadap ERD

Salin ERD dan kamus, lalu jalankan cek dengan dua file:

```bash
docker cp ../demo-3/erd-tabungan-umkm.drawio.png oracle-alp:/tmp/erd-cek.drawio.png
docker cp latihan-kamus-data.md oracle-alp:/tmp/kamus-cek.md
docker exec oracle-alp python3 /tmp/cek-erd.py /tmp/erd-cek.drawio.png /tmp/kamus-cek.md
```

Yang harus terlihat: baris 7 dan 8 bertambah sampai `27 dari 27 kolom` dan `Subtotal otomatis` `80 / 80` (jumlah kolom mengikuti ERD). Sebelum `TODO` diisi, ERD yang lengkap mendapat `12 dari 27 kolom` dan subtotal `69 / 80`: hanya `BRANCHES` dan `CUSTOMERS` yang sudah cocok.

## Tantangan tambahan Demo 4 (opsional)

1. Pilih `CUSTOMERS` dan `TRANSACTIONS`. Untuk tiap tabel tulis satu baris data yang valid dan dua baris yang harus ditolak database. Untuk setiap baris yang ditolak, sebut constraint yang menolaknya: `PK`/`UQ` (data ganda), `FK` (parent tidak ada), atau `CK` (nilai di luar aturan).
2. Isi kolom **Nilai bawaan** di `ACCOUNTS` dan `TRANSACTIONS` untuk kolom yang pantas punya `DEFAULT`, dan tulis alasannya satu kalimat per kolom.
