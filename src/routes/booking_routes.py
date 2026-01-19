from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database.session import get_db
from ..services.booking_service import BookingService
from ..schemas.booking_schema import BookingCreate, BookingResponse

# In a real app, this would be derived from the authenticated token
# For this task, we will simulate passing user_id or having a mock auth dependency
from ..services.user_service import UserService

router = APIRouter(
    prefix="/bookings",
    tags=["bookings"]
)

def get_booking_service(db: Session = Depends(get_db)) -> BookingService:
    return BookingService(db)

# Mock Auth Dependency
def get_current_user_id():
    return 1  # Simplified for demonstration

@router.post("/", response_model=BookingResponse, status_code=status.HTTP_201_CREATED)
def create_booking(
    booking_data: BookingCreate,
    service: BookingService = Depends(get_booking_service),
    user_id: int = Depends(get_current_user_id)
):
    """
    Create a new booking for the authenticated user.
    """
    return service.create_booking(user_id, booking_data)

@router.get("/", response_model=List[BookingResponse])
def get_my_bookings(
    service: BookingService = Depends(get_booking_service),
    user_id: int = Depends(get_current_user_id)
):
    """
    Get all bookings for the authenticated user.
    """
    return service.get_user_bookings(user_id)
