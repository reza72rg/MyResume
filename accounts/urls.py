from django.urls import path
#from accounts.views import *
from accounts.views import * 


app_name = 'accounts'

urlpatterns = [
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',UserLogOut.as_view(),name='logout'),

    #path('singup/',singup_view,name='singup'),
    path('register/',RegisterView.as_view(),name='singup'),
    path('changepassword/',UserPasswordResetView.as_view(),name='changepassword'),
	path('reset/done/', UserPasswordResetDoneView.as_view(), name='password_reset_done'),
	path('confirm/<uidb64>/<token>', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('confirm/complete', UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
]