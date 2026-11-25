# Kebutuhan Data · Tabungan UMKM

Aplikasi contoh untuk bank fiktif. Semua nama dan angka adalah data simulasi.

1. Bank punya beberapa **cabang**. Setiap cabang punya kode cabang yang unik (contoh `KCP-SIM-01`), nama cabang, dan kota.
2. Setiap **nasabah** terdaftar di satu cabang. Nasabah punya nomor CIF yang unik (contoh `CIF-SIM-0001`), nama lengkap, email yang unik, nomor telepon, segmen (`INDIVIDU` atau `UMKM`), dan tanggal terdaftar.
3. Satu nasabah bisa punya lebih dari satu **rekening**. Rekening punya nomor rekening yang unik (contoh `SIM-1000001`), produk (`TABUNGAN` atau `GIRO`), saldo yang tidak boleh negatif, status (`AKTIF`, `DIBLOKIR`, atau `DITUTUP`), dan tanggal dibuka.
4. Setiap setoran, penarikan, dan transfer dicatat sebagai **transaksi** pada satu rekening. Transaksi punya jenis (`SETOR`, `TARIK`, `TRANSFER_MASUK`, `TRANSFER_KELUAR`), kategori untuk laporan keuangan UMKM (`PENJUALAN`, `BAHAN_BAKU`, `OPERASIONAL`, `GAJI`, `TRANSFER`, `LAINNYA`), nominal lebih dari nol, waktu transaksi, keterangan, dan nomor referensi yang unik (contoh `REF-SIM-000001`).
5. Laporan yang nanti dibutuhkan: saldo per cabang, mutasi per rekening per bulan, nasabah yang belum pernah bertransaksi, dan arus kas UMKM per kategori per bulan.
