from django.urls import path

from . import views as accounts_views


urlpatterns = [
    path('signup/', accounts_views.signup, name='signup'),
    path('profileupdate/',accounts_views.update_profile,name='profileupdate'),
    path('profile/',accounts_views.profile,name='profile')
]
