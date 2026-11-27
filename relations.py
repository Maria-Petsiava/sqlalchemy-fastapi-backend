from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload
from database import engine
from models import User, Task

# 1. Προσθήκη εργασιών στη Μαρία
with Session(engine) as session:
    maria = session.scalar(select(User).where(User.username == "maria_dev"))

    if maria:
        # Περνάμε απευθείας το αντικείμενο maria στο owner (όχι το id!)
        task1 = Task(title="Σύνδεση με PostgreSQL", description="Ρύθμιση server", owner=maria)
        task2 = Task(title="Έλεγχος κώδικα", owner=maria)

        session.add_all([task1, task2])
        session.commit()
        print("Οι εργασίες αποθηκεύτηκαν!")

# 2. Ανάγνωση χρηστών μαζί με τις εργασίες τους
with Session(engine) as session:
    stmt = select(User).options(selectinload(User.tasks))
    users = session.scalars(stmt).all()

    for user in users:
        print(f"Χρήστης: {user.username} -> Εργασίες: {len(user.tasks)}")
        for t in user.tasks:
            print(f"   - {t.title} (Done: {t.is_completed})")