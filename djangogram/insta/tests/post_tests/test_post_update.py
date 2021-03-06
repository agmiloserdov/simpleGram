from django.core.exceptions import ValidationError
from django.test import TestCase

from django.contrib.auth.models import User
from django.urls import reverse

from insta.models.post import Post
from insta.views.post import UpdatePostView


class PostUpdateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test_user", password="1@abcTest",
                                             email="test@email.com")
        self.post = Post.objects.create(title='test_title', description='test_description', image='test.jpg',
                                        creator=self.user)

    def test_update_post_when_not_signed_up(self):
        response = self.client.get(reverse('insta:edit', kwargs={'pk': 1}), follow=True)
        status_code = self.client.get(reverse('insta:add')).status_code
        self.assertEqual('/accounts/login/', response.request['PATH_INFO'])
        self.assertEqual(302, status_code)

    def test_update_post_when_signed_up(self):
        self.client.login(username='test_user', password="1@abcTest")
        with open('insta/tests/fixtures/test_image.jpg', 'rb') as fp:
            response = self.client.post(reverse('insta:edit', kwargs={'pk': 1}), {'title': 'test_title',
                                                                                  'description': 'test_description',
                                                                                  'image': fp,
                                                                                  'creator': self.user}, follow=True)
        post = response.context_data['post']

        self.assertEqual('/posts/1', response.request['PATH_INFO'])
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, post.pk)
        self.assertTrue(response.is_rendered)
        self.assertTrue(response.charset == 'utf-8')
        self.assertEqual('test_title', post.title)
        self.assertEqual('test_description', post.description)
        self.assertIsNotNone(post.image)
        self.assertEqual(self.user, post.creator)

    def test_get_error_messages(self):
        self.client.login(username='test_user', password="1@abcTest")
        with open('insta/tests/fixtures/test.txt', 'rb') as fp:
            response = self.client.post(reverse('insta:edit', kwargs={'pk': 1}),
                                        {'title': 'q',
                                         'description': 'q',
                                         'image': fp,
                                         'creator': self.user}, follow=True)

        self.assertEqual(200, response.status_code)
        self.assertIn('post/edit.html', response.template_name)
        self.assertIsInstance(response.context_data['view'], UpdatePostView)
        self.assertTrue(response.charset == 'utf-8')
        self.assertRaisesMessage(ValidationError,
                                 expected_message="??????????????????, ?????? ?????? ???????????????? ???????????????? ???? ?????????? 3 ???????????????? (???????????? 1)")
        self.assertRaisesMessage(ValidationError,
                                 expected_message="?????????????????? ???????????????????? ??????????????????????. ????????, ?????????????? ???? ??????????????????, "
                                                  "?????????????????? ?????? ???? ???????????????? ????????????????????????.")

    def tearDown(self):
        self.user.delete()
        self.post.delete()
