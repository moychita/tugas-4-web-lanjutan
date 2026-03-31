from fastapi import FastAPI, HTTPException, Header, Depends
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Database simulasi menggunakan Dictionary
fake_users_db = {}
fake_items_db = {}

# Model Data (Pydantic)
class UserRegister(BaseModel):
    username: str
    password: str
    role: str = "user"

class Item(BaseModel):
    id: str
    name: str
    description: Optional[str] = None

# Dependency untuk cek token sederhana
def get_token(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token tidak valid atau tidak ditemukan")
    return authorization.replace("Bearer ", "")

# --- ENDPOINT ---

@app.post("/auth/register", status_code=201)
def register(user: UserRegister):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username sudah terdaftar")
    fake_users_db[user.username] = user
    return {"username": user.username, "message": "Registrasi Berhasil"}

@app.post("/auth/login")
def login(login_data: dict):
    username = login_data.get("username")
    password = login_data.get("password")
    
    user = fake_users_db.get(username)
    if user and user.password == password:
        # Simulasi token: "token-nama-role"
        return {"access_token": f"token-{user.username}-{user.role}", "token_type": "bearer"}
    
    raise HTTPException(status_code=401, detail="Username atau password salah")

@app.post("/items/", status_code=201)
def create_item(item: Item, token: str = Depends(get_token)):
    fake_items_db[item.id] = item
    return item

@app.delete("/admin/delete-all")
def delete_all_data(token: str = Depends(get_token)):
    # Logika RBAC Sederhana: Cek apakah token berakhiran '-admin'
    if not token.endswith("-admin"):
        raise HTTPException(status_code=403, detail="Access Denied! Hanya admin yang boleh mengakses.")
    
    fake_items_db.clear()
    return {"message": "Semua data item berhasil dihapus oleh admin"}