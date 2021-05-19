from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

User._meta.get_field('email')._unique = True
Status=(
        ('single','Single'),
        ('not','Prefer Not to say'),
        ('Interested in','Interestedin'),
        ('In a relationship','In a relationship')
)
locker=(('on','ON'),('off','OFF'))
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    name= models.CharField(max_length=50,null=True, blank=True)
    pic=models.ImageField(default='default.png',upload_to='profilepic',null='True')
    verified=models.CharField(default='False',max_length=5)
    status=models.CharField(max_length=100,default='',choices=Status)
    born =models.DateField(default=datetime.date.today,blank=True)
    email=models.CharField(max_length=100,default='',blank=True)
    emailconfirmed = models.CharField(max_length=5,default='False')
    emaildonotshowagain=models.CharField(max_length=5,default='False')
    blocked=models.CharField(max_length=5,default='False')
    ipadress=models.CharField(max_length=2000,default=' ')
    forcelock= models.CharField(max_length=3, choices=locker, default='off')
    def __str__(self):
        return self.name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


