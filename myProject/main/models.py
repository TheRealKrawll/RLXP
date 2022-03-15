from django.db import models
from django.contrib.auth.models import User

class Duck(models.Model):
    #need some attributes
    name = models.CharField(max_length=40)
    color = models.CharField(max_length=40)
    media = models.CharField(max_length=40, null=True)

    #to show in admin page
    def __str__(self):
        return self.name
        

class Chicken(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


# EVERYTHING BELOW IS FOR THE TUTORIAL

#ONE TO ONE (each room can only have one topic)
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)

    #blank=True is for the form, #null=True is for database
    description = models.TextField(null=True, blank=True)
    #partiicipants = 

    #auto_now=True takes a snapshot when of time when you save a model
    updated = models.DateTimeField(auto_now=True)

    #auto_now_add=True takes a snamshow when a model is created
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

#ONE TO MANY  (one room many messages)
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #with cascade, if a room gets deletes, so will all the messages
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
