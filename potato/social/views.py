from django.shortcuts import render,redirect
from .forms import *

from .models import Post,Explore,Like,Follow,Comment as Comments,Music,Storyplayviews,Chat,Quickpost,Notification
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from django.shortcuts import *
from datetime import date
from django.http import JsonResponse,HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from ipaddr import client_ip
import hashlib
# Create your views here.
@login_required(login_url='login')
def home(request):
    hashtag = Explore.objects.all()
    post=Post.objects.all()
    hash=Explore.objects.all()

    #return render(request,'home.html',{'hashtag':hashtag,'post':post,'hash':hash})
    return redirect('link','covid19')

@login_required(login_url='login')
def newpost(request):
    video=''
    if request.method == 'POST':
        form = Posting(request.POST,request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user =request.user

            video = post.pic
            if str(video).split(".")[-1] == 'mp4':
                post.video = 'True'


            form.save()
            return redirect('link','covid19')
    else:
        form = Posting()
        music=Music.objects.all()
    return render(request, 'posts/post.html', {'form': form})
@login_required(login_url='login')
def explore(request):
    hashtag = Explore.objects.all()
    hash=Explore.objects.all()
    post=Post.objects.all()
    post=post.order_by('date_posted').reverse()
    userlist=User.objects.all()

    return render(request,'explore.html',{'hashtag':hashtag,'post':post,'hash':hash})
@login_required(login_url='login')
def linkhashtag(request,slug='covid19'):
    room=Explore.objects.get(slug='covid19')
    hash=Explore.objects.all()
    post=Post.objects.filter(hashtag=slug)[:4]
    likers = Like.objects.all
    dic={'post':post}
    users=Profile.objects.get(user=request.user)
    users.ipadress=client_ip(request)
    users.save()
    print(post)

    noti=Like.objects.filter(user=request.user)
    followpost=Post.objects.filter(user__following__follower=request.user)
    followpost=followpost.order_by('date_posted').reverse()
    countfollowpost=Post.objects.filter(user__following__follower=request.user).count()
    userlist=Profile.objects.all()
    comments=Post.objects.all()
    likecountpost=0
    commentcountpost=0
    for live in followpost:
        live.user_namepost=str(live.user)
        live.namepost=str(live.user.profile.name)
        live.postprofilepic='https://potatomello.pythonanywhere.com/media/'+str(live.user.profile.pic)
        live.verified=str(live.user.profile.verified)
        likecountpost=Like.objects.filter(post=live).count()
        commentcountpost=Comments.objects.filter(post=live).count()
        live.likepost=str(likecountpost)
        live.commentpost=str(commentcountpost)
        live.save()
    video=''
    if request.method == 'POST':
        form = Posting(request.POST,request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user =request.user
            video = post.pic
            if str(video).split(".")[-1] == 'mp4':
                post.video = 'True'


            form.save()
            post=Post.objects.filter(hashedshaurl='False')
            for iteration in post:
                if iteration.hashedshaurl=='False':
                    postid=iteration.id
                    hashid=bytes(str(postid),'utf-8')
                    iteration.hashedshaurl=hashlib.sha224(hashid).hexdigest()
                    iteration.save()


            return redirect('link','covid19')
    else:
        form = Posting()

    quickpost = Quickpost.objects.all()
    quickpost=quickpost.order_by('time').reverse()
    countn=0
    n = Notification.objects.filter(viewed='False')
    for notification in n:
        if notification.foruser in request.user.username:
            countn+=1

    return render(request,'hashtagroom.html',{'form':form,'room':room,'post':post,'hash':hash,'likers':likers,'users':users,'noti':noti,'followpost':followpost,'countfollowpost':countfollowpost,'userlist':userlist,'quickpost':quickpost,'countn':countn,'notification':n})
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
    post=Post.objects.get(hashedshaurl=slug)

    if request.method == 'POST':
        form = Comment(request.POST, request.FILES)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.user_name = request.user.profile.name
            comment.profilepic =request.user.profile.pic
            comment.verified = request.user.profile.verified



            form.save()
            return redirect('link',post.hashtag)
    else:
        form = Comment()

    if request.is_ajax():
        comments=Comments.objects.get(user_id=slug).all()
        return JsonResponse({'comment':list(comments.values())})
    return  render(request,'comment.html',{'post':post,'form':form,'slug':slug})
def profilevisit(request,slug):
    u=slug
    if u.isnumeric():
        user=User.objects.get(id=slug)
    else:
        user =User.objects.get(username=slug)

    comment=Comments.objects.all().count()
    followers=Follow.objects.filter(following=user).count()
    followerslist=Follow.objects.filter(following=user)

    p=0
    users=request.user
    post=Post.objects.filter(user=user)
    post=post.order_by('date_posted').reverse()
    following='False'
    for i in post:
        p+=comment
    for followpeople in followerslist:
        if followpeople.follower.profile.name in request.user.profile.name:
            following ='True'
    return render(request, 'profilevisit.html',{'post': post,'user':user,'followers':followers,'p':p,'users':users,'followerslist':followerslist,'following':following})
def signuphash(request,slug):
    room=Explore.objects.get(slug='covid19')
    hash=Explore.objects.all()
    post=Post.objects.filter(hashtag=slug)
    post=post.order_by('date_posted').reverse()
    likers = Like.objects.all
    dic={'post':post}
    return render(request,'hashtagroomsignup.html',{'room':room,'post':post,'hash':hash,'likers':likers})


def like(request,slug):
    post=Post.objects.get(id=slug)
    user=Profile.objects.get(user=request.user)
    notification = Notification.objects.all()
    noti,creat = Notification.objects.get_or_create(likeuser=user.user,post=post,foruser=post.user_namepost)
    obj,created=Like.objects.get_or_create(post=post,user=user.user)
    if request.is_ajax():
        post=Post.objects.get(id=slug)
        user=Profile.objects.get(user=request.user)
        notification = Notification.objects.all()
        noti,creat = Notification.objects.get_or_create(likeuser=user.user,post=post,foruser=post.user_namepost)
        obj,created=Like.objects.get_or_create(post=post,user=user.user)
        likecount=post.like.count()
        likecount+1
        return HttpResponse(likecount)
    return redirect('link','covid19')
def followers(request,slug):
   users=Profile.objects.get(user_id=slug)
   obj,created=Follow.objects.get_or_create(following=users.user,follower=request.user)
   return redirect('profilevisit',slug=users.user_id)

def trending(request):
    post=Post.objects.filter(hashtag='covid19')
    post=post.order_by('date_posted').reverse()
    userlist=User.objects.all()
    l=[]
    for i in post :
        l.append(i)

    for live in post:
        live.user_namepost=str(live.user)
        live.namepost=str(live.user.profile.name)
        live.postprofilepic='https://potatomello.pythonanywhere.com/media/'+str(live.user.profile.pic)
        live.verified=str(live.user.profile.verified)
        likecountpost=Like.objects.filter(post=live).count()
        commentcountpost=Comments.objects.filter(post=live).count()
        live.likepost=str(likecountpost)
        live.commentpost=str(commentcountpost)
        live.save()
    data={'post':l}

    return JsonResponse({'post':list(post.values())} ,safe=False)

def chat(request):
    chatq = Chat.objects.all()
    users=User.objects.all()[11:]
    if request.is_ajax():
        chatq=Chat.objects.all()
        print(chatq.values())
        return JsonResponse({'chat':list(chatq.values())})
    if request.method == 'POST':
        form = Chating(request.POST)

        if form.is_valid():
            chatform = form.save(commit=False)
            chatform.user = request.user
            chatform.name = request.user.profile.name
            chatform.urlimage=request.user.profile.pic
            form.save()
            return redirect('chat')
    else:
        form = Chating()


    return render(request,'posts/yt.html',{'form':form,'chatq':chatq,'users':users})
def quicklike(request,slug):
    post=Quickpost.objects.get(id=slug)
    user=Profile.objects.get(user=request.user)

    obj,created=Like.objects.get_or_create(user=user.user,post=post)


    return redirect('link','covid19')

def quickcomment(request,slug):
    post=Quickpost.objects.get(id=slug)
    if request.method == 'POST':
        form = QuickComment(request.POST, request.FILES)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            form.save()
            return redirect('comment',post.id)
    else:
        form = QuickComment()


    return  render(request,'comment.html',{'post':post,'form':form,'slug':slug})
def notification(request):
    if request.is_ajax():
        notification=Notification.objects.filter(foruser=request.user.profile.user)
        for i in notification:
            i.viewed = 'True'
            i.save()
        n=Notification.objects.filter(foruser=request.user.profile.user)
        n=n.order_by('time').reverse()
        return render(request,'notificationf.html',{'notification':n})
    notification=Notification.objects.filter(foruser=request.user.profile.user)
    for i in notification:
        i.viewed = 'True'
        i.save()

    n = Notification.objects.filter(foruser=request.user.profile.user)
    n=n.order_by('time').reverse()
    return render(request,'notificationf.html',{'notification':n})
def emailsend(request,slug):
    subject = 'Potato'
    username=request.user
    email=str(username)+'Two factor authentication is enabled in potato with this email .It wasn\'t you , You can disable this email address from this url potatomello.pythonanywhere.com'
    send_mail('Potato',email,'email@email.com',[slug],fail_silently=False)
    return redirect('link','covid19')
def emaildont(request):
    request.user.profile.emaildontshowagain = 'True'
    return redirect('link','covid19')

