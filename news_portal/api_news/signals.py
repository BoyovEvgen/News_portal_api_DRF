from django.core.exceptions import ValidationError
from django.db.models.signals import pre_delete, pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Post, PostImage

User = get_user_model()


@receiver(pre_delete, sender=User)
def delete_author_posts(sender, instance, **kwargs):
    if hasattr(instance, 'posts'):
        new_author = User.objects.filter(is_staff=True).first()
        if not new_author:
            raise ValidationError("Неможливо видалити автора. Немає іншого адміністратора для назначення постам створених видаляємим автором.")
        instance.posts.update(author=new_author)


@receiver(pre_save, sender=PostImage)
def update_main_image(sender, instance, **kwargs):
    if instance.is_main:
        sender.objects.filter(post=instance.post, is_main=True).exclude(id=instance.id).update(is_main=False)


@receiver(post_save, sender=PostImage)
def ensure_main_image_exists(sender, instance, created, **kwargs):
    if created and not sender.objects.filter(post=instance.post, is_main=True).exists():
        instance.is_main = True
        instance.save()

