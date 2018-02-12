from django import forms

from .models import newsEntry

class PostForm(forms.ModelForm):

    class Meta:
        model  = newsEntry
        fields = ('content', 'author', 'date')