from django.shortcuts import render


def index(request):
    return render(request, "website/index.html")


def download(request):
    return render(request, "website/download.html")


def register(request):
    return render(request, "website/register.html")


def sign_in(request):
    return render(request, "website/signin.html")
