from django.db import models
from django.conf import settings
from django.contrib.auth.models import User  # for access to users
from django.contrib.auth import get_user_model  # for access to users
from django.urls import reverse  # for absolute url


class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.pk)])


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author) + " " + str(self.id)


def get_absolute_url(self):
    return reverse('article_list', args=[str(self.pk)])

