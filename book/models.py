from django.db import models

class Book(models.Model):
    name = models.CharField('书名',max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)