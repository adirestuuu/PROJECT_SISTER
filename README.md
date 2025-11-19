# Proyek Akhir Mata Kuliah Sistem Terdistribusi

Proyek ini mengimplementasikan sebuah sistem terdistribusi menggunakan arsitektur **Microservices** untuk memfasilitasi pengambilan keputusan (polling) secara real-time.

Status Pengerjaan: **Perencanaan Arsitektur & Proof-of-Concept Skeleton (MVP)**

## 1. STRUKTUR ARSITEKTUR & PEMBAGIAN TUGAS

Kami membagi sistem menjadi **lima layanan (API)** independen yang merepresentasikan **Application Logic (Tier 2)**.

| Layanan (API) | Tujuan Utama | Penanggung Jawab |
| :--- | :--- | :--- |
| **API User** | Otentikasi, Registrasi, dan Profil Pengguna. | **Dimas** |
| **API Poll** | Mengelola data pertanyaan dan pilihan polling. | **Adi** |
| **API Vote** | Merekam suara/data voting yang masuk. | **Salsabila** |
| **API Result** | Menghitung agregasi dan menyajikan hasil akhir polling. | **Putri** |
| **API Sharing** | Layanan utilitas untuk men-generate link sharing. | **Muamanah** |

## 2. KONTRAK API

Ini adalah format Request dan Response yang wajib ditaati oleh semua layanan agar komunikasi antar *microservice* terjamin.

### Layanan: API User (Port: 5001) - [Dimas]

| Endpoint | Method | Deskripsi | JSON Request | JSON Response (Success) |
| :--- | :--- | :--- | :--- | :--- |
| `/login` | `POST` | Autentikasi pengguna | `{ "email": "...", "password": "..." }` | `{ "status": "ok", "user_id": 123, "token": "..." }` |
| `/register` | `POST` | Registrasi pengguna baru | `{ "name": "...", "email": "...", "password": "..." }` | `{ "status": "created", "user_id": 123 }` |

### Layanan: API Poll (Port: 5002) - [Adi]

| Endpoint | Method | Deskripsi | JSON Request | JSON Response (Success) |
| :--- | :--- | :--- | :--- | :--- |
| `/polls` | `POST` | Membuat polling baru | `{ "token": "...", "question": "...", "options": [...] }` | `{ "status": "sukses", "poll_id": 456 }` |
| `/polls` | `GET` | Mendapatkan daftar semua polling aktif | (Tidak ada) | `[ { "id": 456, "question": "..." }, ... ]` |

### Layanan: API Vote (Port: 5003) - [Salsabila]

| Endpoint | Method | Deskripsi | JSON Request | JSON Response (Success) |
| :--- | :--- | :--- | :--- | :--- |
| `/vote` | `POST` | Mengirimkan suara | `{ "user_id": 123, "poll_id": 456, "option": "A" }` | `{ "status": "vote_recorded" }` |

### Layanan: API Result (Port: 5004) - [Putri]

| Endpoint | Method | Deskripsi | JSON Request | JSON Response (Success) |
| :--- | :--- | :--- | :--- | :--- |
| `/results/{poll_id}` | `GET` | Mengambil hasil polling spesifik | (Tidak ada) | `{ "poll_id": 456, "results": { "A": 50, "B": 75 } }` |

### Layanan: API Sharing (Port: 5005) - [Muamanah]

| Endpoint | Method | Deskripsi | JSON Request | JSON Response (Success) |
| :--- | :--- | :--- | :--- | :--- |
| `/share/{poll_id}` | `GET` | Generate link untuk polling | (Tidak ada) | `{ "shareable_link": "pilihmana.com/vote/xyz123" }` |

## 3. Bukti Konsep (PoC)

* File kerangka (`app_*.py`) sudah dibuat di setiap folder API.
* Layanan dapat dijalankan secara independen di port masing-masing (5001-5005).
