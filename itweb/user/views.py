from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import AuthorForm, QuoteForm, ArticleForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from main.models import Articles, Author, Quote, Tag
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.generic import UpdateView, DeleteView



def user_create(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'user/create.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/user/home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'user/login.html')


def quote_list(request):
    quotes = Quote.objects.all()
    return render(request, 'user/userquote.html', {'quotes': quotes})


def news_detail(request, id):
    news = get_object_or_404(Articles, id=id)
    return render(request, 'user/news_detail.html', {'news': news})


def author_detail(request, id):
    author = get_object_or_404(Author, id=id)
    return render(request, 'user/author_detail.html', {'author': author})


def quote_detail(request, id):
    quote = get_object_or_404(Author, id=id)
    return render(request, 'user/quote_detail.html', {'quote': quote})



class NewsUpdateView(UpdateView):
    model = Articles
    form_class = ArticleForm
    template_name = 'user/update_news.html'



class QuoteUpdateView(UpdateView):
    model = Quote
    template_name = 'user/update_quote.html'

    form_class = QuoteForm



class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'user/update_author.html'

    form_class = AuthorForm




class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'user/delete_news.html'
    success_url = '/user/news'



class QuoteDeleteView(DeleteView):
    model = Quote
    template_name = 'user/delete_quote.html'
    success_url = '/user/quotes'



class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'user/delete_author.html'
    success_url = '/user/authors'






@login_required
def profile(request, username):
    user_profile = get_object_or_404(User, username=username)
    return render(request, 'user/profile.html', {'user_profile': user_profile})

@login_required
def user_home(request):
    return render(request, 'user/userhome.html')


@login_required
def user_news(request):
    news_page = Articles.objects.order_by()
    return render(request, 'user/usernews.html', {'news': news_page})


@login_required
def user_author(request):
    authors_page = Author.objects.all()
    return render(request, 'user/userauthor.html', {'authors': authors_page})



@login_required
def user_quote(request):
    quotes = Quote.objects.all()
    return render(request, 'user/userquote.html', {'quotes': quotes})


@login_required
def add_news(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usernews')
    else:
        error = 'Form error'

    form = ArticleForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'user/add_news.html', data)


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userauthors')
    else:
        form = AuthorForm()
    return render(request, 'user/add_author.html', {'form': form})


@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userquotes')
    else:
        form = QuoteForm()
    return render(request, 'user/add_quote.html', {'form': form})


@login_required
def add_tags(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userquotes')
    else:
        form = QuoteForm()
    return render(request, 'user/add_quote.html', {'form': form})

