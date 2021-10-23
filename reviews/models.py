from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    rate = models.CharField(max_length=10, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    body = models.TextField(max_length=700, null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-rate']
