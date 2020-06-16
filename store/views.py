from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SignUpForm
from .models import Book


# Create your views here.

def index(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'web/index.html', context)


def detail(request, id):
    book = get_object_or_404(Book, pk=id)
    context = {'book': book}
    return render(request, 'web/detail.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})
