from sqlalchemy.orm import sessionmaker
from models import User, Book, Genre, engine

# Create a Session class linked to the engine
Session = sessionmaker(bind=engine)

def add_book():
     # Prompt user for book details
    user = input('Your name: ')
    title = input('Book title: ')
    genre = input('Book genre: ')

    # Validate input
    if not user or not title or not genre:
        print("Error: Please provide non-empty names for user, title, and genre.")
        return

    # Create a new session
    session = Session()
    # Check if the user exists, if not, add them
    user_obj = session.query(User).filter_by(name=user).first()
    if not user_obj:
        user_obj = User(name=user)
        session.add(user_obj)
        session.commit()

    # Check if the genre exists, if not, add it
    genre_obj = session.query(Genre).filter_by(name=genre).first()
    if not genre_obj:
        genre_obj = Genre(name=genre)
        session.add(genre_obj)
        session.commit()

    # Create a new book and add it to the session
    book = Book(title=title, user=user_obj, genre=genre_obj)
    session.add(book)
    # Commit the changes to the database
    session.commit()
    print(f'Book "{title}" added successfully!')

def view_books():
    # Prompt user for their name
    user = input('Your name: ')

    # Create a new session
    session = Session()

    # Query the database to get the user
    user_obj = session.query(User).filter_by(name=user).first()

    if user_obj:
        # If the user exists, retrieve and display their books
        books = session.query(Book).filter_by(user=user_obj).all()
        if books:
            print(f'Books for {user}:')
            for book in books:
                print(f'- {book.title} (Genre: {book.genre.name})')
        else:
            print(f'No books found for {user}.')
    else:
        print(f'User "{user}" not found.')