from django.test import TestCase
from . models import Post
from django.urls import reverse
from django.contrib.auth import get_user_model

class BlogTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@gmail.com',
            password = 'testing321',
        )

        self.post = Post.objects.create(
            user=self.user,
            title='hello',
            body='body part'
        )

    def test_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')


    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'hello')
        self.assertEqual(f'{self.post.user}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'body part')

    def test_post_list_view(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'body part')
        self.assertTemplateUsed(resp, 'home/home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'body part')
        self.assertTemplateUsed(response, 'home/detail.html')

    def test_post_create_view(self):
        resp = self.client.get(reverse('post-new'), {
            'title': 'New title',
            'body': 'New body',
            'user': self.user
        })

        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'New')
        self.assertContains(resp, 'body')

    def test_post_update_view(self):
        resp = self.client.get(reverse('post-edit', args='1'),{
            'title': 'Updated title',
            'body': 'Updated text'
        })

        self.assertEqual(resp.status_code, 200)

    def test_post_delete_view(self):
        resp = self.client.get(reverse('post-delete', args='1'))
        self.assertEqual(resp.status_code, 200)








