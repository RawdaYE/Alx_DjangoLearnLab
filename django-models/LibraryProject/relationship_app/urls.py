from django.urls import path
from .  import views
from .views import list_books, BookListView, LibraryDetailView
from .views import LoginView, LogoutView
from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view

urlpatterns = [
    path('books/', list_books, name = 'list_all_books'),
    path('books/list/', BookListView.as_view(), name = 'book'),
    path('Library/<int:pk>/', LibraryDetailView.as_view(), name = 'library'),

    path('register/', views.register, name= 'register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name= 'login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name= 'logout'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]