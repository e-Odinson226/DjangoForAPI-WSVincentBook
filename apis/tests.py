from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from books.models import Book


class APITest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="test book title",
            subtitle="test book subtitle",
            author="test book author",
            isbn="test book isbn",
        )

    def test_api_list_view(self):
        response = self.client.get(reverse("book_list_api"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.book)
