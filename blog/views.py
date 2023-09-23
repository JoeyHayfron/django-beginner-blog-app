from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from django.urls import reverse_lazy

# Create your views here.
class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog_posts.html'
    context_object_name = 'blog_post_list'


class BlogItemView(DetailView):
    model = BlogPost
    template_name = 'blog_post.html'

    
class NewBlogPostView(CreateView):
    model = BlogPost
    template_name = 'new_post.html'
    fields = ['title', 'author', 'body']

class UpdateBlogPost(UpdateView):
    model = BlogPost
    template_name = 'update_post.html'
    fields = ['title', 'body']
    
class DeleteBlogPost(DeleteView):
    model = BlogPost
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    