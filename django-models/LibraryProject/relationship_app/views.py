from django.shortcuts import render
from relationship_app.models import  Book, Library
from django.views.generic import ListView, DetailView

def list_all_books(request):
    books = Book.objects.all()
    return render(request, 'list_book.html', {'books': books})

if __name__ == "__main__":
    list_all_books()

class BookList(ListView):
    model = Book
    template_name = 'list_book.html'
    context_object_name= 'books'


class LibraryDetail(DetailView):
    model = Library
    template_name= 'library_detail.html'
    context_object_name= 'library'