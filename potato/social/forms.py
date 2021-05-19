from django import forms
from .models import Post,Explore,Comment,Chat,Quickpost
from django.contrib.auth.models import User


class Posting(forms.ModelForm):
      class Meta:
          model =Post

          fields = ('post','pic')
class Exploreform(forms.ModelForm):
    class Meta:
        model=Explore
        fields=('hashtags','slug')
class Comment(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('comment',)
class Facemashing(forms.ModelForm):
    class Meta:
        model=Post
        fields=('image1','image2')
class Youtubeing(forms.ModelForm):
    class Meta:
        model=Post
        fields=('post','src',)
class Chating(forms.ModelForm):
    class Meta:
        model=Chat
        fields=('text',)
class Quickposting(forms.ModelForm):
    class Meta:
        model=Quickpost
        fields=('quickpost',)
