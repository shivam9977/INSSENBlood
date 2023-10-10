from django.urls import path
from . import views

urlpatterns = [
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('view_feedback/', views.view_feedback, name='view_feedback'),
]
