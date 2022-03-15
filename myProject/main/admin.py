from django.contrib import admin

#importing my models
from .models import Duck, Message
from .models import Chicken
#from tutorial
from .models import Room, Topic, Message

# Register your models here.
admin.site.register(Duck)
admin.site.register(Chicken)

#Tutorial
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Topic)

