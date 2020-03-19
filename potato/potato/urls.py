"""potato URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from social import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home,name='home'),
    path('post/new/',views.newpost,name='newpost'),
    path('explore/',views.explore,name='explore'),
    path('explore/createhashtags/',views.createhashtag,name='createhashtag'),
    path('explore/hashtag/<slug:slug>',views.linkhashtag,name='link'),
    path('addcommment/<slug:slug>',views.comment,name='comment'),
    path('<slug:slug>',views.profilevisit,name='profilevisit'),
    path('explore/hashtag/like/<slug:slug>',views.like,name='like'),
    path('follow/<slug:slug>',views.followers,name='followers')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)