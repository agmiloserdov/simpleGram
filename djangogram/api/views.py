from django.contrib.auth.models import User
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api.serializers.user_serializer import UserSerializer


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

