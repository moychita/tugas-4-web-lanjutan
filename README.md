# 🚀 Microservice Testing with FastAPI & Pytest

## 📌 Deskripsi Proyek
Proyek ini merupakan implementasi microservice sederhana menggunakan FastAPI yang dilengkapi dengan automated testing menggunakan pytest.

Fokus utama proyek ini adalah:
- Implementasi endpoint API
- Pengujian otomatis (unit testing)
- Validasi autentikasi dan otorisasi
- Penerapan Role-Based Access Control (RBAC)

## ⚙️ Teknologi yang Digunakan
- Python 3.x  
- FastAPI  
- Pytest  
- HTTPX / TestClient  
- Uvicorn  

## 🧩 Fitur Utama

### 🔐 Autentikasi
- Register user
- Login user (JWT Token)

### 📦 CRUD Operations
- Create item
- Read item

### 🛡️ Role-Based Access Control (RBAC)
- Akses endpoint dibatasi berdasarkan role
- Admin memiliki akses penuh
- User biasa dibatasi (Access Denied)

## 📁 Struktur Project
.
├── main.py
├── test_main.py
├── requirements.txt
└── README.md

## ▶️ Cara Menjalankan Project

### 1. Clone Repository
git clone https://github.com/username/repository-name.git
cd repository-name

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Jalankan Server
uvicorn main:app --reload

Akses API di:
http://127.0.0.1:8000/docs

## 🧪 Menjalankan Pengujian
pytest test_main.py -v

## 🧾 Test Case yang Diimplementasikan
1. Autentikasi (Register & Login)
2. CRUD (Create Item)
3. RBAC (Access Denied)

## 📊 HTTP Status Code
- 200 OK
- 201 Created
- 403 Forbidden

## 🎯 Tujuan Proyek
- Memahami microservices
- Mengimplementasikan automated testing
- Memahami keamanan API

## 👨‍💻 Author
Diana Sang Penunggu Inspiriskiskis
