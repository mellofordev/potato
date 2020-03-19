from django.shortcuts import render,redirect
from .forms import Posting,Exploreform,Comment
from .models import Post,Explore,Like,Followers,Comment as Comments
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from django.shortcuts import *
# Create your views here.
def home(request):
    posts = Post.objects.all()
    posts= posts.order_by('date_posted').reverse()
    lists={'posts':posts}
    print(lists)
    return render(request,'home.html',lists)
@login_required

def newpost(request):

    if request.method == 'POST':
        form = Posting(request.POST,request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user =request.user
            form.save()
            return redirect('explore')
    else:
        form = Posting()
    return render(request, 'posts/post.html', {'form': form})
def explore(request):
    hashtag = Explore.objects.all()
    post=Post.objects.all()
    hash=Explore.objects.all()
    return render(request,'explore.html',{'hashtag':hashtag,'post':post,'hash':hash})
def linkhashtag(request,slug):
    room=Explore.objects.get(slug=slug)
    hash=Explore.objects.all()
    post=Post.objects.filter(hashtag=slug)
    post=post.order_by('date_posted').reverse()
    likers = Like.objects.all
    dic={'post':post}
    users=Profile.objects.get(user=request.user)
    print(post)


    return render(request,'hashtagroom.html',{'room':room,'post':post,'hash':hash,'likers':likers,'users':users})
def createhashtag(request):
    if request.method == 'POST':
        form = Exploreform(request.POST,request.FILES)

        if form.is_valid():


            form.save()
            return redirect('explore')
    else:
        form = Exploreform()
    return render(request,'hashtags.html',{'form':form})

def comment(request,slug):
    post=Post.objects.get(id=slug)

    if request.method == 'POST':
        form = Comment(request.POST, request.FILES)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            form.save()
            return redirect('link',post.hashtag)
    else:
        form = Comment()


    return  render(request,'comment.html',{'post':post,'form':form,'slug':slug})
def profilevisit(request,slug):

    user =Profile.objects.get(user=slug)
    comments=Comments.objects.all().count()
    followers=Followers.objects.all().count()




    post=Post.objects.filter(user=user.user)
    post=post.order_by('date_posted').reverse()
    return render(request, 'profilevisit.html',{'post': post,'user':user,'comment':comments,'followers':followers})
def like(request,slug):
    post=Post.objects.get(id=slug)
    user=Profile.objects.get(user=request.user)

    Like.objects.create(post=post,user=user.user)


    return redirect('link',post.hashtag)
def followers(request,slug):
    post=Post.objects.get(id=slug)
    users=Profile.objects.get(user=request.user)

    Followers.objects.create(followers=users.user)




    return redirect('link',post.hashtag)


