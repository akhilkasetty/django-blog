from .models import Post
from django import forms

class Postform(forms.ModelForm):

    class Meta:
        method=Post
        fields=('title','content',)
