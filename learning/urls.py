from django.conf.urls import re_path
from . import views


urlpatterns = [
    # learning主页
    re_path(r'^$', views.index, name='index'),
    # 显示书单
    re_path(r'^BookList/$', views.books, name='books'),
    # 显示电影清单
    re_path(r'^MovieList/$', views.movies, name='movies'),
    # 显示单个详细图书
    re_path(r'^BookList/(?P<book_id>\d+)/$', views.book, name='book'),
    # 显示单个详细电影
    re_path(r'^MovieList/(?P<movie_id>\d+)/$', views.movie, name='movie'),
]