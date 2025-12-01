from django.urls import path
from . import views
from .views import list_books, BookListView, LibraryDetailView
from .views import LoginView, LogoutView


urlpatterns = [
    path('books/', list_books, name = 'list_all_books'),
    path('books/list/', BookListView.as_view(), name = 'book'),
    path('Library/<int:pk>/', LibraryDetailView.as_view(), name = 'library'),

    path('register/', views.register, name= 'register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name= 'login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name= 'logout'),
    path('admin/', views.admin_view, name='admin'),
    path('librarian/', views.librarian_view, name='librarians'),
    path('member/', views.member_view, name='members'),
    path('books/add', views.add_book_view, name='add_book'),
    path('books/<int:book_id>/edit/', views.change_book_view, name='edit_book'),
    path('books/<int:book_id>/delete/', views.delete_book_view, name='delete_book'),
    

]