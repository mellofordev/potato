from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class Post(models.Model):
    post=models.TextField(max_length=10000000,default='',null=True,blank=True)
    user_namepost=models.CharField(max_length=100,default=' ',blank=True)
    namepost=models.CharField(max_length=100,default=' ',blank=True)
    verified=models.CharField(max_length=5,default='False',blank=True)
    postprofilepic=models.CharField(max_length=10000,default=' ',blank=True)
    likepost=models.CharField(max_length=1000,default='',blank=True)
    commentpost=models.CharField(max_length=1000,default='',blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    pic=models.FileField(upload_to='postpics',null=True,blank=True)
    hashtag=models.CharField(max_length=50,default='covid19')
    yt=models.CharField(max_length=5,default='False',blank=True)
    src=models.CharField(max_length=100,default='',blank=True)
    image1 = models.ImageField(upload_to='facemash', blank=True)
    image2 = models.ImageField(upload_to='facemash', blank=True)
    facemash=models.CharField(max_length=5,default='False')
    musicurl=models.CharField(max_length=100000,default='')
    video = models.CharField(max_length =5,default='False')
    blocked=models.CharField(max_length=5,default='False')
    blockreport=models.CharField(max_length=150,default='This post includes potentially  sensitive content')
    hashedshaurl=models.CharField(max_length=56,default='False')


    def __str__(self):
        return self.post
class Explore(models.Model):
    hashtags=models.CharField(max_length=50,default='')
    slug=models.SlugField(default='',unique=True)
    image=models.ImageField(upload_to='hashtagpics',null=True,blank=True)
    def __str__(self):
        return self.hashtags
class Comment(models.Model):
    post = models.ForeignKey('social.Post', on_delete=models.CASCADE,related_name='comment')
    comment=models.CharField(max_length=100,default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50,default=' ')
    profilepic = models.CharField(max_length=10000,default= ' ' )
    verifiedprofile = models.CharField(max_length=5,default='False')

    def __str__(self):
        return self.comment
class Like(models.Model):
    post=models.ForeignKey('social.Post',on_delete=models.CASCADE,related_name='like')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    color=models.CharField(max_length=10,default=' ')
    def __str__(self):
        return self.user.profile.name

class Music(models.Model):
    music=models.FileField(upload_to='music',validators=[FileExtensionValidator(allowed_extensions=['mp3'])])
    name=models.CharField(max_length=100,default='')

    def __str__(self):
        return self.name
class Storyplayviews(models.Model):
    post = models.ForeignKey('social.Post', on_delete=models.CASCADE, related_name='playviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.profile.name
class Follow(models.Model):
    following=models.ForeignKey(User,on_delete=models.CASCADE,related_name='following')
    follower=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.follower.profile.name

class Chat(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=150,default='user')
    text=models.CharField(max_length=100,default='')
    urlimage=models.CharField(max_length=10000,default='default.png')
    time=models.DateTimeField(default=timezone.now)
    privatechat=models.CharField(max_length=4,default='False')
    def __str__(self):
        return self.user.profile.name
class Quickpost(models.Model):
    quickpost=models.CharField(max_length=100,default='')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    time= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.quickpost
class QuickLike(models.Model):
    post=models.ForeignKey('social.Quickpost',on_delete=models.CASCADE,related_name='Quicklike')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    time=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.user.profile.name
class Notification(models.Model):
    post= models.ForeignKey('social.Post', on_delete=models.CASCADE, related_name='notificationpost')
    likeuser = models.ForeignKey(User,on_delete=models.CASCADE,related_name='likeuser')
    viewed = models.CharField(max_length=5,default='False')
    foruser = models.CharField(max_length=150,default='')
    time=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.post.user_namepost
