from django.forms import ModelForm, CharField

from .models import Comment


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)