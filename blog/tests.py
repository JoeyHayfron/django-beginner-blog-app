from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import BlogPost

# Create your tests here.
class BlogPostsModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@gmail.com",
            password="secret"
        )
        
        self.post = BlogPost.objects.create(
            title="Some Title",
            body="Nice body content",
            author=self.user
        )
        
    def test_string_representation(self):
        post = BlogPost(title="New Post")
        self.assertEqual(str(post), post.title)
        
    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'Some Title')
        self.assertEqual(f'{self.post.body}', 'Nice body content')
        self.assertEqual(f'{self.post.author}', 'testuser')
        
    def test_post_list_view(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'blog_posts.html')
        
    def test_post_detail_view(self):
        response = self.client.get('/blogpost/1/')
        non_response = self.client.get('/blogpost/1000000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(non_response.status_code, 404)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'blog_post.html')
        
    def test_get_absolute_url(self):
        response = self.post.get_absolute_url()
        self.assertEqual(response, '/blogpost/1/')
    
    def test_post_create_view(self):
        response = self.client.post(reverse('new_post'), {
            'title': 'A new one',
            'body': 'New body',
            'author': self.user    
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A new one')
        self.assertContains(response, 'New body')
        
        
    def test_edit_post_view(self):
        response = self.client.post(reverse('update_post', args="1"), {
            'title': 'NEw',
            'body': 'I will be the greatest Python dev'
        })
        self.assertEqual(response.status_code, 302)
        
    def test_delete_post(self):
         response = self.client.post(reverse('delete_post',args='1') )
         self.assertEqual(response.status_code, 302)