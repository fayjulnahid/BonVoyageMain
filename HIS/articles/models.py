from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    sluge = models.SlugField()
    experties = models.TextField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(default="default.png", blank=True)


    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:50] + '...'

class Hospital(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()

    def __str__(self):
        return self.title