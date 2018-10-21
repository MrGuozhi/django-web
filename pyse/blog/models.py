from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(blank=True, default=timezone.now)
    publich_date = models.DateTimeField(blank=True, null=True)

    def publiched(self):
        self.publich_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
