from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.book_list, name='list_books'),
    path('create/', views.add_book, name='add_book'),
    path('edit/', views.edit_book, name='edit_book'),
    path('delete/', views.delete_book, name='delete_book'),

]