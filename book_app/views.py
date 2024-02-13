from .models import Book, Genre
from .forms import BookForm , GenreForm
from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.models import Q

##################  Book ##################################
def book_view(request):
  
    query = request.GET.get("query")
    if query:
        books = Book.objects.filter(
            Q(title__icontains=query)|
            Q(author__icontains=query)|
            Q(genre__name__icontains = query)
        )
    else:
        books = Book.objects.all()

    return render(request , "book-view.html", {'books':books} )


def book_detail(request , pk):
    book = Book.objects.get(id=pk)
    return render(request , "book-detail.html", {'book':book})



def book_create_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request ,"Book Added Successfully")
            return redirect('book-view')  
    else:
        form = BookForm()
    return render(request, 'form.html', {'form': form})


def book_update_view(request , pk):
    obj = Book.objects.get(id=pk)
    if request.method == 'POST':
        form = BookForm(request.POST , instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request ,"Book Update Successfully")
            return redirect('book-view') 
    else:
        form = BookForm(instance=obj)
    return render(request, 'form.html', {'form': form})

#####################  Genre ##############################

def genre_view(request):
    genres = Genre.objects.all()
    return render(request , "genre-view.html", {'genres':genres} )

def genre_create_view(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request ,"Genre Added Successfully")
            return redirect('genre-view')  
    else:
        form = GenreForm()
    return render(request, 'form.html', {'form': form})


def genre_update_view(request , pk):
    obj = Genre.objects.get(id=pk)
    if request.method == 'POST':
        form = GenreForm(request.POST , instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request ,"Genre Update Successfully")
            return redirect('genre-view') 
    else:
        form = GenreForm(instance=obj)
    return render(request, 'form.html', {'form': form})





