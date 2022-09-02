from django.urls import path
from .views import *

urlpatterns = [
    path("", BooksListViews.as_view(), name="book-list"),
]
