from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('watch/<int:pk>/', views.video_detail, name="video-detail"),
]
