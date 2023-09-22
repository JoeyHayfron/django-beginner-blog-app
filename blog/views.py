from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost

# Create your views here.
class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog_posts.html'
    
    context_object_name = 'blog_post_list'


class BlogItemView(DetailView):
    model = BlogPost
    template_name = 'blog_post.html'