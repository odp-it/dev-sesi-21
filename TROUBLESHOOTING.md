# Troubleshooting

[Kembali ke README](README.md)

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
| `Error response from daemon: container ... is not running` saat cek | Container `oracle-alp` mati | `docker start oracle-alp`, ulangi (cek bisa jalan tanpa menunggu database siap) |
