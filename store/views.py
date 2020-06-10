from django.shortcuts import render, get_object_or_404
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
