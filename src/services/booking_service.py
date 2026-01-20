from sqlalchemy.orm import Session
from ..database.models import Booking, User
from ..schemas.booking_schema import BookingCreate
from fastapi import HTTPException, status

class BookingService:
    def __init__(self, db: Session):
        self.db = db

    def create_booking(self, user_id: int, booking_data: BookingCreate):
        # Verify route_id with Catalogue Service
        from ..clients.catalogue_client import CatalogueClient
        catalogue_client = CatalogueClient()
        route = catalogue_client.get_route(booking_data.route_id)
        
        if not route:
             raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Route ID")

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

    def update_booking_status(self, booking_id: int, status: str):
        booking = self.db.query(Booking).filter(Booking.id == booking_id).first()
        if booking:
            booking.status = status
            self.db.commit()
            self.db.refresh(booking)
        return booking

    def get_user_bookings(self, user_id: int):
        return self.db.query(Booking).filter(Booking.user_id == user_id).all()
