# Retrieve Operation

```python
from bookshelf.models import Book

# Retrieve all books
book = Book.objects.get(title = "1984")
book

```

Expected output: 

```
 <Book: 1984>
``` 
Comment: Successfully retrieved the book we created.