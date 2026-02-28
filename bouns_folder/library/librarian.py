import json

FILE = "books.json"


def load_library():
    try:
        f = open(FILE, "r")
        data = json.load(f)
        f.close()
        return data
    except:
        return {}


def save_library(library):
    f = open(FILE, "w")
    json.dump(library, f)
    f.close()


def add_book(library, title, author, isbn):
    if isbn in library:
        print("Book already exists.")
    else:
        library[isbn] = {
            "title": title,
            "author": author,
            "available": True
        }
        save_library(library)


def remove_book(library, isbn):
    if isbn in library:
        del library[isbn]
        save_library(library)
    else:
        print("Book not found.")


def check_out_book(library, isbn):
    if isbn in library and library[isbn]["available"]:
        library[isbn]["available"] = False
        save_library(library)
    else:
        print("Cannot borrow book.")


def return_book(library, isbn):
    if isbn in library:
        library[isbn]["available"] = True
        save_library(library)
    else:
        print("Book not found.")


def display_books(library):
    if not library:
        print("No books.")
        return

    for isbn, book in library.items():
        status = "Available" if book["available"] else "Borrowed"
        print(f"{book['title']} by {book['author']} (ISBN: {isbn}) - {status}")


def search_book(library, keyword):
    found = False
    for isbn, book in library.items():
        if keyword.lower() in book["title"].lower():
            status = "Available" if book["available"] else "Borrowed"
            print(f"{book['title']} by {book['author']} (ISBN: {isbn}) - {status}")
            found = True

    if not found:
        print("No matching books found.")