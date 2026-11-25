# Checklist ERD

## Demo 3 · ERD Tabungan UMKM

- [ ] Ada 4 entity, satu untuk setiap kata benda utama di kebutuhan.
- [ ] Nama entity dan atribut konsisten: huruf besar untuk tabel, `snake_case` untuk kolom.
- [ ] Setiap entity punya satu primary key (`PK`) berupa ID angka.
- [ ] Atribut yang harus unik ditandai (`UQ`): kode cabang, nomor CIF, email, nomor rekening, nomor referensi.
- [ ] Setiap atribut punya tipe data Oracle (`NUMBER`, `NUMBER(15,2)` untuk uang, `VARCHAR2(n)`, `TIMESTAMP`).
- [ ] Setiap relasi digambar dengan crow's foot, sisi "satu" dan sisi "banyak" jelas.
- [ ] Foreign key (`FK`) ada di tabel sisi "banyak" dan menunjuk PK tabel sisi "satu".
- [ ] Nilai yang dibatasi (segmen, produk, status, jenis, kategori) dicatat di samping atribut.
- [ ] Tidak ada data yang diulang di dua tabel (mis. nama nasabah tidak disimpan lagi di tabel transaksi).

## Lab L.3 · Peer review ERD tim lain

- [ ] Setiap entity bisa dikaitkan ke satu fitur MVP di backlog tim.
- [ ] Setiap entity punya PK; FK di sisi "banyak".
- [ ] Relasi N:M (kalau ada) dipecah dengan tabel penghubung.
- [ ] Tipe data uang dan tanggal masuk akal.
- [ ] Tidak ada kolom yang menyimpan banyak nilai sekaligus (mis. "daftar_produk" berisi teks dipisah koma).

Tulis maksimal 3 temuan, masing-masing satu kalimat: apa yang perlu diubah dan kenapa.
