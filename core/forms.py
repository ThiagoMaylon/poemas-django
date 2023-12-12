from django import forms
from .models import Post

class PostModelFrom(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'texto']