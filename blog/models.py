from django.db import models
from django.utils import timezone


class Post(models.Model):
    #author = models.ForeignKey('auth.User')
    title = models.CharField('标题', max_length=200)
    text = models.TextField('正文')
    created_date = models.DateTimeField('创建时间', auto_now_add=True)
    published_date = models.DateTimeField('发布日期', blank=True, null=True)
    category = models.ForeignKey('Category', verbose_name='分类', blank=True, null=True)
    tags = models.ManyToManyField('Tag', verbose_name='标签', blank=True,)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField('昵称', max_length=200)
    text = models.TextField('内容')
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Category(models.Model):
    name = models.CharField('name',max_length=16)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField('name',max_length=16)

    def __str__(self):
        return self.name