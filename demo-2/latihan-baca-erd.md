# Latihan Baca Kasus · Tabungan UMKM

Demo 2. Sumber: `tabungan-umkm.md`. Ganti setiap `TODO`. Baris `BRANCHES` dan satu relasi sudah diisi sebagai contoh.

## A. Entity dan key

Nama tabel huruf besar, nama kolom `snake_case`. Primary key memakai ID angka (surrogate key).

| Entity | Primary key | Atribut yang harus unik (`UQ`) | Foreign key (menunjuk tabel) | Nilai yang dibatasi atau aturan angka |
| --- | --- | --- | --- | --- |
| `BRANCHES` | `branch_id` | `branch_code` | (tidak ada) | (tidak ada) |
| TODO | TODO | TODO | TODO | TODO |
| TODO | TODO | TODO | TODO | TODO |
| TODO | TODO | TODO | TODO | TODO |

## B. Relasi

Satu baris per relasi: kalimat bisnis, bentuk relasi, dan letak foreign key.

| Kalimat | Relasi | Foreign key ada di |
| --- | --- | --- |
| Satu cabang punya banyak nasabah | `BRANCHES 1:N CUSTOMERS` | `CUSTOMERS.branch_id` |
| TODO | TODO | TODO |
| TODO | TODO | TODO |

## C. Simbol crow's foot

| Simbol di Draw.io | Dibaca |
| --- | --- |
| `ERmandOne` | TODO |
| `ERzeroToOne` | TODO |
| `ERoneToMany` | TODO |
| `ERzeroToMany` | TODO |

## Cek mandiri

- Jumlah entity: 4. Jumlah relasi 1:N: 3. Jumlah foreign key: 3.
- Atribut `UQ` di seluruh kasus: 5.
- Kolom dengan daftar nilai: 5. Aturan angka: 2.
