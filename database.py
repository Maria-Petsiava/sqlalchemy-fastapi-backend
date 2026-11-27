from sqlalchemy import create_engine
from pathlib import Path

# Βρίσκουμε τον ακριβή φάκελο στον οποίο βρίσκεται το αρχείο database.py (δηλαδή το sqlalchemy_course)
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "company.db"

# Σύνδεση με τοπική βάση SQLite (θα δημιουργηθεί ένα αρχείο company.db)
# Το echo=True εκτυπώνει στην κονσόλα τις εντολές SQL που τρέχουν από πίσω (τέλειο για εκπαίδευση!)
engine = create_engine(f"sqlite:///{DB_PATH}", echo=True)