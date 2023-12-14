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

