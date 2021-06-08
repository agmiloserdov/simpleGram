from django.contrib.auth import login, authenticate, logout, get_user_model, get_user
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View, UpdateView

from accounts.forms import UserRegisterForm, UserUpdateForm, ProfileChangeForm, PasswordChangeForm
from accounts.models import InstaUser


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = UserRegisterForm()
        return render(request, 'register.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('insta:index')
        else:
            return render(request, 'register.html', context={'form': form})


class LoginView(View):
    context = {}

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        next_url = self.get_next_url(request)
        if user is not None:
            login(request, user)
            if not next_url:
                next_url = reverse('insta:index')
            return redirect(next_url)
        else:
            self.context['has_error'] = True
            return render(request, 'login.html', context=self.context)

    def get(self, request, *args, **kwargs):
        next_url = self.get_next_url(request)
        if next_url:
            self.context['next'] = next_url
        self.context['has_error'] = False
        return render(request, 'login.html', context=self.context)

    def get_next_url(self, request):
        next_url = request.POST.get('next')
        if not next_url:
            return request.GET.get('next')
        else:
            return None


class LogoutView(View):
    def get(self, request):
        logout(request)
        next_url = request.GET.get('next')
        if not next_url:
            next_url = reverse('accounts:login')
        return redirect(next_url)


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    def get_object(self, queryset=None):
        return self.request.user

    model = get_user_model()
    form_class = UserUpdateForm
    template_name = 'edit.html'
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        if 'profile_form' not in kwargs:
            kwargs['profile_form'] = self.get_profile_form()
        kwargs['current_photo'] = self.request.user.profile.avatar
        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        profile_form = self.get_profile_form()
        if form.is_valid() and profile_form.is_valid():
            return self.form_valid(form, profile_form)
        else:
            return self.form_invalid(form, profile_form)

    def form_valid(self, form, profile_form):
        response = super().form_valid(form)
        profile_form.save()
        return response

    def form_invalid(self, form, profile_form):
        context = self.get_context_data(form=form, profile_form=profile_form)
        return self.render_to_response(context)

    def get_profile_form(self):
        form_kwargs = {'instance': self.object.profile}
        if self.request.method == 'POST':
            form_kwargs['data'] = self.request.POST
            form_kwargs['files'] = self.request.FILES
        return ProfileChangeForm(**form_kwargs)

    def get_success_url(self):
        return reverse('insta:profile', kwargs={'pk': self.object.pk})


class ChangePasswordView(LoginRequiredMixin, UpdateView):
    def get_object(self, queryset=None):
        return self.request.user

    model = get_user_model()
    template_name = 'change_password.html'
    form_class = PasswordChangeForm
    context_object_name = 'user_obj'

    def get_success_url(self):
        return reverse('accounts:login')
