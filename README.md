# 21 - Database Fundamentals & Oracle Setup

Lab ini menyiapkan Oracle Database di laptop dan merancang data sebelum tabel dibuat. Hasil akhirnya: Oracle jalan di container, user `ALP_DEV` bisa dipakai dari SQL client, ERD dan kamus data kasus contoh Tabungan UMKM, serta Tahap 1 project kelompok **ALP Database Sprint**: ERD kelompok yang sudah di-review, kamus datanya, dan repo kelompok yang berisi semuanya.

## Environment & Tools

Siapkan sebelum mulai (download image butuh waktu). Versi dikunci: jangan update tool di tengah pengerjaan.

| Tool | Versi | Catatan |
| --- | --- | --- |
| Docker Desktop (atau Rancher Desktop dengan CLI `docker`, kalau Docker Desktop tidak berlisensi di kantor) | Docker Desktop dengan Docker Engine 29.x | Windows: WSL2 aktif (butuh admin sekali). Semua perintah lab memakai `docker` |
| Image Oracle | `container-registry.oracle.com/database/free:23.26.4.0-lite` | ±1,3 GB download, ±4,5 GB setelah jalan, RAM ±2–2,7 GB |
| VS Code + ekstensi **Oracle SQL Developer for VS Code** | 26.3.x | SQL client |
| VS Code + ekstensi **Draw.io Integration** (Henning Dieterichs) | 1.19.0 | Menggambar ERD di dalam VS Code |
| Git + akun GitHub | Git 2.x | Clone dan push repo kelompok (Lab). Akun GitHub pribadi aktif |

Versi dicek 22 Nov 2026 (Marketplace VS Code). Laptop minimal RAM 8 GB, disk kosong 10 GB, port `1521` tidak dipakai aplikasi lain.

## Studi Kasus

**Tabungan UMKM** adalah fitur keuangan digital untuk nasabah UMKM di sebuah bank fiktif: pelaku usaha melihat rekening, membaca mutasi, mencatat transfer, dan melihat arus kas per kategori. Tim contoh yang membangunnya memulai dari database. Di Demo 1–4 instruktur memperagakan langkah tim contoh, dan peserta mengikuti. Database-nya menyimpan cabang, nasabah, rekening, dan transaksi. Schema ini dipakai lagi di sesi 22–23 (SQL) dan sesi REST API berikutnya. Semua data di lab ini data simulasi.

Di Lab, setiap kelompok mengerjakan hal yang sama untuk ALP-nya sendiri.

## Project Kelompok: ALP Database Sprint

**Tujuan.** Dalam dua hari (sesi 21–23 database Oracle, sesi 24 Claude Code), setiap kelompok membangun **database ALP sendiri** yang bisa dibangun ulang, terdokumentasi, dan dipresentasikan. Ini potongan database dari CP2 ALP ("ERD dan database schema") dan menjadi bekal untuk sesi Node.js/Express, React.js, dan React Native: backend, web, dan mobile membaca database yang sama.

**Kelompok dan tema.** Kelompok ALP 3–4 orang, tema sesuai project brief CP1 (sesi 17–20): Perbankan, E-commerce, atau Logistik. Satu repo per kelompok, dibuat dari template (langkah L.0 di bagian Lab).

### Jadwal dua hari

| Waktu | Sesi | Di Demo (individu) | Di Lab (kelompok, repo kelompok) | Hasil Lab |
| --- | --- | --- | --- | --- |
| Hari 1, 08.00–12.00 | 21 | Setup Oracle, baca ERD, gambar ERD, kamus data Tabungan UMKM | Kick-off, Tahap 1: repo, ERD, peer review, kamus data | `docs/erd.drawio.png`, `docs/kamus-data.md`, `docs/review.md` |
| Hari 1, 13.00–17.00 | 22 | DDL, DML, uji input salah, query dasar | Tahap 2: DDL, data contoh, uji input salah, `00-run-all.sql` | `db/00` sampai `db/03` |
| Malam hari 1 | mandiri | | Rapikan sesuai review, bangun ulang dua kali, isi README | `README.md` |
| Hari 2, 08.00–12.00 | 23 | Laporan dan validasi, transaksi, explain plan dan index, koneksi Java/Node | Tahap 3: data uji, view laporan, validasi, transaksi, index | `db/04` sampai `db/07` |
| Hari 2, 13.00–17.00 | 24 | Claude Code | Persiapan, lalu **presentasi kelompok 16.00–17.00** | README lengkap, bukti cek |
| Hari 2, 23.59 | mandiri | | Push final, link repo dikumpulkan | Paket serah terima ke backend |

### Repo kelompok

Repo dibuat dari template `odp-it/alp-db-template` lewat tombol **Use this template**. Isinya sudah berupa kerangka:

```text
alp-<nama-kelompok>-db/
├── README.md                 # bagian wajib, diisi bertahap
├── docs/
│   ├── kartu-tema.md         # titik awal entity per tema (bukan jawaban jadi)
│   ├── erd.drawio.png        # Lab sesi 21
│   ├── kamus-data.md         # Lab sesi 21
│   └── review.md             # Lab sesi 21: temuan dari kelompok lain + tanggapan
└── db/
    ├── 00-run-all.sql        # menjalankan semua tahap; aman diulang
    ├── 01-ddl.sql            # Lab sesi 22
    ├── 02-seed.sql           # Lab sesi 22
    ├── 03-test-invalid.sql   # Lab sesi 22
    ├── 04-data-uji.sql       # Lab sesi 23
    ├── 05-laporan.sql        # Lab sesi 23
    ├── 06-transaksi.sql      # Lab sesi 23
    └── 07-index.sql          # Lab sesi 23
```

Satu anggota (driver) membuat repo dan mengundang anggota lain. Semua anggota clone repo dan menjalankan database kelompok di laptop masing-masing. Perubahan masuk lewat satu driver per tahap, anggota lain `git pull`.

### Syarat untuk semua kelompok

1. Tabel pengguna + role (`<awalan>_APP_USERS`), dipakai untuk login di sesi backend. Mulai dari ERD di Lab ini.
2. README repo berisi: masalah dan pengguna, fitur MVP, cara menjalankan, ERD, aturan data penting, peta fitur → tabel → query, laporan, tiga pertanyaan bisnis, bukti cek.
3. Awalan tabel 2–4 huruf per kelompok (mis. `KAS_`), supaya tabel kelompok dikenali.

### Penilaian

Nilai project diberikan **saat presentasi di sesi 24**, berdasarkan hasil yang ditunjukkan di kelas. Repo pukul 23.59 hari 2 hanya untuk serah terima ke backend. Presentasi 5 menit per kelompok plus 3 menit tanya jawab, tanpa slide: README repo menjadi alur bicara dan demo langsung di VS Code. Pergantian kelompok dilakukan saat tanya jawab: kelompok berikutnya menyiapkan laptop selagi kelompok sebelumnya menjawab.

| Komponen | Poin | Yang ditunjukkan |
| --- | --- | --- |
| A. ERD + kamus data | 25 | ERD, skor `lab/cek-erd.py`, entity sesuai fitur MVP, tabel pengguna + role, satu aturan data beserta alasannya |
| B. Database | 35 | `00-run-all.sql` jalan live, skor `cek-lab.sql` sesi 22, satu input salah ditolak |
| C. Laporan + kesiapan backend | 15 | View laporan tampil, peta fitur → tabel → query di README |
| D. Penyampaian | 25 | Alur masalah → data runtut, selesai 5 menit, tanya jawab dijawab dengan data |

Rubrik Lab 100 poin di bagian Lab adalah panduan dan cek mandiri Tahap 1. Skor otomatis dijalankan kelompok sebelum presentasi dan ditempel di README bagian "Bukti cek".

## Jembatan ke Tema Kelompok

Konsep di Demo (Tabungan UMKM) sama dengan yang dibutuhkan ERD kelompok. Pakai tabel ini untuk memetakan ERD kelompok sebelum menggambar.

| Konsep di Demo (Tabungan UMKM) | Perbankan | E-commerce | Logistik |
| --- | --- | --- | --- |
| Entity pusat (banyak tabel lain menunjuk ke sini) | UMKM | Pesanan | Kiriman |
| Relasi 1:N | Akun → transaksi | Pembeli → pesanan | Kiriman → riwayat status |
| N:M lewat tabel penghubung | (tidak wajib) | Pesanan ↔ produk lewat isi pesanan | (tidak wajib) |
| FK boleh kosong | Pengguna admin tanpa UMKM | Pengguna admin tanpa toko atau pembeli | Kiriman belum punya kurir |
| Tabel pengguna + role | `ADMIN`, `PEMILIK`, `STAF` | `ADMIN`, `PENJUAL`, `PEMBELI` | `ADMIN`, `PETUGAS`, `KURIR` |

Tabel pengguna + role bisa dilihat bentuknya di Tantangan tambahan Demo 3 (`APP_USERS`, hanya di ERD). Titik awal entity per tema ada di `docs/kartu-tema.md` di repo kelompok: contoh, bukan jawaban jadi. Entity kelompok diturunkan dari fitur MVP di project brief CP1.

## Struktur Repo

| Folder | Isi |
| --- | --- |
| [`demo-1/`](demo-1/) | Demo 1 · Setup Oracle & `ALP_DEV` |
| [`demo-2/`](demo-2/) | Demo 2 · Baca Kasus Contoh: Entity, Key, Relasi |
| [`demo-3/`](demo-3/) | Demo 3 · Gambar ERD di Draw.io |
| [`demo-4/`](demo-4/) | Demo 4 · Kamus Data |
| [`lab/`](lab/) | Lab · Tahap 1 Project Kelompok: Repo, ERD, Peer Review, Kamus Data |

Setiap folder punya `README.md` berisi langkahnya. Kerjakan berurutan: `demo-1` sampai `demo-4`, lalu `lab`.

## Bantuan

- [TROUBLESHOOTING.md](TROUBLESHOOTING.md): pesan error dan cara memperbaikinya.
- [CHECKLIST.md](CHECKLIST.md): hasil yang harus terlihat dan kriteria selesai.

## Cleanup

Container dan volume **jangan dihapus**: dipakai lagi di sesi 22 dan 23. Setelah selesai, cukup hentikan container supaya RAM lega:

```bash
docker stop oracle-alp
```

Di awal sesi berikutnya: buka Docker Desktop, `docker start oracle-alp`, tunggu `(healthy)` di `docker ps` (±15–40 detik; kalau status `Exited (255)` setelah laptop dimatikan, perintah yang sama cukup), lalu buka koneksi `ALP_DEV @ FREEPDB1`.

Sesi 22 mengubah ERD Tabungan UMKM menjadi tabel sungguhan dengan `CREATE TABLE`, constraint, dan data contoh.
