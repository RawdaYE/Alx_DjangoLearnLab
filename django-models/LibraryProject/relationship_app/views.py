from django.shortcuts import render
from .models import Library
from .models import Book
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


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


class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

class LoginView(LoginView):
    template_name = 'relationship_app/login.html'

class LogoutView(LogoutView):
    next_page = 'login'