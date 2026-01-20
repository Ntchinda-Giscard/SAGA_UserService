from fastapi import FastAPI
from .database.session import engine, Base
from .routes import user_routes, booking_routes

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Bus Booking - User Service",
    description="Service for managing users and their bookings",
    version="1.0.0"
)

app.include_router(user_routes.router)
app.include_router(booking_routes.router)

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "UserService"}


