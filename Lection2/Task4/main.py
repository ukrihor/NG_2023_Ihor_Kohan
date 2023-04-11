import json


def load_data():
    try:
        with open("books.txt", "r") as f:
            return json.load(f)
    except:
        return []


def save_data(books):
    with open("books.json", "w") as f:
        json.dump(books, f)


books = load_data()

print("\nSelect an action:")
print("1. Add book")
print("2. Remove book")
print("3. Edit book")
print("4. Search books")
print("5. Exit")

while True:
    choice = input("Please enter a number from 1 to 5: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        pages = input("Enter number of pages: ")
        genre = input("Enter book genre: ")
        binding = input("Enter book binding (hardcover/paperback): ")
        book = {"title": title, "author": author, "pages": pages, "genre": genre, "binding": binding}
        books.append(book)
        save_data(books)
        print(f"Book '{title}' added to the database.")

    elif choice == "2":
        title = input("Enter book title to remove: ")
        found = False
        for i, book in enumerate(books):
            if book["title"] == title:
                books.pop(i)
                save_data(books)
                print(f"Book '{title}' removed from the database.")
                found = True
                break
        if not found:
            print(f"Book '{title}' not found in the database.")

    elif choice == "3":
        title = input("Enter book title to edit: ")
        field = input("Enter field to edit (title/author/pages/genre/binding): ")
        value = input(f"Enter new value for '{field}': ")
        found = False
        for book in books:
            if book["title"] == title:
                book[field] = value
                save_data(books)
                print(f"'{field}' of book '{title}' has been updated to '{value}'.")
                found = True
                break
        if not found:
            print(f"Book '{title}' not found in the database.")

    elif choice == "4":
        field = input("Enter field to search (title/author/pages/genre/binding): ")
        value = input(f"Enter value to search for in '{field}': ")
        found_books = []
        for book in books:
            if book[field] == value:
                found_books.append(book)
        if found_books:
            print(f"{len(found_books)} book(s) found:")
            for book in found_books:
                print(
                    f"{book['title']} ({book['author']}) - {book['pages']} pages, {book['genre']}, {book['binding']} binding")
        else:
            print("No books found.")

    elif choice == "5":
        break

    else:
        print("Invalid choice.")





