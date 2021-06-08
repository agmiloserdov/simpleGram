from django.contrib import admin

from insta.models.comment import Comment
from insta.models.like import Like
from insta.models.post import Post

admin.register(Post)
admin.register(Comment)
admin.register(Like)

