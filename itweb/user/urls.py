from django.urls import path
from . import views
from user.views import user_author
from django.contrib.auth.views import LogoutView
from .views import NewsUpdateView, QuoteUpdateView, AuthorUpdateView, QuoteDeleteView, AuthorDeleteView, NewsDeleteView



urlpatterns = [
    path('create', views.user_create, name='create'),
    path('login', views.user_login, name='login'),
    path('home', views.user_home, name='userhome'),
    path('news', views.user_news, name='usernews'),
    path('authors', user_author, name='userauthors'),
    path('quotes', views.user_quote, name='userquotes'),
    path('news/<int:id>/', views.news_detail, name='news_detail'),
    path('authors/<int:id>/', views.author_detail, name='author_detail'),
    path('quotes/<int:pk>/update', QuoteUpdateView.as_view(), name='quoteupdate'),
    path('news/<int:pk>/update', NewsUpdateView.as_view(), name='newsupdate'),
    path('authors/<int:pk>/update', AuthorUpdateView.as_view(), name='authorupdate'),
    path('quotes/<int:pk>/delete', QuoteDeleteView.as_view(), name='quotedelete'),
    path('news/<int:pk>/delete', NewsDeleteView.as_view(), name='newsdelete'),
    path('authors/<int:pk>/delete', AuthorDeleteView.as_view(), name='authordelete'),
    path('news/add', views.add_news, name='addnews'),
    path('authors/add', views.add_author, name='addauthors'),
    path('quotes/add', views.add_quote, name='addquotes'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<str:username>/', views.profile, name='profile'),
]