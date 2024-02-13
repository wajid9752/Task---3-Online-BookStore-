from django.urls import path,include
from book_app import views
urlpatterns = [
   path("",                  views.book_view ,         name="book-view"),
   path("book-detail/<int:pk>/",                  views.book_detail ,         name="book-detail"),
   path("book_create_view/", views.book_create_view ,  name="book-create-view"),
   path("book_update_view/<int:pk>/", views.book_update_view ,  name="book-update-view"),
   path("genre_view/",       views.genre_view ,        name="genre-view"),
   path("genre_create_view/",views.genre_create_view , name="genre-create-view"),
   path("genre_update_view/<int:pk>/",views.genre_update_view , name="genre-update-view"),
]
