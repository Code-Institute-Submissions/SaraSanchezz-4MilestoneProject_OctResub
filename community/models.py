from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=700)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
