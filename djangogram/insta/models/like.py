from django.contrib.auth import get_user_model
from django.db import models


class Like(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='likes', on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    post = models.ForeignKey('insta.Post', related_name='likes', on_delete=models.CASCADE,
                             verbose_name='Публикация')

    def __str__(self):
        return f'Пользователю {self.user.username} понравилась публикация : {self.post.title[:20]}'

    class Meta:
        verbose_name_plural = "Лайки"
