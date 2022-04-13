from django.shortcuts import render


posts = [
    {
        "author": "KelvinR",
        "title": "Blog post 1",
        "content": "First post content",
        "date_posted": "April 13, 2022"
    },
    {
        "author": "Jane Doe",
        "title": "Blog post 2",
        "content": "Second post content",
        "date_posted": "April 23, 2022"
    },
]


def home(request):
    context = {
        "posts": posts
    }
    return render(request, "BlogHome/home.html", context)


def about(request):
    return render(request, "BlogHome/about.html", {'title': 'About'})
