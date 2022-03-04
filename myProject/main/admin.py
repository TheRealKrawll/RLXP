from django.contrib import admin

#importing my models
from .models import Duck

# Register your models here.
admin.site.register(Duck)

