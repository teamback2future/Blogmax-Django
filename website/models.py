from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=250)
    article_image = models.FileField(blank=True, null=True,verbose_name="Add Picture")

    def __str__(self):
        return self.title
