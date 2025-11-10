# Retrieve Operation

```python
from bookshelf.models import Book

# Retrieve all books
books = Book.objects.all()
books

```

Expected output: 

```
 <QuerySet [<Book: 1984>]> 
``` 
Comment: Successfully retrieved the book we created.