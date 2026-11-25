# Latihan Kamus Data · Tabungan UMKM

Demo 4. `BRANCHES` dan `CUSTOMERS` sudah lengkap, jadikan contoh. Di `ACCOUNTS` dan `TRANSACTIONS`, ganti setiap `TODO` di kolom **Tipe Oracle**, **Wajib diisi?**, dan **Constraint** berdasarkan ERD hasil Demo 3 dan `../demo-2/tabungan-umkm.md`.

- **Wajib diisi?**: `YA` (`NOT NULL`) atau `TIDAK`.
- **Constraint**: `PK`, `FK -> NAMA_TABEL`, `UQ`, atau `CK:` diikuti aturannya. Kosongkan (hapus `TODO`) bila kolom tidak punya constraint.
- Nama kolom di tabel ini nama baku kasus contoh (dipakai DDL sesi 22). Kalau ERD memakai nama lain, samakan ERD-nya.

## Tabel: `BRANCHES`

| Kolom | Tipe Oracle | Wajib diisi? | Constraint | Nilai bawaan | Contoh nilai |
| --- | --- | --- | --- | --- | --- |
| `branch_id` | `NUMBER` | YA | PK |  | 1 |
| `branch_code` | `VARCHAR2(20)` | YA | UQ |  | KCP-SIM-01 |
| `branch_name` | `VARCHAR2(100)` | YA |  |  | Cabang Simulasi Satu |
| `city` | `VARCHAR2(50)` | YA |  |  | Jakarta |

## Tabel: `CUSTOMERS`

| Kolom | Tipe Oracle | Wajib diisi? | Constraint | Nilai bawaan | Contoh nilai |
| --- | --- | --- | --- | --- | --- |
| `customer_id` | `NUMBER` | YA | PK |  | 1 |
| `cif_no` | `VARCHAR2(20)` | YA | UQ |  | CIF-SIM-0001 |
| `full_name` | `VARCHAR2(100)` | YA |  |  | Rina Contoh |
| `email` | `VARCHAR2(100)` | YA | UQ |  | rina.contoh@example.com |
| `phone` | `VARCHAR2(20)` | TIDAK |  |  | 0800-0000-0001 |
| `segment` | `VARCHAR2(10)` | YA | CK: segment IN ('INDIVIDU', 'UMKM') |  | UMKM |
| `branch_id` | `NUMBER` | YA | FK -> BRANCHES |  | 1 |
| `created_at` | `TIMESTAMP` | YA |  | SYSTIMESTAMP | 2026-01-05 09:00:00 |

## Tabel: `ACCOUNTS`

| Kolom | Tipe Oracle | Wajib diisi? | Constraint | Nilai bawaan | Contoh nilai |
| --- | --- | --- | --- | --- | --- |
| `account_id` | TODO | TODO | TODO |  | 1 |
| `account_no` | TODO | TODO | TODO |  | SIM-1000001 |
| `customer_id` | TODO | TODO | TODO |  | 1 |
| `product` | TODO | TODO | TODO |  | TABUNGAN |
| `balance` | TODO | TODO | TODO |  | 2500000.00 |
| `status` | TODO | TODO | TODO |  | AKTIF |
| `opened_at` | TODO | TODO | TODO |  | 2026-01-05 09:10:00 |

## Tabel: `TRANSACTIONS`

| Kolom | Tipe Oracle | Wajib diisi? | Constraint | Nilai bawaan | Contoh nilai |
| --- | --- | --- | --- | --- | --- |
| `txn_id` | TODO | TODO | TODO |  | 1 |
| `account_id` | TODO | TODO | TODO |  | 1 |
| `txn_type` | TODO | TODO | TODO |  | SETOR |
| `category` | TODO | TODO | TODO |  | PENJUALAN |
| `amount` | TODO | TODO | TODO |  | 150000.00 |
| `txn_at` | TODO | TODO | TODO |  | 2026-02-01 10:30:00 |
| `description` | TODO | TODO | TODO |  | Setoran penjualan harian |
| `ref_no` | TODO | TODO | TODO |  | REF-SIM-000001 |
