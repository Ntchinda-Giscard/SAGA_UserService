from sqlalchemy.orm import Session
from ..database.models import Booking, User
from ..schemas.booking_schema import BookingCreate
from fastapi import HTTPException, status

class BookingService:
    def __init__(self, db: Session):
        self.db = db

    def create_booking(self, user_id: int, booking_data: BookingCreate):
        # In a real microservice architecture, we would verify route_id with Catalogue Service here.
        # For now, we assume route_id is valid.
        
        new_booking = Booking(
            user_id=user_id,
            route_id=booking_data.route_id,
            seat_number=booking_data.seat_number,
            travel_date=booking_data.travel_date
        )
        self.db.add(new_booking)
        self.db.commit()
        self.db.refresh(new_booking)
        return new_booking

    def get_user_bookings(self, user_id: int):
        return self.db.query(Booking).filter(Booking.user_id == user_id).all()
