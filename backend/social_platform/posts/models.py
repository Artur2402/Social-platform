from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail


class Post(models.Model):
  author = models.ForeignKey(
      settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  title = models.CharField(max_length=255)
  content = models.TextField()
  category = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updater_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title


@receiver(post_save, sender=Post)
def send_post_creation_email(sender, instance, created, **kwargs):
  if created:
    'New Post Created',
    f'A new post titled "{instance.title}" has been created by {instance.author.username}.',
    settings.EMAIL_HOST_USER,
    [instance.author.email],
    fail_silently = False,


class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  author = models.ForeignKey(
      settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updater_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.author.username} on {self.post.title}"
