from sqlalchemy.orm import sessionmaker
from models import User, Book, Genre, engine

# Create a Session class linked to the engine
Session = sessionmaker(bind=engine)

