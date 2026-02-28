from library import librarian
library = librarian.load_library()

while True:
    print("\n1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Exit")

    choice = input("Choose: ")

    if choice == "1":
        title = input("Title: ")
        author = input("Author: ")
        isbn = input("ISBN: ")
        librarian.add_book(library, title, author, isbn)

    elif choice == "2":
        librarian.display_books(library)

    elif choice == "3":
        keyword = input("Enter title: ")
        librarian.search_book(library, keyword)

    elif choice == "4":
        isbn = input("Enter ISBN: ")
        librarian.remove_book(library, isbn)

    elif choice == "5":
        isbn = input("Enter ISBN: ")
        librarian.check_out_book(library, isbn)

    elif choice == "6":
        isbn = input("Enter ISBN: ")
        librarian.return_book(library, isbn)

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")