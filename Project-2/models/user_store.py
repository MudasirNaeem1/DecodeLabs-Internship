"""
In-memory user store (simulates a database).
For this internship project, we skip real DB setup and use a Python dict.
In production you'd swap this for SQLAlchemy + PostgreSQL.
"""
from typing import Optional
from schemas.user import UserInDB
from core.security import hash_password

# Seed one default user for testing
_users: dict[str, UserInDB] = {
    "admin@example.com": UserInDB(
        id=1,
        name="Admin User",
        email="admin@example.com",
        hashed_password=hash_password("admin123"),
        is_active=True,
    )
}
_next_id = 2

def get_user_by_email(email: str) -> Optional[UserInDB]:
    return _users.get(email)

def get_user_by_id(user_id: int) -> Optional[UserInDB]:
    for user in _users.values():
        if user.id == user_id:
            return user
    return None

def get_all_users() -> list[UserInDB]:
    return list(_users.values())

def create_user(name: str, email: str, password: str) -> UserInDB:
    global _next_id
    user = UserInDB(
        id=_next_id,
        name=name,
        email=email,
        hashed_password=hash_password(password),
        is_active=True,
    )
    _users[email] = user
    _next_id += 1
    return user

def update_user(email: str, name: Optional[str] = None) -> Optional[UserInDB]:
    user = _users.get(email)
    if not user:
        return None
    if name:
        user.name = name
    return user

def delete_user(email: str) -> bool:
    if email in _users:
        del _users[email]
        return True
    return False
