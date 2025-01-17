from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from datetime import date

from .models import Book

User = get_user_model()


class Test_pages(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", email="hereis@example.com", password="135210h.")
        self.book1 = Book.objects.create(
            name="Django for Beginners", author="William S. Vincent", description="All about django!"
        )
        self.client.login(username="testuser", password="135210h.")

    def test_bookModel(self):
        book = Book.objects.get(name="Django for Beginners")
        self.assertEqual(book.author, "William S. Vincent")

    def test_homePage(self):
        url = reverse("home_page")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_book(self):
        url = reverse("create_book")
        self.assertEqual(self.client.get(url).status_code, 200)

    def test_books_list(self):
        url = reverse("books_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,text="Django for Beginners")

    def test_students_list(self):
        url = reverse("students_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)