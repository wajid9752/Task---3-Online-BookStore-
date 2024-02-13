from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE , related_name="books")
    published_date = models.DateField()

    def __str__(self):
        return self.title





