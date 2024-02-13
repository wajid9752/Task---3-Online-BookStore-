from django.test import TestCase
from django.urls import reverse
from book_app.models import Book, Genre
from book_app.forms import BookForm, GenreForm

class BookViewsTestCase(TestCase):
    def setUp(self):
        self.book1 = Book.objects.create(title='Test Book 1', author='Author 1', genre='Genre 1')
        self.book2 = Book.objects.create(title='Test Book 2', author='Author 2', genre='Genre 2')

    def test_book_view_with_query(self):
        url = f'{reverse("book-view")}?query=Test'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Book 1')
        self.assertNotContains(response, 'Test Book 2')

    def test_book_view_without_query(self):
        url = reverse("book-view")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Book 1')
        self.assertContains(response, 'Test Book 2')

    def test_book_detail_view(self):
        url = reverse("book-detail", kwargs={'pk': self.book1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Book 1')

    # Similarly, you can write tests for book_create_view and book_update_view


class GenreViewsTestCase(TestCase):
    def setUp(self):
        self.genre1 = Genre.objects.create(name='Test Genre 1')
        self.genre2 = Genre.objects.create(name='Test Genre 2')

    def test_genre_view(self):
        url = reverse("genre-view")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Genre 1')
        self.assertContains(response, 'Test Genre 2')

    # Similarly, you can write tests for genre_create_view and genre_update_view
