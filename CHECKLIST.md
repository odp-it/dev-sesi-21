# Checklist

[Kembali ke README](README.md)

## Kriteria Selesai

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
