from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views.generic import View

from insta.models.comment import Comment
from insta.models.post import Post


class AddCommentView(View):
    http_method_names = ['post']

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        user = get_user(self.request)
        post = get_object_or_404(Post, pk=kwargs['pk'])
        comment_text = request.POST.get('comment')
        if comment_text and len(comment_text) > 5:
            comment = Comment.objects.create(text=comment_text, creator=user, post=post)
            html = render_to_string(
                template_name='partial/comment/_comment.html',
                context={'comment': comment}
            )
            data_dict = {"html_response": html, "has_error": False}
            return JsonResponse(data_dict, status=200)
        else:
            return JsonResponse(
                {
                    "has_error": True,
                    "error_message": "Минимальная длина комментария 5 символов"
                },
                status=200
            )
