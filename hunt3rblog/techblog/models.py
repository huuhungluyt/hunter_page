from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    creater= models.ForeignKey(User, null=True, related_name='topics', on_delete=models.SET_NULL)
    title=models.CharField(max_length=256)
    description= models.CharField(max_length=1024)
    time_created=models.DateTimeField(auto_now_add=True)
    time_updated= models.DateTimeField(auto_now=True)
    class Meta:
        ordering=('-time_created',)

    def __str__(self):
        return "%s"%self.title


class Post(models.Model):
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE)
    title=models.CharField(max_length=256)
    poster=models.ForeignKey(User, null=True, related_name='posts', on_delete=models.SET_NULL)
    content=models.TextField(max_length=20480)
    time_created=models.DateTimeField(auto_now_add=True)
    time_updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s"%self.title

    class Meta:
        ordering=('-time_created',)



class Comment(models.Model):
    post= models.ForeignKey(Post, on_delete=models.CASCADE)
    reader= models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    content= models.CharField(max_length=512)
    time_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s"%self.content

    class Meta:
        ordering=['-time_created']


class Log(models.Model):
    ACTION_LIST=[
        ('hit', 'accessed blog'),
        ('cmt', 'commented post'),
        ('pos', 'posted'),
    ]
    ip_addr=models.CharField(default='unknown', max_length=16)
    accessed_url=models.CharField(null=True, max_length=256)
    user=models.ForeignKey(User, null=True, related_name='logs', on_delete=models.SET_NULL)
    action=models.CharField(choices=ACTION_LIST, default='hit', max_length=3)
    message = models.CharField(default='nothing', max_length=512)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-time']