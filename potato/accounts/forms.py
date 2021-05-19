from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


locker=[('on','ON'),('off','OFF')]

class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=30,required=True)
    year = ['2003']
    #born = forms.DateField(label='Date of birth', widget=forms.SelectDateWidget(years=year))
    class Meta:
        model = User
        fields = ('username','email', 'name', 'password1', 'password2' )


class ProfileForm(forms.ModelForm):
    year = ['2003']
    born = forms.DateField(label='Date of birth', widget=forms.SelectDateWidget(years=year))
    lockprofile =forms.CharField(label='Private account?',initial='off', widget=forms.Select(choices=locker))
    class Meta:
        model = Profile
        fields = ('bio', 'name','pic','status','born')
class EmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields =('email',)
class ResetForm(forms.ModelForm):
    emailreset=forms.CharField(max_length=100,required=True)

    class Meta:
        model=Profile
        fields=('emailreset',)
class PasswordresetForm(forms.ModelForm):
    newpassword=forms.CharField(max_length=32, widget=forms.PasswordInput)
    confirmpassword=forms.CharField(max_length=32, widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('newpassword','confirmpassword')
