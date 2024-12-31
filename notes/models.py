from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Note(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-updated',)
