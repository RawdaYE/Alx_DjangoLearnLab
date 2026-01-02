## Book API Views

This project uses Django REST Framework generic views to implement CRUD operations for the Book model.

### Views
- BookListView: Lists all books (public access)
- BookDetailView: Retrieves a single book by ID (public access)
- BookCreateView: Creates a new book (authenticated users only)
- BookUpdateView: Updates an existing book (authenticated users only)
- BookDeleteView: Deletes a book (authenticated users only)

### Permissions
Read-only endpoints are accessible to unauthenticated users.
Write operations are restricted to authenticated users using DRF permission classes.
