from django.urls import path
from .  import views
from .views import list_books, BookListView, LibraryDetailView
from .views import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('books/', list_books, name = 'list_all_books'),
    path('books/list/', BookListView.as_view(), name = 'book'),
    path('Library/<int:pk>/', LibraryDetailView.as_view(), name = 'library'),

    path('register/', RegisterView.as_view(), name= 'register'),
    path('login/', LoginView.as_view(), name= 'login'),
    path('logout/', LogoutView.as_view(), name= 'logout'),
]