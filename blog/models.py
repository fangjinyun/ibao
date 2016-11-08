from django.db import models
from django.utils import timezone


class Post(models.Model):
    #author = models.ForeignKey('auth.User')
    title = models.CharField('标题', max_length=200)
    text = models.TextField('正文')
    created_date = models.DateTimeField('创建时间', auto_now_add=True)
    published_date = models.DateTimeField('发布日期', blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title