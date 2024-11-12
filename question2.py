# Problem Statement: You are maintaining a library system where each book is stored 
# as a tuple within a list. Your task is to update this system by adding new books 
# and ensuring no duplicates.

# - Add functionality to insert new books into `library`. 
# Ensure that adding a duplicate book is handled appropriately.

def display_library(library):
    for book in library:
        print(f"Title: {book[0]}, Author: {book[1]}")

def search_by_title(library):
    title = input("Enter book title to search:  ")
    found = False
    for book in library:
        if book[0].lower() == title.lower():
            print(f"Title: {book[0]}, Author: {book[1]}")
            found = True
            break
    if not found:
        print("Book not found.")

def add_title(library):
    new_title = input("Enter the title you would like to add:   ")
    new_author = input("Enter the name of the book's author:   ")
    added_book = (new_title, new_author)
    if added_book not in library:
        library.append(added_book)
        print(f"New title added: {new_title} by {new_author}.")
    else:
        print("This book already exists in the library.")


def main():
    library = [
        ("1984", "George Orwell"), 
        ("Brave New World", "Aldous Huxley")
        ]

    while True:
        print("\n1. View All Books")
        print("2. Search by Title")
        print("3. Add Title to Library")
        print("4. Exit")
        choice = input("Enter your choice:  ")
    

        if choice == "1":
            display_library(library)
        elif choice == "2":
            search_by_title(library)
        elif choice == "3":
            add_title(library)
        elif choice == "4":
            print("Exiting program")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == '__main__':
    main()