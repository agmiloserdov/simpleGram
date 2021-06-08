from django.contrib.auth import get_user
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from insta.forms import PostForm
from insta.models.post import Post


class IndexView(LoginRequiredMixin, ListView):
    context_object_name = 'posts'
    template_name = 'post/index.html'
    model = Post
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        user = get_user(self.request)
        if user.is_superuser:
            posts = queryset.all()
        else:
            profile = get_user(self.request).profile
            posts = queryset.filter(creator_id__in=profile.subscriptions.values_list("user_id", flat=True))
        return posts


class CreatePostView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    http_method_names = ['post', 'get']
    model = Post
    template_name = 'post/add.html'

    def form_valid(self, form):
        user = get_user(self.request)
        post = form.save(commit=False)
        post.creator = user
        post.save()
        return redirect('insta:post', pk=post.pk)


class UpdatePostView(LoginRequiredMixin, UpdateView):
    context_object_name = 'post'
    template_name = 'post/edit.html'
    form_class = PostForm
    model = Post

    def form_valid(self, form):
        user = get_user(self.request)
        post = form.save(commit=False)
        if post.creator.pk == user.pk:
            post.save()
            return redirect('insta:post', pk=post.pk)
        else:
            raise ValidationError('Только создатель может изменять публикацию')

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        return self.render_to_response(context)


class DeletePostView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    http_method_names = ['post']
    model = Post

    def test_func(self):
        return self.get_object().creator == self.request.user

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        if post:
            post.delete()
            return JsonResponse({'is_deleted': True}, status=200)
        else:
            return JsonResponse({'is_deleted': False}, status=200)


class PostView(DetailView):
    template_name = 'post/post.html'
    model = Post

