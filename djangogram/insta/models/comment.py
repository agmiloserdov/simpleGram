from django.contrib.auth import get_user_model
from django.db import models


class Comment(models.Model):
    text = models.TextField(max_length=200, null=False, verbose_name='Комментарий', blank=False)
    creator = models.ForeignKey(get_user_model(), related_name='comments', on_delete=models.CASCADE,
                                verbose_name='Создатель')
    post = models.ForeignKey('insta.Post', related_name='comments', verbose_name='Комментарий к публикации',
                             on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False, verbose_name='Дата создания')

    def __str__(self):
        return f'Комментарий от {self.creator.username} к публикации : {self.post.title[:20]}'

    class Meta:
        verbose_name_plural = "Комментарии"
