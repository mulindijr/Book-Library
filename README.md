## Book Library
### Description
Book Library is a simple command-line application for managing a library of books. Users can add books, view their own books, delete books, delete users, and update user, book, or genre names.Only admins can view all users and their books.
### Features
- `Add a Book:` Users can add a new book to the library by providing details such as user name, book title, and genre.
- `View Books:` Users can view their own books by entering their name. The application displays the book title and genre.
- `View All Users and Their Books:` Admins can view all users and their associated books. This requires admin credentials.
- `Delete a Book:` Users can delete a book by providing their name and the book title.
- `Delete a User:` Admins can delete a user, along with all the books associated with that user. This requires admin credentials.
- `Update User, Book, or Genre Name:` Users can update the name of a user, book, or genre by providing the current name and the new name.
## Getting Started
### Prerequisites
- Python 3.x
- [Pipenv](https://pipenv.pypa.io/)
### Installation
1. Clone the repository:
```
git clone https://github.com/mulindijr/Book-Library.git
```
2. Navigate to the project directory:
```
cd book-library
```
3. Install dependencies:
```
pipenv install
```
### Usage
1. Run the application:
```
pipenv run python cli.py
```
2. Follow the on-screen prompts to perform actions.
### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
### Acknowledgments
- [SQLAlchemy](https://www.sqlalchemy.org/) - Database Toolkit for Python