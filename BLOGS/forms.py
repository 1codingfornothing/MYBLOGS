from django import forms
from BLOGS.models import Comment

class NewCommentForm(forms.ModelForm):


    class Meta:
        model = Comment

        fields = ['name', 'name']