import os

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

from insta.models import Post


@receiver(post_delete, sender=Post)
def auto_delete_file_on_post_delete(sender, instance, **kwargs):
    instance.image.delete(False)


@receiver(models.signals.pre_save, sender=Post)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_image = sender.objects.get(pk=instance.pk).image
    except sender.DoesNotExist:
        return False
    new_image = instance.image
    if not old_image == new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)
