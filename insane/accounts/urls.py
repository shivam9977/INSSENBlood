from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signIn/', views.signIn, name='signIn'),
    path('signUp/', views.signUp, name='signUp'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('contactUs/', views.contactUs, name='contactUs'),
    path('blog/', views.blog, name='blog'),
    path('gall/', views.gall, name='gall'),
    path('whoweare/', views.whoweare, name='whoweare'),
    path('becomeDonar/', views.becomeDonor, name='becomeDonar'),
    path('findDonor/', views.findDonor, name='findDonor'),
    path('bookAppointment/', views.bookAppointment, name='bookAppointment'),
    

    
    
    
   
]
    