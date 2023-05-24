from django import forms
from posts.models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("username", "text")
    
class CreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "category", "content")  