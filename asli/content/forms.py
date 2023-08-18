from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('body',)

class UpdateCommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('body',)

class SearchHomeForm(forms.Form):
    search=forms.CharField()

class SearchListCoursesForm(forms.Form):
    search=forms.CharField()
    
class SearchListSingleVideoForm(forms.Form):
    search=forms.CharField()

class SearchListArticleForm(forms.Form):
    search=forms.CharField()


