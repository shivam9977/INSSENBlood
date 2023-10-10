from django.urls import path
from. import views

urlpatterns = [
    path('', views.home , name='home'),
    path("become_donor/", views.become_donor, name="become_donor"),
]