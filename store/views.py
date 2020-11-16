from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SignUpForm, CommentsForm, CartForm
from .models import Book, Comments, Cart


# Create your views here.

def index(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'web/index.html', context)


def detail(request, id):
    book = get_object_or_404(Book, pk=id)
    user = request.user
    comments = Comments.objects.filter(book_id=id)
    form = CommentsForm(request.POST)
    cart_quantity = CartForm(request.GET)
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = user
            comment.book = book
            comment.save()
            form = CommentsForm()
        else:
            form = CommentsForm()
    if request.method == 'GET':
        if form.is_valid():
            cart_quantity = CartForm(request.GET.dict())
            quantity = cart_quantity.data.__len__()
            context = {
                'book': book.id,
                'quantity': quantity
            }
            return redirect(add_to_cart, context)
    context = {
        'book': book,
        'form': form,
        'comments': comments,
        'cart_quantity': cart_quantity
    }
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
        context = {
            'form': form
        }
        return render(request, 'registration/signup.html', context)


def cart(request):
    user = request.user.id
    cart_items = Cart.objects.filter(user_id=user)
    context = {
        'cart': cart_items
    }
    return render(request, 'web/cart.html', context)


@login_required(login_url='/account/login/')
def add_to_cart(request, id, quantity):
    user = request.user
    Cart.objects.create(user_id=user.id, book_id=id, quantity=quantity)
    return redirect('cart')
