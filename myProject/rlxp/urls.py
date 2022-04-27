from django.urls import path
from . import views

urlpatterns = [
  #dynamic urls
  #str can be an int or slug as well
  #path('room', views.mainroom, name="mainroom"),
  #path('room/<str:pk>/', views.room, name="room"),
  path('', views.home_view, name="home"),
  path('profile/', views.profile_view, name="profile"),
  path('dashboard/', views.dashboard_view, name="dashboard"),
  path('accounts/register', views.register_view, name='register'),
  path('studentform', views.studentform_view, name='studentform'),
  path('delete-asssignment/<int:pk>/', views.deleteAssignment, name='delete-assignment'),
  path('delete-chore/<int:pk>/', views.deleteChore, name='delete-chore'),
  path('message', views.message_view, name='message'),
  
]