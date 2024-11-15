from django import forms
from django.forms import ModelForm
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) > 200:
            raise forms.ValidationError("Название статьи не должно превышать 200 символов.")
        return name