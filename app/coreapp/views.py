from django.shortcuts import render
from django.views import generic
from .models import Post

class BlogView(generic.ListView):
    queryset = Post.objects.filter(status=0).order_by('-created_on')
    template_name = "posts.html"