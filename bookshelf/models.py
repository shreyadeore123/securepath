from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    published_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookshelf_owned')  # ✅ DIFFERENT

    def __str__(self):
        return self.title
