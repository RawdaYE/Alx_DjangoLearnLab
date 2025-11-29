from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    author_name = input("Enter author name: ")
    try:
        author = Author.objects.get(name = author_name)
        books = author.books.all()
        print(f"Books written by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name '{author_name}'")

    
    library_name = input("\nEnter library name: ")
    try:
        library = Library.objects.get(name = library_name)
        books_in_library  = library.books.all()
        print(f"Books in {library_name}:")
        for book in books_in_library:
            print(f"{book.title}")
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'")
    
    try:
        library = Library.objects.get(name = library_name)
        librarian = library.librarian
        print(f"Librarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to '{library_name}'")


if __name__ == "__main__":
    run_queries()

