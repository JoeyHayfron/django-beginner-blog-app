from django.urls import path
from .views import BlogListView, BlogItemView, NewBlogPostView, UpdateBlogPost, DeleteBlogPost

urlpatterns = [
    path('blogpost/delete/<int:pk>/', DeleteBlogPost.as_view(), name='delete_post'),
    path('blogpost/edit/<int:pk>/',UpdateBlogPost.as_view(), name="update_post"),
    path('post/new/', NewBlogPostView.as_view(), name="new_post"),
    path('blogpost/<int:pk>/', BlogItemView.as_view(), name="blog_details"),
    path('', BlogListView.as_view(), name="home")
]
