from django.contrib import admin
from .models import Genre, Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'genre', 'published_date')
    list_filter = ('genre',)

admin.site.register(Book, BookAdmin)
admin.site.register(Genre)