from django.urls import path
from . import views

urlpatterns = [
  #dynamic urls
  #str can be an int or slug as well
  #path('room', views.mainroom, name="mainroom"),
  #path('room/<str:pk>/', views.room, name="room"),
  path('', views.home_view, name="home"),
  path('profile/', views.profile_view, name="profile"),
  path('dashboard/', views.profile_view, name="dashboard"),
  path('accounts/register', views.register_view, name='register'),
]