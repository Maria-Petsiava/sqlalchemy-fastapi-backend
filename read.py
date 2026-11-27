from sqlalchemy import select
from sqlalchemy.orm import Session
from database import engine
from models import User

with Session(engine) as session:
    
    # --- Περίπτωση 1: Φέρε ΟΛΟΥΣ τους χρήστες ---
    # 1. Χτίζουμε την ερώτηση (δεν εκτελείται ακόμα)
    query_all = select(User)
    
    # 2. Την εκτελούμε στη βάση:
    # Το .scalars() ξεπακετάρει τα αντικείμενα User
    # Το .all() τα μαζεύει σε μια λίστα Python
    all_users = session.scalars(query_all).all()
    
    print("--- Όλοι οι χρήστες ---")
    for u in all_users:
        print(u.id, u.username, u.email)


    # --- Περίπτωση 2: Φέρε ΕΝΑΝ συγκεκριμένο χρήστη ---
    # Χρησιμοποιούμε .where() για να βάλουμε συνθήκη φίλτρου
    query_one = select(User).where(User.username == "maria_dev")
    
    # Το .scalar() (χωρίς 's') φέρνει ΜΟΝΟ 1 αποτέλεσμα (ή None αν δεν βρει τίποτα)
    maria = session.scalar(query_one)
    
    print("\n--- Αναζήτηση Μαρίας ---")
    if maria:
        print("Βρέθηκε:", maria.full_name, "| Active:", maria.is_active)
    else:
        print("Δεν βρέθηκε χρήστης.")