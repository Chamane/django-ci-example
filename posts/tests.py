from django.test import TestCase

from .models import Post 

class PostTests(TestCase):
    def test_create_post(self):
        post = Post(title='Django', body='Django is good...')
        self.assertEqual('Django', post.title)
        self.assertEqual('Django is good...', post.body)