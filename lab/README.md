# Lab · ERD ALP Tim + Peer Review + Kamus Data

[Persiapan](../README.md) · [Troubleshooting](../TROUBLESHOOTING.md)

**Skenario.** Tim sudah punya tema dan backlog MVP dari sesi 20. Tim lead meminta rancangan data ALP sebelum satu pun tabel dibuat: ERD yang menjawab fitur MVP, sudah di-review tim lain, dan dilengkapi kamus data. Sesi 22 menulis `CREATE TABLE` langsung dari dua file itu. Hasil dinilai dengan rubrik di bawah.

Satu laptop per tim. Nama tim ditulis huruf kecil tanpa spasi (mis. `tim-garuda`).

| Langkah | Yang dikerjakan | Menit |
| --- | --- | --- |
| Skenario dan rubrik | Baca skenario, rubrik, dan contoh bentuk di slide | 3 |
| L.1 Daftar data | Dari tema dan backlog MVP, tulis 4–6 entity dan fitur yang memakainya. Relasi N:M (mis. satu pesanan berisi banyak produk) disiapkan tabel penghubungnya | 4 |
| L.2 Gambar ERD tim | Buat `erd-alp-<nama-tim>.drawio.png` dengan langkah 3.1–3.2 | 12 |
| L.3 Peer review | Kirim file `.drawio.png` ke tim lain (chat atau flashdisk). Review memakai `checklist-erd.md` bagian "Lab L.3". Tulis maksimal 3 temuan di `review-untuk-<nama-tim-lain>.md`, satu kalimat per temuan (apa yang diubah dan kenapa), lalu kirim ke tim pemilik ERD | 7 |
| L.4 Kamus data tim | Salin `kamus-data-template.md` menjadi `kamus-data-<nama-tim>.md`. Bagi tabel antar anggota. Di bawah tiap temuan review yang diterima tim, tulis `Tanggapan:` (diterapkan atau ditolak, dengan alasan) dan perbarui ERD serta kamus | 7 |
| L.5 Cek otomatis | Jalankan `cek-erd.py` untuk file tim (perintah di bawah), perbaiki, ulangi | 2 |

```bash
docker cp cek-erd.py oracle-alp:/tmp/cek-erd.py
docker cp erd-alp-<nama-tim>.drawio.png oracle-alp:/tmp/erd-cek.drawio.png
docker cp kamus-data-<nama-tim>.md oracle-alp:/tmp/kamus-cek.md
docker exec oracle-alp python3 /tmp/cek-erd.py /tmp/erd-cek.drawio.png /tmp/kamus-cek.md
```

Ganti `<nama-tim>` dengan nama tim. Kamus belum ada: lewati baris `docker cp` kedua untuk kamus dan jalankan `docker exec` tanpa argumen terakhir. Cek boleh dijalankan dari laptop anggota mana pun yang punya container `oracle-alp`.

## Rubrik Lab (100 poin)

| Kriteria | Poin | Dinilai oleh | Indikator keberhasilan |
| --- | --- | --- | --- |
| Jumlah tabel | 10 | `cek-erd.py` | Minimal 4 tabel dengan judul sendiri dan minimal 2 kolom |
| Primary key | 10 | `cek-erd.py` | Setiap tabel punya baris `PK` |
| Relasi crow's foot | 15 | `cek-erd.py` | Kedua ujung garis memakai simbol crow's foot; minimal jumlah tabel dikurangi 1 relasi (paling sedikit 3); N:M dipecah tabel penghubung |
| FK di sisi banyak | 10 | `cek-erd.py` | Ujung sisi banyak menempel ke baris `FK`, ujung lain ke baris `PK` atau `UQ` |
| Tipe data Oracle | 10 | `cek-erd.py` | Setiap kolom bertipe Oracle (`VARCHAR2` dengan panjang); kolom uang `NUMBER(15,2)` |
| Penamaan | 5 | `cek-erd.py` | Tabel `HURUF_BESAR` dan tidak kembar, kolom `snake_case` |
| Kamus sama dengan ERD | 15 | `cek-erd.py` | Setiap tabel dan kolom ERD ada di kamus dengan tipe yang sama, tanpa kolom tambahan |
| Kamus lengkap | 5 | `cek-erd.py` | `Wajib diisi?` YA/TIDAK dan contoh nilai terisi; kolom `PK` ditandai `PK`, kolom `FK` ditulis `FK -> TABEL` |
| Cocok dengan fitur MVP | 10 | Review tim lain | Setiap entity terkait satu fitur MVP; tidak ada kolom berisi banyak nilai; kolom bernilai terbatas punya `CK` di kamus |
| Peer review untuk tim lain | 5 | Review | Maksimal 3 temuan, satu kalimat per temuan: apa yang diubah dan kenapa |
| Menanggapi review | 5 | Review | Setiap temuan yang diterima punya `Tanggapan:`; ERD dan kamus sudah diperbarui sesuai keputusan |
| **Total** | **100** | | |

Target minimal 60 poin. Cek sendiri dengan `cek-erd.py` dan daftar rubrik di atas.

Cek otomatis hanya menghitung bentuk: tabel, key, garis, tipe, dan kecocokan kamus. Benar tidaknya entity untuk fitur tim dinilai manusia.

## Bonus Lab (opsional, maks. +10)

1. (+5) Pilih satu entity yang statusnya berubah-ubah (pesanan, tiket, pengajuan). Tambahkan entity histori status (status lama, status baru, waktu berubah) sebagai relasi 1:N dari entity itu, lengkap di ERD dan kamus.
2. (+5) Tulis tiga pertanyaan bisnis yang harus bisa dijawab data tim di `pertanyaan-bisnis-<nama-tim>.md` (mis. "berapa total transaksi per kategori bulan ini?"). Untuk tiap pertanyaan, tuliskan urutan tabel yang dilalui dan kolom FK yang dipakai.
