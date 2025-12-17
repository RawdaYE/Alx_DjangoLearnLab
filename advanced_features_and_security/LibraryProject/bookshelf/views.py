from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book
from .forms import BookSearchForm
from django.db.models import Q
# Create your views here.



@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
        form = BookSearchForm(request.GET or None)
        books = Book.objects.all()
        if form.is_valid():
           query = form.cleaned_data.get('query', '').strip()
           if query:
               # Safe ORM query prevents SQL injection
               books = books.filter(Q(title__icontains=query) | Q(author__icontains=query))

        return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})
        
        
@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
        return HttpResponse("Add book page")
    

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request):
        return HttpResponse("Edit book page")
    

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request):
        return HttpResponse("Delete book page")