from django.contrib import admin

#importing my models
from .models import Duck
from .models import Chicken

# Register your models here.
admin.site.register(Duck)
admin.site.register(Chicken)

