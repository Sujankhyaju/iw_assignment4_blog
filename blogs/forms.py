from django import forms

from .models import Blogs


class CreatePostForm(forms.ModelForm):

    class Meta:
        model = Blogs
        fields = ['title', 'author', 'content']
        