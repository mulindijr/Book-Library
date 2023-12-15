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

def authenticate_admin(username, password):
    # Simple authentication function
    return username == 'Mulindi' and password == '1234'

def view_all_data():
    # Prompt admin for credentials
    admin_username_input = input('Admin username: ')
    admin_password_input = input('Admin password: ')

    # Check admin credentials
    if authenticate_admin(admin_username_input, admin_password_input):
        # If authenticated, create a session and retrieve all users
        session = Session()
        users = session.query(User).all()
        print('\n ==== Users and their Books ====')
        if users:
            for user in users:
                print(f'\nUser: {user.name}')
                # For each user, retrieve and display their books
                books = session.query(Book).filter_by(user=user).all()
                if books:
                    print('Books:')
                    for book in books:
                        print(f'- {book.title} (Genre: {book.genre.name})')
                else:
                    print('No books found for this user.')
        else:
            print('No users found.')
    else:
        print('Access denied. Invalid admin credentials.')

def delete_book():
    # Prompt user for details
    user = input('Your name: ')
    title = input('Book title: ')

    # Create a new session
    session = Session()
    # Query the user in the database
    user_obj = session.query(User).filter_by(name=user).first()
    if user_obj:
        # If the user exists, query the book and delete it
        book = session.query(Book).filter_by(user=user_obj, title=title).first()
        if book:
            session.delete(book)
            session.commit()
            print(f'Book "{title}" deleted successfully!')

            # Check if the user has no more books, then delete the user
            remaining_books = session.query(Book).filter_by(user=user_obj).count()
            if remaining_books == 0:
                session.delete(user_obj)
                session.commit()
                print(f'User "{user}" deleted since there are no more books.')
        else:
            print(f'Book "{title}" not found for {user}.')
    else:
        print(f'User "{user}" not found.')

def delete_user():
    # Prompt to delete user
    user = input('User name: ')

    # Create a new session
    session = Session()
     # Query the user in the database
    user_obj = session.query(User).filter_by(name=user).first()
    if user_obj:
        # If the user exists, delete all books associated with the user
        session.query(Book).filter_by(user=user_obj).delete()

        # Delete the user
        session.delete(user_obj)
        session.commit()
        print(f'User "{user}" and associated books deleted successfully!')
    else:
        print(f'User "{user}" not found.')

def update_name(entity_type):
    # Prompt user for details
    entity_name = input(f'Enter the {entity_type} name you want to update: ')
    new_name = input(f'Enter the new name for {entity_type}: ')

    # Check if the new name is provided
    if not new_name:
        print(f"Error: The {entity_type} name cannot be empty.")
        return

     # Create a new session
    session = Session()

    # Query the entity in the database based on the type
    if entity_type == 'user':
        entity = session.query(User).filter_by(name=entity_name).first()
    elif entity_type == 'book':
        entity = session.query(Book).filter_by(title=entity_name).first()
    elif entity_type == 'genre':
        entity = session.query(Genre).filter_by(name=entity_name).first()
    else:
        print('Invalid entity type.')
        return

    # If the entity is found, update its name and commit changes
    if entity:
        if entity_type == 'user' or entity_type == 'genre':
            entity.name = new_name
        elif entity_type == 'book':
            entity.title = new_name

        session.commit()
        print(f'{entity_type.capitalize()} name updated successfully!')
    else:
        print(f'{entity_type.capitalize()} "{entity_name}" not found.')


if __name__ == '__main__':
    print("\n======WELCOME TO BOOK LIBRARY======")
    while True:
        print('\nChoose action:')
        print('1. Add a book')
        print('2. View books')
        print('3. View all the users and their books')
        print('4. Delete a book')
        print('5. Delete a user')
        print('6. Update user, book, or genre name')
        print('7. Exit')

        # Prompt user for choice
        choice = input('Enter the number corresponding to the action: ')

        # Execute the chosen action
        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            view_all_data()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            delete_user()
        elif choice == '6':
            print('Choose entity type to update:')
            print('1. User')
            print('2. Book')
            print('3. Genre')
            entity_choice = input('Enter the number corresponding to the entity type: ')

            # Validate and execute the update
            if entity_choice == '1':
                entity_type = 'user'
            elif entity_choice == '2':
                entity_type = 'book'
            elif entity_choice == '3':
                entity_type = 'genre'
            else:
                print('Invalid entity type.')
                continue

            update_name(entity_type)
        elif choice == '7':
            print('Exiting the program.')
            break
        else:
            print('Invalid choice. Please try again.')