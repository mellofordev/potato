from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=30,required=True)

    class Meta:
        model = User
        fields = ('username', 'name', 'password1', 'password2', )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'bio', 'name','pic')