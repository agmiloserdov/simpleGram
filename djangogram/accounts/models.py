from django.contrib.auth import get_user_model
from django.db import models


class InstaUser(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE,
                                verbose_name='Пользователь')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Аватар')
    subscriptions = models.ManyToManyField('accounts.InstaUser', related_name='followers', verbose_name='Подписки')

    @property
    def subscriptions_count(self):
        return self.subscriptions.count()

    @property
    def followers_count(self):
        return self.followers.count()

    def __str__(self):
        return "Профиль пользователя " + self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
