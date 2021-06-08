from django.contrib.auth import get_user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import View

from insta.models.like import Like
from insta.models.post import Post


class LikeView(LoginRequiredMixin, View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        user = get_user(self.request)
        post = get_object_or_404(Post, pk=kwargs['pk'])
        if not post.likes.filter(user=user).exists():
            Like.objects.create(user=user, post=post)
        else:
            like = Like.objects.get(user=user, post=post)
            like.delete()
        return JsonResponse({"like_count": post.likes.count()}, status=200)
