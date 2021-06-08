from django.test import TestCase

from django.contrib.auth.models import User
from django.urls import reverse

from accounts.models import InstaUser
from insta.models.post import Post


class PostDetailsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test_user", password="1@abcTest",
                                             email="test@email.com")
        self.profile = InstaUser.objects.create(user=self.user)
        self.post = Post.objects.create(title='test_title', description='test_description', image='test.jpg',
                                        creator=self.user)
        self.client.login(username='test_user', password="1@abcTest")

    def test_get_post(self):
        response = self.client.get(reverse('insta:post', kwargs={'pk': 1}))

        self.assertEqual(200, response.status_code)
        post = response.context_data['post']
        self.assertEqual('test_title', post.title)
        self.assertEqual('test_description', post.description)
        self.assertEqual('test.jpg', post.image)
        self.assertEqual('/posts/1', response.request['PATH_INFO'])

    def test_get_not_found_post(self):
        response = self.client.get(reverse('insta:post', kwargs={'pk': 99999}))
        self.assertEqual(404, response.status_code)

    def tearDown(self):
        self.user.delete()
        self.profile.delete()
        self.post.delete()
