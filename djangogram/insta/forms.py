from django import forms
from django.core.validators import FileExtensionValidator, MinLengthValidator, MaxLengthValidator, \
    ProhibitNullCharactersValidator

from insta.models.post import Post
from insta.views.validators.filesizevalidator import FileSizeValidator


class PostForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput, label="Фото публикации",
                             validators=[
                                 FileExtensionValidator(
                                     allowed_extensions=['jpg', 'jpeg', 'png']),
                                 FileSizeValidator(limit_value=5000,
                                                   message="Недопустимый размер файла!")

                             ])
    title = forms.CharField(label="Заголовок", strip=False, required=True, widget=forms.TextInput,
                            validators=[
                                MinLengthValidator(limit_value=3),
                                MaxLengthValidator(limit_value=50),
                                ProhibitNullCharactersValidator()])
    description = forms.CharField(label="Описание", strip=False, required=True, widget=forms.Textarea,
                                  validators=[
                                      MinLengthValidator(limit_value=3),
                                      MaxLengthValidator(limit_value=500),
                                      ProhibitNullCharactersValidator()])

    class Meta:
        model = Post
        fields = ['title', 'description', 'image']
