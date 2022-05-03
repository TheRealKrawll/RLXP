from django.urls import path
from . import views

urlpatterns = [
  #dynamic urls
  #str can be an int or slug as well
  path('', views.home_view, name="home"),
  path('profile/', views.profile_view, name="profile"),
  path('dashboard/', views.dashboard_view, name="dashboard"),
  path('accounts/register', views.register_view, name='register'),
  path('studentform', views.studentform_view, name='studentform'),
  path('about', views.about_view, name='about'),
  path('delete-asssignment/<int:pk>/', views.deleteAssignment, name='delete-assignment'),
  path('submit-asssignment/<int:pk>/<int:st>/', views.submitAssignment, name='submit-assignment'),
  path('delete-chore/<int:pk>/', views.deleteChore, name='delete-chore'),
  path('submit-chore/<int:pk>/<int:st>/', views.submitChore, name='submit-chore'),

  path('message', views.message_view, name='message'),
  
]