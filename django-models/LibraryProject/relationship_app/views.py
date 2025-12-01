from .models import Library
from .models import Book
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class BookListView(ListView):
    model = Book
    template_name = 'relationship_app/list_books.html'
    context_object_name= 'books'


class LibraryDetailView(DetailView):
    model = Library
    template_name= 'relationship_app/library_detail.html'
    context_object_name= 'library'


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('login') 
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

class LoginUserView(LoginView):
    template_name='relationship_app/login.html'

class LogoutUserView(LogoutView):
    next_page = 'login'



def is_admin(user):
    return user.userprofile.role == "admin"

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

def is_member(user):
    return user.userprofile.role == "member"

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

def is_librarian(user):
    return user.userprofile.role == "librarian"

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book_view(request):
        return HttpResponse("Add Book - Permission Granted")

@permission_required('relationship_app.can_change_book', raise_exception=True)
def change_book_view(request, book_id):
        return HttpResponse(f"Edit Book {book_id} - Permission Granted")

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book_view(request, book_id):
        return HttpResponse(f"Delete Book {book_id}- Permission Granted")

