from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.base, name="base"),
    path("index/", views.name_view, name="index")
]
