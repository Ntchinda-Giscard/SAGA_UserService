from datetime import datetime
from enum import Enum
from pydantic import BaseModel

class BookingStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"

class BookingBase(BaseModel):
    route_id: int
    seat_number: str
    travel_date: datetime

class BookingCreate(BookingBase):
    pass

class BookingResponse(BookingBase):
    id: int
    user_id: int
    status: BookingStatus
    booking_time: datetime

    class Config:
        from_attributes = True
