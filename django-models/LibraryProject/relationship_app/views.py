from django.shortcuts import render
from relationship_app.models import  Book, Library
from django.views.generic import ListView, DetailView

def list_all_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class BookList(ListView):
    model = Book
    template_name = 'relationship_app/list_books.html'
    context_object_name= 'books'


class LibraryDetail(DetailView):
    model = Library
    template_name= 'relationship_app/library_detail.html'
    context_object_name= 'library'