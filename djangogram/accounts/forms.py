from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password, password_changed
from django.core.validators import FileExtensionValidator, EmailValidator

from accounts.models import InstaUser
from insta.views.validators.filesizevalidator import FileSizeValidator


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label="Пароль", strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Подтвердите пароль", required=True, widget=forms.PasswordInput,
                                       strip=False)
    email = forms.CharField(label="Электронная почта", strip=False, required=True, widget=forms.EmailInput,
                            validators=[EmailValidator(message="Некорректный email")])
    username = forms.CharField(label="Логин", strip=False, required=True, widget=forms.TextInput)
    first_name = forms.CharField(label="Имя", strip=False, required=True, widget=forms.TextInput)
    last_name = forms.CharField(label="Фамилия", strip=False, required=True, widget=forms.TextInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            InstaUser.objects.create(user=user)
        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm', 'first_name', 'last_name', 'email']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Email'}


class ProfileChangeForm(forms.ModelForm):
    birth_date = forms.DateField(
        label='Дата рождения',
        input_formats=['%d/%m/%Y'],
        widget=forms.TextInput(attrs={
            'class': 'datepicker',
            'data-date-format': "dd/mm/yyyy"
        })
    )
    avatar = forms.ImageField(widget=forms.FileInput, label="Фото профиля",
                              validators=[
                                  FileExtensionValidator(
                                      allowed_extensions=['jpg', 'jpeg']),
                                  FileSizeValidator(limit_value=5000,
                                                    message="Недопустимый размер файла!")

                              ])

    class Meta:
        model = InstaUser
        exclude = ['user', 'subscriptions']


class PasswordChangeForm(forms.ModelForm):
    password = forms.CharField(label="Новый пароль", strip=False, widget=forms.PasswordInput, validators=[
        validate_password, password_changed
    ])
    password_confirm = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput, strip=False)
    old_password = forms.CharField(label="Старый пароль", strip=False, widget=forms.PasswordInput)

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')
        return password_confirm

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.instance.check_password(old_password):
            raise forms.ValidationError('Старый пароль неправильный!')
        return old_password

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['password', 'password_confirm', 'old_password']