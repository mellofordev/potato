from django.urls import path

from . import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', accounts_views.signup, name='signup'),
    path('profileupdate/',accounts_views.update_profile,name='profileupdate'),
    path('profile/',accounts_views.profile,name='profile'),
    path('edit/email/',accounts_views.editemail,name='editemail'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),name='reset_password'),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),

]
