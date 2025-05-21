from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.submission_detail, name='submission_detail'),
    path('<int:pk>/like/', views.like_submission, name='like_submission'),
]
