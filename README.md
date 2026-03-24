# Tugas2 - PPL1

## 1. Deskripsi Project

API sederhana untuk manajemen inventori produk skincare.
API ini memungkinkan pengguna untuk:

* Melihat daftar produk skincare
* Menambahkan produk baru

Dibangun menggunakan Flask dan dijalankan dalam container menggunakan Docker.

---

## 2. Dokumentasi API

### Endpoint List

#### GET /products

Mengambil semua data produk

**Response (Success - 200)**

```json
{
  "status": "success",
  "data": [
    {
      "id": 1,
      "name": "Sunscreen SPF 50",
      "brand": "GlowUp",
      "price": 120000
    },
    {
      "id": 2,
      "name": "Moisturizer Ceramide",
      "brand": "Skintific",
      "price": 150000
    }
  ]
}
```

---

#### POST /products

Menambahkan produk baru

**Request Body**

```json
{
  "name": "Toner Brightening",
  "brand": "SomeBrand",
  "price": 90000
}
```

**Response (Success - 201)**

```json
{
  "status": "success",
  "message": "Produk ditambah!"
}
```

---

### Contoh Error Response

```json
{
  "status": "error",
  "message": "Invalid request data"
}
```

---

## 3. Panduan Instalasi (Docker)

### Langkah Menjalankan

```bash
docker-compose up --build
```

Jika berhasil, akan muncul:

```
Running on http://0.0.0.0:5000
```

---

### Akses API

Buka di browser:

```
http://localhost:8000/products
```

---

### Informasi Port

| Tipe          | Port |
| ------------- | ---- |
| Host (Laptop) | 8000 |
| Container     | 5000 |

Mapping:

```
8000:5000
```

---

## 4. Alur Kerja Git

### Branch Strategy

* main → branch utama (production)
* develop → integrasi fitur
* feature/api-skincare → development fitur API

---

### Conventional Commits

Contoh commit:

```bash
git commit -m "feat: implement skincare api with docker and ci-cs workflow"
```

Format:

```
<type>: <description>
```

Contoh type:

* feat → fitur baru
* fix → perbaikan bug
* docs → dokumentasi

---

## 5. Status Automasi (GitHub Actions)

Workflow berada di:

```
.github/workflows/main.yml
```

### Penjelasan

* CI (Continuous Integration): menjalankan proses testing setiap ada push
* CS (Code Scanning): simulasi scanning untuk mendeteksi potensi celah keamanan

---

### Trigger

```
on: [push]
```

---

### Badge Status (Opsional)

```md
![CI Status](https://github.com/username-kamu/nama-repo/actions/workflows/main.yml/badge.svg)
```

---

## Teknologi yang Digunakan

* Python (Flask)
* Docker dan Docker Compose
* Git dan GitHub
* GitHub Actions (CI/CS)
