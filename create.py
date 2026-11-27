from sqlalchemy.orm import Session
from database import engine
from models import User

# Το 'with' ανοίγει μια ασφαλή συνεδρία (Session) με τη βάση και την κλείνει αυτόματα στο τέλος
with Session(engine) as session:
    
    # Βήμα Α: Φτιάχνουμε απλά αντικείμενα Python στη μνήμη (δεν έχουν μπει ακόμα στη βάση!)
    user1 = User(
        username="maria_dev", 
        email="maria@company.gr", 
        full_name="Μαρία Παπαδοπούλου"
    )
    user2 = User(
        username="nikos_99", 
        email="nikos@company.gr"
    )
    user3 = User(
        username="eleni_hr", 
        email="eleni@company.gr", 
        full_name="Ελένη Γεωργίου"
    )

    # Βήμα Β: Τα παραδίδουμε στο Session για παρακολούθηση
    session.add(user1)               # Βάζει έναν χρήστη στην ουρά
    session.add_all([user2, user3])  # Βάζει λίστα χρηστών στην ουρά

    # Βήμα Γ: Οριστική αποθήκευση στη βάση!
    # Εδώ το SQLAlchemy γράφει και εκτελεί τις εντολές SQL INSERT
    session.commit()

    print("Επιτυχία! Ο κωδικός (ID) της Μαρίας στη βάση είναι:", user1.id)