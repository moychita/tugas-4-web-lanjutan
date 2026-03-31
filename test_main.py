import pytest
from fastapi.testclient import TestClient
from main import app  # Pastikan mengarah ke file main.py

client = TestClient(app)

# Data testing
test_user = {"username": "dianicoba", "password": "ahhay11", "role": "user"}
test_item = {"id": "101", "name": "Modul FastAPI", "description": "Materi Tugas"}

# Variabel global untuk menyimpan token hasil login
token_storage = {}

def test_register_flow():
    """Test alur registrasi user baru"""
    response = client.post("/auth/register", json=test_user)
    assert response.status_code == 201
    assert response.json()["username"] == test_user["username"]

def test_login_flow():
    """Test alur login untuk mendapatkan token"""
    response = client.post("/auth/login", json={
        "username": test_user["username"], 
        "password": test_user["password"]
    })
    assert response.status_code == 200
    # Simpan token ke dalam storage untuk dipakai test selanjutnya
    token_storage["user_token"] = response.json()["access_token"]

def test_create_item_with_auth():
    """Test buat item menggunakan token yang sudah didapat"""
    headers = {"Authorization": f"Bearer {token_storage['user_token']}"}
    response = client.post("/items/", json=test_item, headers=headers)
    assert response.status_code == 201
    assert response.json()["id"] == test_item["id"]

def test_rbac_user_cannot_delete_all():
    """Test User biasa (bukan admin) dilarang menghapus semua data (403)"""
    headers = {"Authorization": f"Bearer {token_storage['user_token']}"}
    response = client.delete("/admin/delete-all", headers=headers)
    
    assert response.status_code == 403
    assert response.json()["detail"] == "Access Denied! Hanya admin yang boleh mengakses."