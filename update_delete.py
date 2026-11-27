from sqlalchemy import select
from sqlalchemy.orm import Session
from database import engine
from models import User

with Session(engine) as session:
    
    # --- UPDATE ---
    nikos = session.scalar(select(User).where(User.username == "nikos_99"))
    
    if nikos:
        nikos.full_name = "Νίκος Κωνσταντίνου"
        nikos.is_active = False
        session.commit()
        print("Ο Νίκος ενημερώθηκε!")

    # --- DELETE ---
    eleni = session.scalar(select(User).where(User.username == "eleni_hr"))
    
    if eleni:
        session.delete(eleni)
        session.commit()
        print("Η Ελένη διαγράφηκε!")