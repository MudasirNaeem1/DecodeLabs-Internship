# Project 3 — Database Integration
**Full Stack Development | DecodeLabs 2026**

## Tech Stack
- **Backend:** Python + FastAPI
- **Database:** SQLite (built-in, no setup needed)
- **Frontend:** HTML + Vanilla JS (served by FastAPI)

## Setup & Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the server
uvicorn main:app --reload

# 3. Open browser
http://localhost:8000
```

## Features Implemented

| Feature | Endpoint | SQL |
|---------|----------|-----|
| Create User | POST /api/users | INSERT INTO users |
| Read Users | GET /api/users | SELECT * FROM users |
| Update User | PUT /api/users/{id} | UPDATE users SET |
| Delete User | DELETE /api/users/{id} | DELETE FROM users |
| Create Order | POST /api/orders | INSERT INTO orders |
| Read Orders | GET /api/orders | SELECT + JOIN |
| Delete Order | DELETE /api/orders/{id} | DELETE FROM orders |

## Schema

```sql
TABLE users
  user_id   INTEGER PRIMARY KEY AUTOINCREMENT
  name      TEXT    NOT NULL
  email     TEXT    UNIQUE NOT NULL
  status    TEXT    CHECK(status IN ('active','inactive'))
  created_at DATETIME

TABLE orders
  order_id   INTEGER PRIMARY KEY AUTOINCREMENT
  user_id    INTEGER NOT NULL → REFERENCES users(user_id)
  amount     REAL    CHECK(amount > 0)
  created_at DATETIME
```

## Key Concepts Demonstrated

- **Schema Design** — Primary keys, foreign keys, constraints (UNIQUE, NOT NULL, CHECK)
- **CRUD Operations** — All 4 operations mapped to REST endpoints
- **FK Integrity** — Cannot delete user with existing orders
- **SQL Injection Prevention** — All queries use parameterized placeholders `?`
- **RESTful HTTP Mapping** — POST=CREATE, GET=READ, PUT=UPDATE, DELETE=DELETE

## API Docs
FastAPI auto-generates docs at: `http://localhost:8000/docs`
