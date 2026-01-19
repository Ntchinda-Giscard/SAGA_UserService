from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum
from .session import Base

class UserRole(str, enum.Enum):
    ADMIN = "admin"
    CUSTOMER = "customer"

class BookingStatus(str, enum.Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, default=UserRole.CUSTOMER)
    created_at = Column(DateTime, default=datetime.utcnow)

    bookings = relationship("Booking", back_populates="user")

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    route_id = Column(Integer, nullable=False)  # Reference to Catalogue Service Route ID
    seat_number = Column(String, nullable=False)
    status = Column(String, default=BookingStatus.PENDING)
    booking_time = Column(DateTime, default=datetime.utcnow)
    travel_date = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="bookings")
