# Lab · Tahap 1 Project Kelompok: Repo, ERD, Peer Review, Kamus Data

[Persiapan](../README.md) · [Troubleshooting](../TROUBLESHOOTING.md)

**Skenario.** Kelompok sudah punya tema dan backlog MVP dari sesi 20. Tim lead meminta rancangan data ALP sebelum satu pun tabel dibuat: ERD yang menjawab fitur MVP, sudah di-review kelompok lain, dan dilengkapi kamus data. Sesi 22 menulis `CREATE TABLE` langsung dari dua file itu. Semuanya disimpan di repo kelompok, yang dipakai terus sampai presentasi sesi 24. Rubrik di bawah adalah panduan; nilai project diberikan saat presentasi.

Satu repo per kelompok. Nama kelompok ditulis huruf kecil tanpa spasi (mis. `garuda`), repo bernama `alp-<nama-kelompok>-db`. Pola kerja: **satu driver** memegang laptop yang mengedit ERD dan kamus, anggota lain membaca di layar atau clone repo, lalu `git pull` setelah driver push.

| Langkah | Yang dikerjakan | Menit |
| --- | --- | --- |
| Skenario, contoh bentuk, rubrik | Baca skenario, lihat contoh ERD, baca rubrik di slide | 5 |
| L.0 Repo kelompok | Buat repo dari template, undang anggota, semua clone | 3 |
| L.1 Daftar entity | Dari fitur MVP CP1, tulis 4-6 entity dan fitur yang memakainya, plus tabel user + role | 3 |
| L.2 ERD kelompok | Gambar `docs/erd.drawio.png` dengan langkah 3.1-3.2 | 10 |
| L.3 Peer review | Review ERD kelompok lain, tulis temuan; pemilik menyalin ke `docs/review.md` | 6 |
| L.4 Kamus data | Isi `docs/kamus-data.md`, tulis `Tanggapan:` di `docs/review.md`, perbarui ERD dan kamus | 5 |
| L.5 Cek dan README | Jalankan `cek-erd.py`, push, mulai isi README | 3 |

## L.0 Buat repo kelompok dari template

1. Satu anggota (driver) membuka halaman template `odp-it/alp-db-template` di GitHub, klik **Use this template**, lalu **Create a new repository**.
2. Isi nama repo `alp-<nama-kelompok>-db`. Visibility mengikuti pengumuman instruktur.
3. Buka **Settings** → **Collaborators**, undang semua anggota kelompok (dan akun yang disebut instruktur). Setiap anggota menerima undangan lewat email atau notifikasi GitHub sebelum clone.
4. Semua anggota clone repo ke laptop masing-masing. Cara paling mudah lewat VS Code: Command Palette → **Git: Clone** → **Clone from GitHub**, login GitHub di browser saat diminta (login ini juga dipakai saat `git push`). Lewat terminal:

```bash
git clone https://github.com/<akun-driver>/alp-<nama-kelompok>-db.git
```

Yang harus terlihat: folder `docs/` berisi `kartu-tema.md`, `kamus-data.md`, `review.md`, dan folder `db/` berisi `00` sampai `07`.

## L.1 Daftar entity dari fitur MVP

Buka `docs/kartu-tema.md` untuk titik awal entity tema kelompok (contoh, bukan jawaban). Dari backlog MVP CP1, tulis 4-6 entity beserta fitur MVP yang memakainya. Setiap entity harus terkait minimal satu fitur. Relasi N:M (mis. satu pesanan berisi banyak produk) disiapkan tabel penghubungnya.

**Tabel user + role wajib masuk daftar** (`<awalan>_APP_USERS`): `username` unik, `password_hash`, `role` dengan nilai dibatasi, dan FK ke entity pemilik akun yang boleh kosong. Bentuknya ada di `docs/kartu-tema.md` dan di Tantangan tambahan Demo 3.

## L.2 Gambar ERD kelompok

Buka `docs/erd.drawio.png` dari template. Isinya starter: tabel `AWALAN_APP_USERS` dan kotak catatan langkah. Ganti `AWALAN_` dengan awalan kelompok, lengkapi tabel user, lalu tambahkan entity tema dengan langkah 3.1-3.2 di Demo 3. Hapus kotak catatan setelah selesai. Driver menggambar, anggota lain membaca teks kebutuhan dan membantu menentukan kolom. Pakai nama kolom `snake_case` dan tipe Oracle. ERD dilanjutkan setelah kelas bila belum selesai.

## L.3 Peer review

Instruktur menentukan pasangan melingkar: kelompok 1 mereview kelompok 2, kelompok 2 mereview kelompok 3, dan seterusnya sampai kelompok terakhir mereview kelompok 1. Pemilik ERD menunjukkan `docs/erd.drawio.png` (layar laptop atau kirim file lewat chat kelas).

1. Reviewer memakai `checklist-erd.md` bagian "Lab L.3" (file lab sesi 21, tidak ada di repo kelompok).
2. Reviewer menulis maksimal 3 temuan, satu kalimat per temuan: apa yang diubah dan kenapa.
3. Pemilik ERD menyalin temuan ke `docs/review.md` (isi `Reviewer:` dengan nama kelompok reviewer).

## L.4 Kamus data dan tanggapan

1. Isi `docs/kamus-data.md`: satu bagian per tabel di ERD, dibagi antar anggota. Judul bagian tetap ``## Tabel: `NAMA_TABEL` `` dan nama kolom tabel markdown tidak diubah.
2. Di bawah tiap temuan di `docs/review.md`, tulis `Tanggapan:` (diterapkan atau ditolak, dengan alasan).
3. Perbarui ERD dan kamus sesuai tanggapan.

## L.5 Cek otomatis, push, dan README

Dari terminal di folder repo kelompok, jalankan `cek-erd.py` dari lab sesi 21. Ganti `<folder-cek>` = folder yang berisi `cek-erd.py`: folder `lab` di repo `dev-sesi-21`, atau folder `challenge` di ZIP lab sesi 21:

```bash
docker cp <folder-cek>/cek-erd.py oracle-alp:/tmp/cek-erd.py
docker cp docs/erd.drawio.png oracle-alp:/tmp/erd-cek.drawio.png
docker cp docs/kamus-data.md oracle-alp:/tmp/kamus-cek.md
docker exec oracle-alp python3 /tmp/cek-erd.py /tmp/erd-cek.drawio.png /tmp/kamus-cek.md
```

Kamus belum ada: lewati baris `docker cp` ketiga dan jalankan `docker exec` tanpa argumen terakhir. Cek boleh dijalankan dari laptop anggota mana pun yang punya container `oracle-alp`. Perbaiki sesuai baris **Catatan**, ulangi sampai skor minimal 48 dari 80.

Setelah itu driver push ketiga file, anggota lain `git pull`:

```bash
git add docs
git commit -m "docs: erd, kamus data, dan review tahap 1"
git push
```

Isi juga README repo bagian **Masalah dan pengguna** dan **Fitur MVP** (2-3 kalimat masalah, jenis ide dan produk BNI yang dikaitkan, tabel pengguna dan kebutuhannya, 4-6 fitur dari backlog CP1). Bagian ini boleh selesai malam hari 1.

**Target sebelum sesi 22 (13.00):** `docs/erd.drawio.png`, `docs/kamus-data.md`, `docs/review.md` sudah di repo kelompok dan `cek-erd.py` minimal 48 dari 80. ERD dan kamus ini langsung dipakai untuk `CREATE TABLE` di sesi 22.

## Rubrik Lab (100 poin, panduan Tahap 1)

Rubrik ini membantu kelompok menilai diri sendiri. Nilai project diberikan saat presentasi sesi 24 (tabel penilaian di bagian Project Kelompok).

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
| Cocok dengan fitur MVP | 10 | Instruktur atau kelompok lain | Setiap entity terkait satu fitur MVP; ada tabel user + role; tidak ada kolom berisi banyak nilai; kolom bernilai terbatas punya `CK` di kamus |
| Peer review untuk kelompok lain | 5 | Review | Maksimal 3 temuan, satu kalimat per temuan: apa yang diubah dan kenapa |
| Menanggapi review | 5 | Review | Setiap temuan punya `Tanggapan:` di `docs/review.md`; ERD dan kamus sudah diperbarui sesuai keputusan |
| **Total** | **100** | | |

Target minimal 60 poin. Cek sendiri dengan `cek-erd.py` dan daftar rubrik di atas, lalu push ke repo kelompok.

Cek otomatis hanya menghitung bentuk: tabel, key, garis, tipe, dan kecocokan kamus. Benar tidaknya entity untuk fitur kelompok dinilai manusia.

## Bonus Lab (opsional, maks. +10)

1. (+5) Pilih satu entity yang statusnya berubah-ubah (pesanan, tiket, pengajuan). Tambahkan entity histori status (status lama, status baru, waktu berubah) sebagai relasi 1:N dari entity itu, lengkap di ERD dan kamus.
2. (+5) Tulis tiga pertanyaan bisnis yang harus bisa dijawab data kelompok di README repo bagian **Pertanyaan bisnis** (mis. "berapa total transaksi per kategori bulan ini?"). Untuk tiap pertanyaan, tuliskan urutan tabel yang dilalui dan kolom FK yang dipakai.
