from datetime import datetime

from django.http import JsonResponse
from django.test import TestCase

from django.contrib.auth.models import User
from django.urls import reverse

from insta.models.comment import Comment
from insta.models.post import Post


class CommentTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test_user", password="1@abcTest",
                                             email="test@email.com")
        self.post = Post.objects.create(title='test_title', description='test_description', image='test.jpg',
                                        creator=self.user)

    def test_add_comment(self):
        created_at = datetime.now()
        self.client.login(username='test_user', password="1@abcTest")
        response = self.client.post(reverse('insta:comment', kwargs={'pk': 1}), {
            'comment': 'test_comment'
        })
        self.assertEqual(200, response.status_code)
        self.assertIsInstance(response, JsonResponse)
        self.assertFalse(response.json()['has_error'])
        expected = '<div class="comment">\n' \
                   '    <span>\n' \
                   '        <a href="/users/1/profile">test_user </a>\n' \
                   '        <span class="comment-text">test_comment</span>\n' \
                   f'        <span class="comment-date">{created_at.strftime("%d-%m-%Y %H:%M")}</span>\n' \
                   '    </span>\n' \
                   '</div>'
        self.assertEqual(expected, response.json()['html_response'])
        comment = Comment.objects.get(pk=1)

        self.assertEqual('test_comment', comment.text)
        self.assertEqual(self.user, comment.creator)
        self.assertEqual(self.post, comment.post)
        comment.delete()

    def tearDown(self):
        self.user.delete()
        self.post.delete()
