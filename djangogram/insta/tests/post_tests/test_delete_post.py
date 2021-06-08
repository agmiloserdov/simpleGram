from django.test import TestCase

from django.contrib.auth.models import User
from django.urls import reverse

from insta.models.post import Post


class PostDeleteTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test_user", password="1@abcTest",
                                             email="test@email.com")
        self.post = Post.objects.create(title='test_title', description='test_description', image='test.jpg',
                                        creator=self.user)
        self.client.login(username='test_user', password="1@abcTest")

    def test_delete_post(self):
        response = self.client.post(reverse('insta:delete', kwargs={'pk': 1}), follow=True)
        self.assertEqual(200, response.status_code)
        self.assertFalse(Post.objects.filter(pk=1))

    def test_delete_not_exists_post(self):
        self.client.login(username='test_user', password="1@abcTest")
        response = self.client.post(reverse('insta:delete', kwargs={'pk': 0}), follow=True)
        self.assertEqual(404, response.status_code)

    def tearDown(self):
        self.client.logout()
        self.user.delete()
        self.post.delete()
