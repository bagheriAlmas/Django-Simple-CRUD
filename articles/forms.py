from django import forms
from articles.models import Comment, Article


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', ]


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','body']