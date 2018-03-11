from django.contrib import admin
from django import forms

from .models import Topic, Post, Comment

# Register your models here.

# class PostForm(forms.ModelForm):
#     content= forms.CharField(widget=forms.Textarea)
#     class Meta:
#         model=Post

# class BlogAdmin(admin.ModelAdmin):
#     form = PostForm
#     # filter_horizontal = ('tags',)

admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(Comment)