# Demo 3 · Gambar ERD di Draw.io

[Persiapan](../README.md) · [Troubleshooting](../TROUBLESHOOTING.md)

Kerjakan 3.1–3.3: gambar ERD di Draw.io dengan shape **Entity Relation** dan relasi crow's foot.

## 3.1 Buat file ERD dan tabel

1. Di Explorer, klik folder `demo-3`, lalu klik ikon **New File...** dan ketik nama `erd-tabungan-umkm.drawio.png`, Enter.
   File berakhiran `.drawio.png` terbuka sebagai editor Draw.io (label `Draw.io (Binary)` di kanan atas) dan sekaligus tersimpan sebagai gambar PNG.
2. Kalau muncul notifikasi `There are multiple default editors available for the resource.`, klik **Keep Draw.io (Binary)**.
3. Buka panel shape: klik ikon panel kiri di toolbar Draw.io, pilih **Shapes**.
4. Klik **+ More Shapes**, centang **Entity Relation**, klik **Apply**. Grup **Entity Relation** muncul di panel shape.
5. Klik shape pertama di grup **Entity Relation** (tabel dengan kolom `PK`). Tabel `Table` berisi baris `UniqueID`, `Row 1`, `Row 2`, `Row 3` muncul di canvas.
6. Double-click judul `Table`, ganti dengan nama tabel (huruf besar, mis. `BRANCHES`). Double-click setiap baris, ganti dengan `nama_kolom TIPE` (mis. `branch_id NUMBER`). Pakai nama kolom dan tipe dari hasil Demo 2; Demo 4 menyamakannya dengan nama baku. Double-click sel kiri baris untuk menulis `PK`, `FK`, atau `UQ`.
7. Butuh baris tambahan: klik satu baris, klik ikon tabel di toolbar, pilih **Insert Row Below**.
8. Ulangi sampai ada satu tabel per entity, lengkap dengan tipe data Oracle (`NUMBER`, `NUMBER(15,2)` untuk uang, `VARCHAR2(n)`, `TIMESTAMP`).

Yang harus terlihat: 4 tabel di canvas, setiap tabel punya baris `PK` bergaris bawah.

## 3.2 Hubungkan relasi

1. Arahkan mouse ke ujung kanan baris `PK` di tabel sisi "satu" (mis. `branch_id` di `BRANCHES`), tarik garis ke ujung kiri baris `FK` di tabel sisi "banyak" (`branch_id` di `CUSTOMERS`). Kedua ujung garis menempel (titik hijau).
2. Dengan garis masih terpilih, buka panel **Format** (ikon panel kanan di toolbar). Di bagian **Line**, ubah **Line Start** menjadi simbol dua garis tegak (`ERmandOne`, "tepat satu") dan **Line End** menjadi simbol kaki gagak (`ERmany`, "banyak").
3. Ulangi untuk relasi lain. Foreign key selalu ada di tabel sisi "banyak".
4. Simpan dengan **Ctrl+S** (Windows/Linux) atau **⌘S** (macOS).

Yang harus terlihat: 3 garis relasi dengan ujung `||` di sisi tabel induk dan kaki gagak di sisi tabel anak. Tutup file lalu buka lagi: diagram tetap bisa diedit. File yang sama juga bisa dibuka sebagai gambar biasa (dilampirkan ke dokumen atau chat tim).

## 3.3 Cek dengan checklist dan `../lab/cek-erd.py`

1. Cocokkan ERD dengan `checklist-erd.md` bagian Demo 3.
2. Pastikan file sudah disimpan, lalu dari folder `demo-3` jalankan cek otomatis. Skrip dijalankan di dalam container `oracle-alp` (Python sudah ada di image, tidak ada instalasi baru). Perintahnya sama di PowerShell, macOS, dan Linux:

```bash
docker cp ../lab/cek-erd.py oracle-alp:/tmp/cek-erd.py
docker cp erd-tabungan-umkm.drawio.png oracle-alp:/tmp/erd-cek.drawio.png
docker exec oracle-alp python3 /tmp/cek-erd.py /tmp/erd-cek.drawio.png
```

Yang harus terlihat:

```text
Tabel terbaca: BRANCHES, CUSTOMERS, ACCOUNTS, TRANSACTIONS
...
3. Relasi crow's foot           3 relasi              15 / 15
4. FK di sisi banyak            3 dari 3 garis        10 / 10
...
Subtotal otomatis                                     60 / 80
```

Nilai maksimum di tahap ini 60: kriteria 7 dan 8 (kamus data) baru dihitung di Demo 4. Baris **Catatan** di bawah tabel menyebut yang perlu diperbaiki. Skrip hanya membaca salinan file di `/tmp` container: file di laptop dan data di database tidak berubah.

## Tantangan tambahan Demo 3 (opsional)

Kerjakan di salinan file (mis. `erd-tantangan.drawio.png`).

1. Satu rekening ternyata bisa dimiliki lebih dari satu nasabah (rekening bersama), dan satu nasabah tetap boleh punya banyak rekening. Ubah ERD: relasi apa yang terbentuk antara `CUSTOMERS` dan `ACCOUNTS`, dan tabel apa yang perlu ditambahkan? Gambar perubahannya, tandai `PK`, `FK`, dan `UQ`. Pasangan nasabah dan rekening yang sama tidak boleh tercatat dua kali.
2. Nasabah ingin menyimpan daftar penerima transfer (nama penerima dan nomor rekening penerima). Tambahkan entity-nya ke ERD, tentukan relasinya ke `CUSTOMERS`, dan putuskan kombinasi kolom mana yang harus unik.
