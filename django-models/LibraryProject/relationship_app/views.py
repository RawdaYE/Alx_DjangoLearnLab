from django.shortcuts import render
from .models import Library
from .models import Book
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


def list_all_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class List_books(ListView):
    model = Book
    template_name = 'relationship_app/list_books.html'
    context_object_name= 'books'


class LibraryDetailView(DetailView):
    model = Library
    template_name= 'relationship_app/library_detail.html'
    context_object_name= 'library'