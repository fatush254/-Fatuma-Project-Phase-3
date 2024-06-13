# lib/debug.py

from db.models import Session

def debug_db():
    session = Session()
    # Perform debug operations
    session.close()

if __name__ == '__main__':
    debug_db()