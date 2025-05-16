from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('challenge/<int:pk>/', views.challenge_detail, name='challenge_detail'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]
