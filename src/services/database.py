from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set the database URL for SQLAlchemy to connect to a PostgreSQL database
SQLALCHEMY_DATABASE_URL = "postgresql://admin:admin@localhost:5433/db_local"

# Create an engine to establish a connection to the database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session factory using the engine
SessionLocal = sessionmaker(bind=engine)

# Define a base class for declarative models
Base = declarative_base()

# Get a new database session from the session factory. Returns: A new database session.
def get_db_session():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()
