# 🚀 User Management API

> **DecodeLabs Full Stack Project 2 - Backend API Development**  
> Production-ready REST API built with FastAPI for user registration, authentication, and profile management.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **FastAPI** | Modern async Python web framework |
| **JWT (JSON Web Tokens)** | Stateless authentication |
| **Passlib + bcrypt** | Secure password hashing |
| **Pydantic** | Request/response data validation |
| **Uvicorn** | ASGI server |

---

## 📁 Project Structure

```
user_management_api/
├── main.py              # App entry point, middleware, router registration
├── requirements.txt     # Dependencies
├── core/
│   ├── config.py        # Settings (SECRET_KEY, JWT config)
│   ├── security.py      # Password hashing, JWT creation/decoding
│   └── dependencies.py  # get_current_user dependency
├── models/
│   └── user_store.py    # In-memory user store (simulates a database)
├── schemas/
│   └── user.py          # Pydantic models (request/response shapes)
└── routers/
    ├── auth.py          # POST /auth/register, POST /auth/login
    └── users.py         # GET/PUT/DELETE /users/...
```

---

## ⚡ Setup & Run

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the server
uvicorn main:app --reload
```

> **Server:** `http://127.0.0.1:8000`  
> **Swagger UI (interactive docs):** `http://127.0.0.1:8000/docs`

---

## 📡 API Endpoints

### 🔓 Public - no auth required

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health check |
| `POST` | `/auth/register` | Register a new user |
| `POST` | `/auth/login` | Login and get JWT token |

### 🔒 Protected - send `Authorization: Bearer <token>`

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/users/` | List all users |
| `GET` | `/users/me` | Get your profile |
| `GET` | `/users/{id}` | Get user by ID |
| `PUT` | `/users/me` | Update your name |
| `DELETE` | `/users/me` | Delete your account |

---

## 🧪 Testing the API

> 💡 **Tip:** Use `/docs` for FastAPI's auto-generated Swagger UI - test everything in the browser without curl.

### Step 1 - Register

```bash
curl -X POST http://127.0.0.1:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"name": "Mudasir", "email": "mudasir@test.com", "password": "pass123"}'
```

### Step 2 - Login (get token)

```bash
curl -X POST http://127.0.0.1:8000/auth/login \
  -d "username=mudasir@test.com&password=pass123"
```

### Step 3 - Use the token

```bash
curl http://127.0.0.1:8000/users/me \
  -H "Authorization: Bearer <paste_token_here>"
```

---

## 👤 Default Test User (pre-seeded)

```
Email:    admin@example.com
Password: admin123
```

---

## 📋 HTTP Status Codes

| Code | Status | Meaning |
|---|---|---|
| `200` | OK | Successful GET / PUT |
| `201` | Created | User registered |
| `204` | No Content | User deleted |
| `401` | Unauthorized | Bad or missing token |
| `404` | Not Found | User doesn't exist |
| `409` | Conflict | Email already registered |
| `422` | Unprocessable | Validation failed |

---

## 📄 License

This project is part of the **DecodeLabs Internship Batch 2026** program.

---

*Built with ❤️ using FastAPI*
