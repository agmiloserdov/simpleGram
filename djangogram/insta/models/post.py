from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    creator = models.ForeignKey(get_user_model(), related_name='posts', on_delete=models.CASCADE,
                                verbose_name='Создатель')
    title = models.CharField(max_length=200, null=False, verbose_name='Заголовок', blank=False)
    description = models.TextField(max_length=200, null=False, verbose_name='Описание', blank=False)
    image = models.ImageField(null=False, upload_to='posts', blank=False, verbose_name='Фото публикации')
    created_at = models.DateTimeField(auto_now_add=True, null=False, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, null=False, verbose_name='Дата изменения')

    def __str__(self):
        return f'Публикация {self.title[:20]}'

    @property
    def comments_count(self):
        return self.comments.count()

    @property
    def likes_count(self):
        return self.likes.count()

    class Meta:
        verbose_name_plural = "Публикации"
