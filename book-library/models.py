from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# User model representing the 'users' table
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)

    # Relationship with the 'Book' model, back_populates establishes bidirectional relationship
    books = relationship('Book', back_populates='user')

# Book model representing the 'books' table
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='books') # Relationship back to the 'User' model
    genre_id = Column(Integer, ForeignKey('genres.id')) # Foreign key relationship with the 'Genre' model
    genre = relationship('Genre', back_populates='books') # Relationship back to the 'Genre' model

# Genre model representing the 'genres' table
class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Relationship with the 'Book' model, back_populates establishes bidirectional relationship
    books = relationship('Book', back_populates='genre')

# Initialize the database engine
engine = create_engine('sqlite:///library.db')
# Create the tables defined by the models in the database
Base.metadata.create_all(engine)