from django.shortcuts import render
from django.views.generic import ListView

from .models import *


class BooksListViews(ListView):
    model = Book
    template_name = "book_list.html"
