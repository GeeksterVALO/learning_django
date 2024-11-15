from django import forms
from django.forms import ModelForm

class CommentArticleForm(forms.Form):
    content = forms.CharField(label='Комментарий') # Текст комментария

class ArticleCommentForm(ModelForm):
    class Meta:
        model = ArticleComment
        fields = ['content']