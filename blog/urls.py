from django.urls import path
from .views import BlogListView, BlogItemView

urlpatterns = [
    path('blogpost/<int:pk>/', BlogItemView.as_view(), name="blog_details"),
    path('', BlogListView.as_view(), name="home")
]
