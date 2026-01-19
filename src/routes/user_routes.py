from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database.session import get_db
from ..services.user_service import UserService
from ..schemas.user_schema import UserCreate, UserResponse, UserLogin

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

def get_user_service(db: Session = Depends(get_db)) -> UserService:
    return UserService(db)

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(
    user_data: UserCreate, 
    service: UserService = Depends(get_user_service)
):
    """
    Register a new user with the system.
    """
    return service.create_user(user_data)

@router.post("/login")
def login(
    login_data: UserLogin,
    service: UserService = Depends(get_user_service)
):
    """
    Authenticate a user.
    """
    user = service.authenticate_user(login_data.email, login_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # in a real app, return JWT token here
    return {"message": "Login successful", "user_id": user.id, "role": user.role}
