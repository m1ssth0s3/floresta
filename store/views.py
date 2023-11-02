from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'store/index.html', context)


def signin(request):
    context = {}
    return render(request, 'store/signin.html', context)


def signup(request):
    context = {}
    return render(request, 'store/signup.html', context)


def store(request):
    context = {}
    return render(request, 'store/store.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
