from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    post=models.TextField(max_length=10000000,default='')

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    pic=models.FileField(upload_to='postpics',null=True,blank=True)
    hashtag=models.CharField(max_length=50,default='')
    typ=models.CharField(max_length=5,default='',help_text="only video and image",blank=True)



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


    def __str__(self):
        return self.comment
class Like(models.Model):
    post=models.ForeignKey('social.Post',on_delete=models.CASCADE,related_name='like')
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.profile.name
class Followers(models.Model):
    followers=models.ForeignKey(User,on_delete=models.CASCADE,related_name='followers')

    time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.followers.profile.name

