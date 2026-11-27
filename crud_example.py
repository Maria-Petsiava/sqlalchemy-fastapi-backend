from sqlalchemy.orm import Session
from database import engine
from models import User

# Ανοίγουμε ένα Session με 'with' ώστε να κλείσει αυτόματα και με ασφάλεια στο τέλος
with Session(engine) as session:
    # 1. Δημιουργούμε αντικείμενα Python (δεν έχουν μπει ακόμα στη βάση!)
    user1 = User(username="maria_dev", email="maria@company.gr", full_name="Μαρία Παπαδοπούλου")
    user2 = User(username="nikos_99", email="nikos@company.gr")
    user3 = User(username="eleni_hr", email="eleni@company.gr", full_name="Ελένη Γεωργίου")

    # 2. Τα βάζουμε στο "καλάθι" (Session)
    session.add(user1)                  # Προσθήκη ενός
    session.add_all([user2, user3])     # Προσθήκη πολλών μαζί

    # 3. Οριστική αποθήκευση στη βάση (εκτελείται η SQL INSERT)
    session.commit()
    print("Οι χρήστες αποθηκεύτηκαν!")