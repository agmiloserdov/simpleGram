from django.contrib.auth import get_user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import View

from accounts.models import InstaUser


class SubscriptionView(LoginRequiredMixin, View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        user = get_user(self.request)
        follower = get_object_or_404(InstaUser, pk=user.pk)
        profile = get_object_or_404(InstaUser, pk=kwargs['pk'])
        if follower not in profile.followers.all():
            profile.followers.add(follower)
            is_subscribed = True
        else:
            profile.followers.remove(follower)
            is_subscribed = False
        profile.save()
        return JsonResponse({"is_subscribed": is_subscribed}, status=200)
