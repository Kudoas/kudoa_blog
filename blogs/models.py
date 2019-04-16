from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField('カテゴリー名', max_length=50)
    pub_date = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('題名', max_length=50)
    text = models.TextField('本文')
    pub_date = models.DateTimeField('作成日', default=timezone.now)
    category = models.ForeignKey(
        Category, verbose_name='カテゴリー', on_delete=models.PROTECT
    )

    def summary(self):
        return self.text[:50]

    def __str__(self):
        return self.title
