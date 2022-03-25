from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.base, name="base"),
    path('duck/<str:pk>/', views.duck, name="duck"),

    #dynamic urls
    #str can be an int or slug as well
    path('room', views.mainroom, name="mainroom"),
    path('room/<str:pk>/', views.room, name="room"),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
]
