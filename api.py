from typing import Optional, Generator
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from database import engine
from models import User

app = FastAPI(title="Company Backend API")

# 1. DEPENDENCY: Ανοίγει ένα Session για κάθε request και το κλείνει στο τέλος
def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


# 2. PYDANTIC SCHEMAS: Ελέγχουν τα δεδομένα που έρχονται/φεύγουν από το API (JSON)
class UserCreate(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None
    phone_number: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    full_name: Optional[str]
    phone_number: Optional[str]
    is_active: bool

    # Επιτρέπει στο Pydantic να διαβάσει απευθείας αντικείμενα SQLAlchemy!
    model_config = {"from_attributes": True}


# 3. ENDPOINT: Φέρε όλους τους χρήστες (GET)
@app.get("/users", response_model=list[UserResponse])
def read_users(db: Session = Depends(get_db)):
    users = db.scalars(select(User)).all()
    return users


# 4. ENDPOINT: Δημιουργία νέου χρήστη με Transaction & Rollback (POST)
@app.post("/users", response_model=UserResponse, status_code=201)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        username=user_data.username,
        email=user_data.email,
        full_name=user_data.full_name,
        phone_number=user_data.phone_number
    )
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)  # Φέρνει από τη βάση το νέο id και created_at
        return new_user
    except IntegrityError:
        # Αν υπάρχει ήδη το username ή το email, ακυρώνουμε καθαρά το transaction!
        db.rollback()
        raise HTTPException(status_code=400, detail="Το username ή το email υπάρχει ήδη!")