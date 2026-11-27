from database import engine
from models import Base, User, Task

Base.metadata.create_all(engine)
print("Η βάση και οι πίνακες δημιουργήθηκαν με επιτυχία!")