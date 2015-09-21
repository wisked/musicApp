from django.forms import ModelForm
from .models import *


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']