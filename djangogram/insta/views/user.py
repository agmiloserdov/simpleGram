from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import DetailView, View

from accounts.models import InstaUser
from insta.forms import PostForm


class ProfileView(DetailView):
    template_name = 'user/profile.html'
    model = get_user_model()
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.object
        context[self.context_object_name] = profile
        context['posts_count'] = profile.posts.count()
        if self.request.user.pk == self.object.pk:
            context['form'] = PostForm()
        return context


class ProfileSearchView(View):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            search = request.GET.get('search')
            users = []
            if search:
                users = User.objects.filter(Q(username__istartswith=search) | Q(first_name__istartswith=search))
            data_dict = render_search_partial(users)
            return JsonResponse(data=data_dict, safe=False)
        else:
            return redirect('insta:index')


class SubscriptionsSearchView(View):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        is_followers = request.GET.get('followers')
        is_subscriptions = request.GET.get('subscriptions')
        users = []
        if is_followers or is_subscriptions:
            profile = get_object_or_404(InstaUser, pk=kwargs['pk'])
            if is_followers:
                profiles = profile.followers.values_list('user', flat=True)
            else:
                profiles = profile.subscriptions.values_list('user', flat=True)
            users = User.objects.filter(pk__in=profiles)
        if request.is_ajax():
            data_dict = render_search_partial(users)
            return JsonResponse(data=data_dict, safe=False)
        else:
            return redirect('insta:profile', pk=kwargs['pk'])


def render_search_partial(users):
    html = render_to_string(
        template_name='partial/user/_user_search_partial.html',
        context={'users': users}
    )
    return {"html_response": html}
