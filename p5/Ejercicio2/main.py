from library import Library
from book import Book
from user import User
from utils import leer_int, crear_menu, generar_id

def main():
    library = Library()
    users = []

    while True:
        menu_options = [
            "Add Book", 
            "Remove Book", 
            "Register User", 
            "Lend Book", 
            "Return Book", 
            "Display All Books", 
            "Exit"
        ]
        choice = crear_menu(menu_options)

        if choice == 1:  # Add Book
            title = input("Enter book title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            book = Book(title, author, isbn)
            library.add_book(book)
            print(f"Book '{title}' added to the library.")
        
        elif choice == 2:  # Remove Book
            isbn = input("Enter ISBN of the book to remove: ")
            library.remove_book(isbn)
        
        elif choice == 3:  # Register User
            name = input("Enter user name: ")
            user_id = generar_id()
            user = User(name, user_id)
            users.append(user)
            print(f"User '{name}' registered with ID {user_id}.")
        
        elif choice == 4:  # Lend Book
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to lend: ")
            user = next((u for u in users if u.user_id == user_id), None)
            if user:
                library.lend_book(isbn)
                user.borrowed_books.append(isbn)
            else:
                print("User not found.")
        
        elif choice == 5:  # Return Book
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to return: ")
            user = next((u for u in users if u.user_id == user_id), None)
            if user:
                if isbn in user.borrowed_books:
                    library.return_book(isbn)
                    user.borrowed_books.remove(isbn)  # Ahora solo se elimina si el ISBN está en la lista
                    print(f"The book with ISBN {isbn} has been successfully returned.")
                else:
                    print(f"The book with ISBN {isbn} was not borrowed by this user.")
            else:
                print("User not found.")
        
        elif choice == 6:  # Display All Books
            library.display_books()
        
        elif choice == 7:  # Exit
            break

if __name__ == "__main__":
    main()
