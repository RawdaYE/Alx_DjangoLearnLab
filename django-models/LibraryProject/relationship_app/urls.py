from django.urls import path
from .  import views
from .views import BookList, LibraryDetail

urlpatterns = [
    path('', views.list_all_books, name = 'list_all_books'),
    path('books/list/', BookList.as_view(), name = 'book'),
    path('LibraryDetail/<int:pk>/', LibraryDetail.as_view(), name = 'library'),
]