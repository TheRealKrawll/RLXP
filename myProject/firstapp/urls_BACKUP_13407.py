from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index, name="index"),
]
<<<<<<< HEAD
 
=======
>>>>>>> assignment2