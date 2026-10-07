from django import forms
from django.utils import timezone

from .models import Post


class PostForm(forms.ModelForm):

    published_date = forms.SplitDateTimeField(initial=timezone.now)

    class Meta:
        model = Post
        fields = ('title', 'text', 'is_published', 'published_date')

