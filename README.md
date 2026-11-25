# 21 - Database Fundamentals & Oracle Setup

Lab ini menyiapkan Oracle Database di laptop dan merancang data sebelum tabel dibuat. Hasil akhirnya: Oracle jalan di container, user `ALP_DEV` bisa dipakai dari SQL client, ERD dan kamus data kasus contoh Tabungan UMKM, serta ERD ALP tim yang sudah di-review dengan kamus datanya, dinilai dengan rubrik 100 poin.

## Tujuan

1. Menjelaskan tabel, primary key, foreign key, dan relasi 1:1, 1:N, N:M.
2. Menjalankan Oracle Database Free di container dan terhubung dari SQL client.
3. Membuat user `ALP_DEV` sebagai schema kerja ALP.
4. Menggambar ERD kasus contoh dan ERD ALP tim di Draw.io.

## Estimasi Waktu

Format sesi: **4 Demo + 1 Lab**. Di tiap Demo instruktur memperagakan, lalu peserta mengikuti langkah bernomor yang sama dari file di folder ini (di file *starter*, bagian `TODO` sengaja belum lengkap). Demo 1 dan 2 inti sesi: wajib selesai. Demo 3 dan 4 penting. **Lab** adalah tugas tim yang menerapkan semuanya, dinilai dengan rubrik 100 poin dan cek otomatis. Tiap Demo punya **Tantangan tambahan** untuk yang selesai lebih cepat (tidak wajib).

| Bagian | Durasi di kelas (peraga + ikuti) |
| --- | --- |
| Demo 1 · Setup Oracle & `ALP_DEV` | ±55 menit (15 + 40) |
| Demo 2 · Baca kasus contoh: entity, key, relasi | ±20 menit (8 + 12) |
| Demo 3 · Gambar ERD di Draw.io | ±32 menit (12 + 20) |
| Demo 4 · Kamus data | ±18 menit (6 + 12) |
| **Lab** · ERD ALP tim + peer review + kamus data (lanjut setelah kelas) | ±35 menit |
| **Total** | **±160 menit** (+ pembuka 10, konsep 35, penutup 5 = 210) |

## Environment & Tools

Disiapkan sebelum kelas lewat pengumuman persiapan (download image butuh waktu). Versi dikunci: jangan update tool selama kelas.

| Tool | Versi | Catatan |
| --- | --- | --- |
| Docker Desktop (atau Rancher Desktop dengan CLI `docker`, kalau Docker Desktop tidak berlisensi di kantor) | Docker Desktop dengan Docker Engine 29.x | Windows: WSL2 aktif (butuh admin sekali). Semua perintah lab memakai `docker` |
| Image Oracle | `container-registry.oracle.com/database/free:23.26.4.0-lite` | ±1,3 GB download, ±4,5 GB setelah jalan, RAM ±2–2,7 GB |
| VS Code + ekstensi **Oracle SQL Developer for VS Code** | 26.3.x | SQL client |
| VS Code + ekstensi **Draw.io Integration** (Henning Dieterichs) | 1.19.0 | Menggambar ERD di dalam VS Code |

Versi dicek 22 Nov 2026 (Marketplace VS Code). Laptop minimal RAM 8 GB, disk kosong 10 GB, port `1521` tidak dipakai aplikasi lain.

## Struktur Repo

| Folder | Isi |
| --- | --- |
| [`demo-1/`](demo-1/) | Demo 1 · Setup Oracle & `ALP_DEV` |
| [`demo-2/`](demo-2/) | Demo 2 · Baca Kasus Contoh: Entity, Key, Relasi |
| [`demo-3/`](demo-3/) | Demo 3 · Gambar ERD di Draw.io |
| [`demo-4/`](demo-4/) | Demo 4 · Kamus Data |
| [`lab/`](lab/) | Lab · ERD ALP Tim + Peer Review + Kamus Data |

Setiap folder punya `README.md` berisi langkahnya. Kerjakan berurutan: `demo-1` sampai `demo-4`, lalu `lab`.

## Demo dan Lab

Demo 1–4 dikerjakan **individu**. Lab dikerjakan **per tim ALP**.

### Target

| Bagian | Hasil |
| --- | --- |
| Demo 1 | Container `oracle-alp` jalan; login `ALP_DEV` ke `FREEPDB1` berhasil dari SQL client |
| Demo 2 | `demo-2/latihan-baca-erd.md` terisi: 4 entity, 3 relasi |
| Demo 3 | `demo-3/erd-tabungan-umkm.drawio.png`; `lab/cek-erd.py` menampilkan 3 relasi dan `3 dari 3 garis` |
| Demo 4 | `demo-4/latihan-kamus-data.md` terisi dan sama dengan ERD |
| Lab | `erd-alp-<nama-tim>.drawio.png`, `kamus-data-<nama-tim>.md`, `review-untuk-<nama-tim-lain>.md`, skor otomatis dari `lab/cek-erd.py` |

### Studi Kasus

**Tabungan UMKM** adalah aplikasi contoh untuk bank fiktif yang melayani nasabah perorangan dan pelaku UMKM. Database-nya menyimpan cabang, nasabah, rekening, dan transaksi. Schema ini dipakai lagi di sesi 22–23 (SQL) dan sesi REST API berikutnya. Semua data di lab ini data simulasi.

### Kriteria Selesai

- [ ] `docker ps` menampilkan `oracle-alp` dengan status `(healthy)`
- [ ] Query cek di 1.6 mengembalikan `ALP_DEV` dan `FREEPDB1`
- [ ] `demo-2/latihan-baca-erd.md` terisi tanpa `TODO`
- [ ] `demo-3/erd-tabungan-umkm.drawio.png` memenuhi checklist Demo 3
- [ ] `demo-4/latihan-kamus-data.md` terisi dan cocok dengan ERD
- [ ] Lab: ERD tim sudah di-review tim lain, temuannya ditanggapi, dan `lab/cek-erd.py` menampilkan skor otomatis (target minimal 48 dari 80, setara 60%)

## Verifikasi & Expected Result

| Cek | Expected result |
| --- | --- |
| `docker ps` | Satu baris `oracle-alp`, status `Up ... (healthy)`, port `0.0.0.0:1521->1521/tcp` |
| Query 1.6 | 1 baris: `ALP_DEV`, `FREEPDB1`, `freepdb1`; status bar `(Dedicated) ALP_DEV @ FREEPDB1` |
| Demo 2 | 4 entity, 3 relasi 1:N, 3 FK, 5 atribut `UQ` |
| Demo 3 | 4 tabel, 3 relasi 1:N dengan FK di sisi banyak; `lab/cek-erd.py` tanpa kamus: 60 / 80 |
| Demo 4 | `lab/cek-erd.py` dengan kamus: 80 / 80 |
| Lab | `lab/cek-erd.py` menampilkan 8 baris kriteria dan subtotal otomatis maks. 80 |
| Restart | `docker stop oracle-alp` lalu `docker start oracle-alp`: login `ALP_DEV` tetap berhasil, data tidak hilang |

## Troubleshooting

| Masalah / Error | Penyebab | Solusi |
| --- | --- | --- |
| `Bind for 0.0.0.0:1521 failed: port is already allocated` | Port 1521 dipakai container/aplikasi lain | Hentikan container lain yang memakai 1521, atau jalankan dengan `-p 1522:1521` dan isi Port `1522` di SQL client |
| `Conflict. The container name "/oracle-alp" is already in use by container ...` (di Windows PowerShell tampil sebagai teks merah `docker : Error response from daemon: Conflict ...`; di PowerShell 7 tampil bersih tanpa teks merah) | Container dengan nama sama sudah ada | `docker start oracle-alp` untuk memakai yang lama, atau `docker rm -f oracle-alp` lalu ulangi 1.2 (data di volume tetap ada) |
| Container berstatus `Exited (255)` di `docker ps -a` setelah laptop/host dimatikan lalu dihidupkan | Container ikut berhenti bersama host | `docker start oracle-alp`, tunggu `(healthy)` (±15–40 detik pada start ulang) |
| Tombol Run belum aktif, atau `Error: No session associated with the current worksheet` | Folder belum di-Trust, atau file `.sql` belum dipasangi koneksi | Pilih **Trust Folder & Continue**; klik **Attach Connection** dan pilih `ALP_DEV @ FREEPDB1` di tiap file |
| `Unrecognized token in source text` di PowerShell saat menjalankan `docker exec ... @/tmp/01-alp-dev.sql` | Argumen berawalan `@` tanpa tanda kutip dibaca sebagai splatting | Beri tanda kutip: `"@/tmp/01-alp-dev.sql"` |
| `ORA-01017: invalid credential or not authorized; logon denied` | Username atau password salah | Ulangi 1.4 untuk mengganti password `ALP_DEV`, lalu ubah password di koneksi |
| `ORA-12514: Cannot connect to database. Service FREEPDB is not registered with the listener` | Service name salah ketik | Service name harus `FREEPDB1` |
| Koneksi ditolak di port 1521 tepat setelah `run` | Database belum siap | Tunggu status `(healthy)` di `docker ps` |
| `docker: command not found` / `docker` tidak dikenali | Docker Desktop belum terpasang, atau terminal dibuka sebelum instalasi | Tutup dan buka lagi terminal; cek instalasi Docker Desktop |
| `Cannot connect to the Docker daemon` / `error during connect` | Docker Desktop belum dijalankan | Buka Docker Desktop, tunggu status running, ulangi perintah |
| `There are multiple default editors available for the resource.` saat membuka `.drawio.png` | VS Code punya dua editor untuk PNG (gambar biasa dan Draw.io) | Klik **Keep Draw.io (Binary)** |
| File `.drawio.png` terbuka sebagai gambar diam, bukan editor | Terbuka dengan image preview | Command Palette → **View: Reopen Editor With...** → **Draw.io (Binary)** |
| Grup **Entity Relation** tidak muncul setelah **Apply** | Centang belum tersimpan | Klik **+ More Shapes** lagi, pastikan **Entity Relation** tercentang, klik **Apply** |
| SQL client bermasalah, waktu habis | Ekstensi belum terpasang atau error | Sementara pakai SQL*Plus di dalam container: `docker exec -it oracle-alp sqlplus alp_dev@//localhost:1521/FREEPDB1` |
| `ERD tidak bisa dinilai: File kosong (0 byte)` | File `.drawio.png` baru dibuat dan belum disimpan | Gambar lalu **Ctrl+S** / **⌘S**, ulangi `docker cp` |
| `ERD tidak bisa dinilai: PNG ini tidak berisi data diagram` | Yang disalin screenshot atau PNG hasil export tanpa data diagram | Salin file `.drawio.png` yang diedit di VS Code |
| `Tabel 'Table' tidak dihitung` | Judul tabel masih bawaan shape, atau baris belum diisi | Ganti judul dan isi minimal 2 baris kolom |
| Skor atau daftar `Tabel terbaca` tidak berubah setelah file diperbaiki | File belum disimpan, atau `docker cp` gagal sehingga yang dinilai salinan lama | Simpan, jalankan ulang `docker cp` dan pastikan tidak ada pesan error sebelum `docker exec` |
| `Error response from daemon: container ... is not running` saat cek | Container `oracle-alp` mati | `docker start oracle-alp`, ulangi (cek tidak perlu menunggu database siap) |

## Cleanup

Container dan volume **jangan dihapus**: dipakai lagi di sesi 22 dan 23. Setelah kelas, cukup hentikan container supaya RAM lega:

```bash
docker stop oracle-alp
```

Di awal sesi berikutnya: buka Docker Desktop, `docker start oracle-alp`, tunggu `(healthy)` di `docker ps` (±15–40 detik; kalau status `Exited (255)` setelah laptop dimatikan, perintah yang sama cukup), lalu buka koneksi `ALP_DEV @ FREEPDB1`.

Sesi 22 mengubah ERD Tabungan UMKM menjadi tabel sungguhan dengan `CREATE TABLE`, constraint, dan data contoh.
