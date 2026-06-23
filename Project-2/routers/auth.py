from fastapi import APIRouter, HTTPException, status
from schemas.user import UserRegister, UserPublic, Token
from models.user_store import get_user_by_email, create_user
from core.security import verify_password, create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends

router = APIRouter()

@router.post("/register", response_model=UserPublic, status_code=status.HTTP_201_CREATED,
             summary="Register a new user")
def register(user_data: UserRegister):
    """
    Register a new user with name, email, and password.
    - Email must be unique.
    - Password must be at least 6 characters.
    """
    existing = get_user_by_email(user_data.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with this email already exists."
        )
    user = create_user(
        name=user_data.name,
        email=user_data.email,
        password=user_data.password,
    )
    return UserPublic(id=user.id, name=user.name, email=user.email, is_active=user.is_active)

@router.post("/login", response_model=Token, summary="Login and get access token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Login with email (as username) and password.
    Returns a JWT bearer token to use in protected endpoints.
    """
    user = get_user_by_email(form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = create_access_token(data={"sub": user.email})
    return Token(access_token=token)
