import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.models.book import book
from src.db.db_conn import SessionLocal

def create_tables():
    session = SessionLocal()
    book.__table__.create(bind=session.get_bind(), checkfirst=True)
    session.close()

if __name__ == "__main__":
    create_tables()