from django.shortcuts import render
from .models import Articles, Author, Quote



def index(request):
    return render(request, 'main/index.html')


def news(request):
    news_page = Articles.objects.order_by()
    return render(request, 'main/news.html', {'news': news_page})


def authors(request):
    authors_page = Author.objects.all()
    return render(request, 'main/authors.html', {'authors': authors_page})


def quotes(request):
    quotes_page = Quote.objects.order_by()
    return render(request, 'main/quotes.html', {'quotes': quotes_page})
