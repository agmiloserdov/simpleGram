from django.urls import path

from insta.views.comment import AddCommentView
from insta.views.like import LikeView
from insta.views.post import IndexView, CreatePostView, UpdatePostView, DeletePostView, PostView
from insta.views.subscriptions import SubscriptionView
from insta.views.user import ProfileView, ProfileSearchView, SubscriptionsSearchView

app_name = 'insta'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('posts/add', CreatePostView.as_view(), name='add'),
    path('posts/<int:pk>/edit', UpdatePostView.as_view(), name='edit'),
    path('posts/<int:pk>/delete', DeletePostView.as_view(), name='delete'),
    path('posts/<int:pk>', PostView.as_view(), name='post'),
    path('posts/<int:pk>/comment', AddCommentView.as_view(), name='comment'),
    path('posts/<int:pk>/like', LikeView.as_view(), name='like'),
    path('users/<int:pk>/profile', ProfileView.as_view(), name='profile'),
    path('users/', ProfileSearchView.as_view(), name='search'),
    path('users/<int:pk>/subscribe', SubscriptionView.as_view(), name='subscribe'),
    path('users/<int:pk>/subscr', SubscriptionsSearchView.as_view())
]
