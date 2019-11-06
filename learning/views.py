from django.shortcuts import render
from .models import Book, Movie


# Create your views here.
def index(request):
    """学习模块主页"""
    return render(request, 'learning/index.html')


def books(request):
    """显示书单"""
    books = Book.objects.order_by('field')
    context = {
        'books': books,
    }
    return render(request, 'learning/bookList.html', context)


def movies(request):
    """显示电影清单"""
    movies = Movie.objects.order_by('DateField')
    context = {
        'movies': movies,
    }
    return render(request, 'learning/movieList.html', context)


def book(request, book_id):
    """显示特定某本书"""
    book = Book.objects.get(id=book_id)
    author = book.author
    field = book.field
    description = book.description
    progress = book.progress
    context = {
        'book': book,
        'author': author,
        'field': field,
        'description': description,
        'progress': progress,
    }
    return render(request, 'learning/book.html', context)


def movie(request, movie_id):
    """显示特定某个电影"""
    movie = Movie.objects.get(id=movie_id)
    director = movie.director
    dateField = movie.DateField
    description = movie.description
    review = movie.review
    context = {
        'movie': movie,
        'director': director,
        'dateField': dateField,
        'description': description,
        'review': review,
    }
    return render(request, 'learning/movie.html', context)
