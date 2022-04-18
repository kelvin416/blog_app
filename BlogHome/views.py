from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "BlogHome/home.html", context)


def about(request):
    return render(request, "BlogHome/about.html", {'title': 'About'})
