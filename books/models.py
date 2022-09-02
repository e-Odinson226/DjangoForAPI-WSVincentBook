from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=720)
    author = models.CharField(max_length=120)
    isbn = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.title
