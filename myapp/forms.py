from django import forms

from .models import newsEntry

# class PostForm(forms.ModelForm):

    # class Meta:
        # model  = newsEntry
        # fields = ('content', 'author', 'date')
        
        
class PostForm(forms.Form):
    
      content               = forms.CharField(required=True, widget=forms.Textarea())
      author                = forms.CharField(required = True)
      date                  = forms.CharField(required = True, widget=forms.TextInput())
      error_css_class       = 'error'
