from django import forms

from .models import Comment


class CommentForm(forms.Form):
    content=forms.CharField( widget=forms.Textarea(attrs={'rows':4, 'style': 'resize:none;', 'placeholder':'Enter your comment...'}))