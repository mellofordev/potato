from django import forms
from .models import Post,Explore,Comment
from django.contrib.auth.models import User


class Posting(forms.ModelForm):
      class Meta:
          model =Post

          fields = ('post','pic','hashtag','typ')
class Exploreform(forms.ModelForm):
    class Meta:
        model=Explore
        fields=('hashtags','slug')
class Comment(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('comment',)
