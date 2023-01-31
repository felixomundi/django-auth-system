from accounts.views import register,loginuser,logoutuser,activate,get_user_profile
from django.urls import path
from django.contrib.auth import views as auth_views
urlpatterns = [
    
    path('register',register, name='register'),
    path('login/',loginuser, name='login'),
    path('logout',logoutuser,name='logout'),     
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('my-profile',get_user_profile,name="profile"),  
    path('change-password/',auth_views.PasswordChangeView.as_view(template_name='accounts/change-password.html',
    success_url = '/'
    ), name='change-password'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), name="password_reset_complete"), 
    
    
]
