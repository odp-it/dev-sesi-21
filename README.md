# 21 - Database Fundamentals & Oracle Setup

Lab ini menyiapkan Oracle Database di laptop dan merancang data sebelum tabel dibuat. Hasil akhirnya: Oracle jalan di container, user `ALP_DEV` bisa dipakai dari SQL client, ERD dan kamus data kasus contoh Tabungan UMKM, serta ERD ALP tim yang sudah di-review dengan kamus datanya, dinilai dengan rubrik 100 poin.

## Environment & Tools

Siapkan sebelum mulai (download image butuh waktu). Versi dikunci: jangan update tool di tengah pengerjaan.

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

## Studi Kasus

**Tabungan UMKM** adalah aplikasi contoh untuk bank fiktif yang melayani nasabah perorangan dan pelaku UMKM. Database-nya menyimpan cabang, nasabah, rekening, dan transaksi. Schema ini dipakai lagi di sesi 22–23 (SQL) dan sesi REST API berikutnya. Semua data di lab ini data simulasi.

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
