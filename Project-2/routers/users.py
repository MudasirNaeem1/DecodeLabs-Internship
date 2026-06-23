from fastapi import APIRouter, HTTPException, Depends, status
from schemas.user import UserPublic, UserUpdate, UserInDB
from models.user_store import get_all_users, get_user_by_id, update_user, delete_user
from core.dependencies import get_current_user

router = APIRouter()

@router.get("/", response_model=list[UserPublic], summary="List all users (protected)")
def list_users(current_user: UserInDB = Depends(get_current_user)):
    """
    Returns all registered users.
    Requires a valid JWT token in the Authorization header.
    """
    users = get_all_users()
    return [UserPublic(id=u.id, name=u.name, email=u.email, is_active=u.is_active) for u in users]

@router.get("/me", response_model=UserPublic, summary="Get your own profile")
def get_my_profile(current_user: UserInDB = Depends(get_current_user)):
    """Returns the profile of the currently authenticated user."""
    return UserPublic(
        id=current_user.id,
        name=current_user.name,
        email=current_user.email,
        is_active=current_user.is_active
    )

@router.get("/{user_id}", response_model=UserPublic, summary="Get user by ID (protected)")
def get_user(user_id: int, current_user: UserInDB = Depends(get_current_user)):
    """Fetch a specific user by their ID."""
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    return UserPublic(id=user.id, name=user.name, email=user.email, is_active=user.is_active)

@router.put("/me", response_model=UserPublic, summary="Update your profile")
def update_my_profile(update_data: UserUpdate, current_user: UserInDB = Depends(get_current_user)):
    """Update the name of the currently authenticated user."""
    updated = update_user(email=current_user.email, name=update_data.name)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    return UserPublic(id=updated.id, name=updated.name, email=updated.email, is_active=updated.is_active)

@router.delete("/me", status_code=status.HTTP_204_NO_CONTENT, summary="Delete your account")
def delete_my_account(current_user: UserInDB = Depends(get_current_user)):
    """Permanently deletes the authenticated user's account."""
    success = delete_user(current_user.email)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
