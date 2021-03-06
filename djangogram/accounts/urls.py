from django.urls import path
from .views import LoginView, LogoutView, RegisterView, UpdateProfileView, ChangePasswordView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('edit/', UpdateProfileView.as_view(), name='edit'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password')
]

