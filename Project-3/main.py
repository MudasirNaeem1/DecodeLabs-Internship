from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, EmailStr
from typing import Optional
import sqlite3, os

app = FastAPI(title="Project 3 - Database Integration")
templates = Jinja2Templates(directory="templates")

DB_PATH = "database.db"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    conn = get_db()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            user_id   INTEGER PRIMARY KEY AUTOINCREMENT,
            name      TEXT    NOT NULL,
            email     TEXT    NOT NULL UNIQUE,
            status    TEXT    NOT NULL DEFAULT 'active'
                              CHECK(status IN ('active','inactive')),
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS orders (
            order_id   INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id    INTEGER NOT NULL,
            amount     REAL    NOT NULL CHECK(amount > 0),
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        );
    """)
    # Seed data if empty
    if conn.execute("SELECT COUNT(*) FROM users").fetchone()[0] == 0:
        conn.executescript("""
            INSERT INTO users (name, email, status) VALUES
                ('Alice Khan',  'alice@email.com',  'active'),
                ('Bob Raza',    'bob@email.com',    'active'),
                ('Sara Ahmed',  'sara@email.com',   'inactive');
            INSERT INTO orders (user_id, amount) VALUES
                (1, 42.00), (1, 18.50), (2, 99.99), (3, 7.25);
        """)
    conn.commit()
    conn.close()

init_db()

# ── Pydantic schemas ────────────────────────────────────────────────────────
class UserCreate(BaseModel):
    name: str
    email: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    status: Optional[str] = None

class OrderCreate(BaseModel):
    user_id: int
    amount: float

# ── UI Route ────────────────────────────────────────────────────────────────
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# ── Users CRUD ──────────────────────────────────────────────────────────────
@app.get("/api/users")
def get_users():
    conn = get_db()
    rows = conn.execute("SELECT * FROM users ORDER BY user_id").fetchall()
    conn.close()
    return [dict(r) for r in rows]

@app.post("/api/users", status_code=201)
def create_user(user: UserCreate):
    try:
        conn = get_db()
        cur = conn.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (user.name.strip(), user.email.strip())
        )
        conn.commit()
        new_id = cur.lastrowid
        row = conn.execute("SELECT * FROM users WHERE user_id=?", (new_id,)).fetchone()
        conn.close()
        return dict(row)
    except sqlite3.IntegrityError:
        raise HTTPException(400, "Email already exists (UNIQUE constraint violated)")

@app.put("/api/users/{user_id}")
def update_user(user_id: int, data: UserUpdate):
    conn = get_db()
    user = conn.execute("SELECT * FROM users WHERE user_id=?", (user_id,)).fetchone()
    if not user:
        raise HTTPException(404, "User not found")
    name   = data.name   or user["name"]
    status = data.status or user["status"]
    conn.execute("UPDATE users SET name=?, status=? WHERE user_id=?", (name, status, user_id))
    conn.commit()
    row = conn.execute("SELECT * FROM users WHERE user_id=?", (user_id,)).fetchone()
    conn.close()
    return dict(row)

@app.delete("/api/users/{user_id}")
def delete_user(user_id: int):
    conn = get_db()
    orders = conn.execute("SELECT COUNT(*) FROM orders WHERE user_id=?", (user_id,)).fetchone()[0]
    if orders:
        conn.close()
        raise HTTPException(400, f"Cannot delete: user has {orders} order(s) (FK constraint)")
    result = conn.execute("DELETE FROM users WHERE user_id=?", (user_id,))
    conn.commit()
    conn.close()
    if result.rowcount == 0:
        raise HTTPException(404, "User not found")
    return {"message": "User deleted successfully"}

# ── Orders CRUD ─────────────────────────────────────────────────────────────
@app.get("/api/orders")
def get_orders():
    conn = get_db()
    rows = conn.execute("""
        SELECT o.*, u.name AS user_name
        FROM orders o
        LEFT JOIN users u ON o.user_id = u.user_id
        ORDER BY o.order_id
    """).fetchall()
    conn.close()
    return [dict(r) for r in rows]

@app.post("/api/orders", status_code=201)
def create_order(order: OrderCreate):
    if order.amount <= 0:
        raise HTTPException(400, "Amount must be greater than 0 (CHECK constraint)")
    conn = get_db()
    user = conn.execute("SELECT user_id FROM users WHERE user_id=?", (order.user_id,)).fetchone()
    if not user:
        raise HTTPException(404, "User not found (FK constraint)")
    cur = conn.execute("INSERT INTO orders (user_id, amount) VALUES (?, ?)", (order.user_id, order.amount))
    conn.commit()
    row = conn.execute("""
        SELECT o.*, u.name AS user_name FROM orders o
        LEFT JOIN users u ON o.user_id=u.user_id WHERE o.order_id=?
    """, (cur.lastrowid,)).fetchone()
    conn.close()
    return dict(row)

@app.delete("/api/orders/{order_id}")
def delete_order(order_id: int):
    conn = get_db()
    result = conn.execute("DELETE FROM orders WHERE order_id=?", (order_id,))
    conn.commit()
    conn.close()
    if result.rowcount == 0:
        raise HTTPException(404, "Order not found")
    return {"message": "Order deleted successfully"}

# ── Stats ────────────────────────────────────────────────────────────────────
@app.get("/api/stats")
def get_stats():
    conn = get_db()
    users  = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    orders = conn.execute("SELECT COUNT(*) FROM orders").fetchone()[0]
    total  = conn.execute("SELECT COALESCE(SUM(amount),0) FROM orders").fetchone()[0]
    conn.close()
    return {"users": users, "orders": orders, "total_revenue": round(total, 2)}
