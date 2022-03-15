from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.base, name="base"),

    #dynamic urls
    #str can be an int or slug as well
    #path('room', views.mainroom, name="mainroom"),
    path('room/<str:pk>/', views.room, name="room"),
    path('duck/<str:pk>/', views.duck, name="duck"),
]
