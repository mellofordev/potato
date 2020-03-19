from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm,ProfileForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from social.models import Post
from django.contrib.auth.models import User

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.name = form.cleaned_data.get('name')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
@login_required

def profile(request):
    post=Post.objects.filter(user=request.user)
    post=post.order_by('date_posted').reverse()

    print(post)
    return render(request,'profiles/profile.html',{'post':post})
def update_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return render(request,'profiles/profile.html')
        else:
            pass

    else:

        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/updateprofile.html', {

        'profile_form': profile_form
    })