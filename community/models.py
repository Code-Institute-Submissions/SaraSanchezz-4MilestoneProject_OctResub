from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    body = models.TextField(max_length=700, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(null=False, blank=True)
    body = models.TextField(null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']
