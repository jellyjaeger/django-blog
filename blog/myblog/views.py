from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User
myposts = [{'name':'the book','content':'hello world','author':'sooraj','date_time':'28 august'},
{'name':'the book1','author':'sanjay','content':'hello world','date_time':'28 august'},
{'name':'the book1','author':'sanjay','content':'hello world','date_time':'28 august'},
{'name':'the book1','author':'sanjay','content':'hello world','date_time':'28 august'}
]
def home(request):
    return render(request,"myblog/index.html",
    {
        "posts":Post.objects.all(),
        "title":"myblog"
    })
def about(request):
    return render(request,"myblog/about.html")

