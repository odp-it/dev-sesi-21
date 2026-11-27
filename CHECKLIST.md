# Checklist

[Kembali ke README](README.md)

## Kriteria Selesai

- [ ] `docker ps` menampilkan `oracle-alp` dengan status `(healthy)`
- [ ] Query cek di 1.6 mengembalikan `ALP_DEV` dan `FREEPDB1`
- [ ] `demo-2/latihan-baca-erd.md` terisi tanpa `TODO`
- [ ] `demo-3/erd-tabungan-umkm.drawio.png` memenuhi checklist Demo 3
- [ ] `demo-4/latihan-kamus-data.md` terisi dan cocok dengan ERD
- [ ] Lab: repo kelompok dibuat dari template dan semua anggota sudah clone
- [ ] Lab: `docs/erd.drawio.png` memuat tabel pengguna + role, `docs/kamus-data.md` cocok dengan ERD, `docs/review.md` terisi (temuan dan `Tanggapan:`)
- [ ] Lab: `lab/cek-erd.py` menampilkan skor otomatis minimal 48 dari 80 (setara 60%), dan ketiga file sudah di-push ke repo kelompok
- [ ] Lab: README repo kelompok bagian Masalah dan pengguna serta Fitur MVP terisi (paling lambat malam hari 1)

## Verifikasi & Expected Result

| Cek | Expected result |
| --- | --- |
| `docker ps` | Satu baris `oracle-alp`, status `Up ... (healthy)`, port `0.0.0.0:1521->1521/tcp` |
| Query 1.6 | 1 baris: `ALP_DEV`, `FREEPDB1`, `freepdb1`; status bar `(Dedicated) ALP_DEV @ FREEPDB1` |
| Demo 2 | 4 entity, 3 relasi 1:N, 3 FK, 5 atribut `UQ` |
| Demo 3 | 4 tabel, 3 relasi 1:N dengan FK di sisi banyak; `lab/cek-erd.py` tanpa kamus: 60 / 80 |
| Demo 4 | `lab/cek-erd.py` dengan kamus: 80 / 80 |
| Lab | Repo kelompok memuat `docs/erd.drawio.png`, `docs/kamus-data.md`, `docs/review.md`; `lab/cek-erd.py` menampilkan 8 baris kriteria dan subtotal otomatis, target minimal 48 / 80 |
| Restart | `docker stop oracle-alp` lalu `docker start oracle-alp`: login `ALP_DEV` tetap berhasil, data tidak hilang |
