from urllib import response
from django.test import TestCase
from django.urls import reverse
from .models import Book


class TestBook(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="test books title",
            subtitle="test books subtitle",
            author=" test books author",
            isbn="1234567890",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "test books title")
        self.assertEqual(self.book.subtitle, "test books subtitle")
        self.assertEqual(self.book.author, " test books author")
        self.assertEqual(self.book.isbn, "1234567890")

    def test_book_list_view(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test books subtitle")
        self.assertTemplateUsed(response, "book/book_list.html")
