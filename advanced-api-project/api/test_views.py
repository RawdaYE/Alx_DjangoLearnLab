from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book



"""
Unit tests for Book API endpoints:

- List, Retrieve, Create, Update, Delete
- Filtering by title, author, publication_year
- Searching by title and author
- Ordering by title and publication_year
- Permissions for authenticated vs unauthenticated users

Run tests: python manage.py test api
"""


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client = APIClient()

        # Create an author
        self.author = Author.objects.create(name='Chimamanda Ngozi Adichie')

        # Create books
        self.book1 = Book.objects.create(
            title='Half of a Yellow Sun',
            publication_year=2006,
            author=self.author
        )
        self.book2 = Book.objects.create(
            title='Americanah',
            publication_year=2013,
            author=self.author
        )

    def test_list_books(self):
        """Test retrieving the list of books"""
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book_authenticated(self):
        """Test creating a book with authentication"""
        self.client.login(username='testuser', password='password123')
        url = reverse('book-create')
        data = {
            'title': 'Purple Hibiscus',
            'publication_year': 2003,
            'author': self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.client.logout()

    def test_create_book_unauthenticated(self):
        """Test that unauthenticated users cannot create a book"""
        url = reverse('book-create')
        data = {
            'title': 'Purple Hibiscus',
            'publication_year': 2003,
            'author': self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_retrieve_book_detail(self):
        """Test retrieving a single book"""
        url = reverse('book-detail', kwargs={'pk': self.book1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Half of a Yellow Sun')

    def test_update_book_authenticated(self):
        """Test updating a book as authenticated user"""
        self.client.login(username='testuser', password='password123')
        url = reverse('book-update', kwargs={'pk': self.book1.id})
        data = {
            'title': 'Half of a Yellow Sun (Updated)',
            'publication_year': 2006,
            'author': self.author.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Half of a Yellow Sun (Updated)')
        self.client.logout()

    def test_delete_book_authenticated(self):
        """Test deleting a book as authenticated user"""
        self.client.login(username='testuser', password='password123')
        url = reverse('book-delete', kwargs={'pk': self.book2.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)
        self.client.logout()

    def test_filter_books_by_year(self):
        """Test filtering books by publication_year"""
        url = reverse('book-list') + '?publication_year=2013'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Americanah')

    def test_search_books_by_title(self):
        """Test searching books by title"""
        url = reverse('book-list') + '?search=Americanah'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Americanah')

    def test_order_books_by_publication_year_desc(self):
        """Test ordering books by publication_year descending"""
        url = reverse('book-list') + '?ordering=-publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2013)
