# User Management API
**DecodeLabs Full Stack Project 2 — Backend API Development**

A production-ready REST API built with FastAPI for user registration, authentication, and profile management.

## Tech Stack
- **FastAPI** — modern Python web framework
- **JWT (JSON Web Tokens)** — stateless authentication
- **Passlib + bcrypt** — secure password hashing
- **Pydantic** — data validation and schemas
- **Uvicorn** — ASGI server

## Project Structure
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

## Setup & Run

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the server
uvicorn main:app --reload

# Server starts at: http://127.0.0.1:8000
# Interactive docs:  http://127.0.0.1:8000/docs
```

## API Endpoints

### Public (no auth required)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Login and get JWT token |

### Protected (send `Authorization: Bearer <token>`)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/users/` | List all users |
| GET | `/users/me` | Get your profile |
| GET | `/users/{id}` | Get user by ID |
| PUT | `/users/me` | Update your name |
| DELETE | `/users/me` | Delete your account |

## Testing the API

**Step 1 — Register:**
```bash
curl -X POST http://127.0.0.1:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"name": "Mudasir", "email": "mudasir@test.com", "password": "pass123"}'
```

**Step 2 — Login (get token):**
```bash
curl -X POST http://127.0.0.1:8000/auth/login \
  -d "username=mudasir@test.com&password=pass123"
```

**Step 3 — Use the token:**
```bash
curl http://127.0.0.1:8000/users/me \
  -H "Authorization: Bearer <paste_token_here>"
```

**Or just use `/docs`** — FastAPI auto-generates a Swagger UI where you can test everything in the browser.

## Default Test User (pre-seeded)
```
Email:    admin@example.com
Password: admin123
```

## HTTP Status Codes Used
| Code | Meaning |
|------|---------|
| 200 | OK — successful GET/PUT |
| 201 | Created — user registered |
| 204 | No Content — user deleted |
| 401 | Unauthorized — bad/missing token |
| 404 | Not Found — user doesn't exist |
| 409 | Conflict — email already registered |
| 422 | Unprocessable — validation failed |
