# Demo 2 · Baca Kasus Contoh: Entity, Key, Relasi

[Persiapan](../README.md) · [Troubleshooting](../TROUBLESHOOTING.md)

Isi `latihan-baca-erd.md`: entity, key, dan relasi dari teks kebutuhan. Bagian ini tanpa database.

## 2.1 Baca kebutuhan

Buka `tabungan-umkm.md`. Tandai kata benda yang menjadi entity, keterangan yang menjadi atribut, dan kata seperti "unik" atau "tidak boleh negatif" yang menjadi constraint.

## 2.2 Isi tabel entity dan key

Buka `latihan-baca-erd.md` bagian A. Baris `BRANCHES` sudah diisi sebagai contoh. Lengkapi tiga entity lain: primary key, atribut `UQ`, foreign key beserta tabel yang ditunjuk, dan nilai yang dibatasi.

## 2.3 Isi relasi dan simbol

Lengkapi bagian B (dua relasi) dan bagian C (cara membaca empat simbol crow's foot), lalu cocokkan jumlahnya dengan **Cek mandiri** di bawah file.

Yang harus terlihat: tidak ada `TODO` tersisa, 4 entity, 3 relasi 1:N, 3 foreign key, 5 atribut `UQ`, 5 kolom berdaftar nilai, 2 aturan angka.

## Tantangan tambahan Demo 2 (opsional)

Kebutuhan nomor 5 menyebut empat laporan. Untuk tiap laporan, tulis urutan tabel yang harus dilalui (tabel A lewat tabel B ke tabel C) dan kolom FK yang dipakai. Laporan yang tidak punya jalur berarti rancangan kurang satu entity atau relasi.
