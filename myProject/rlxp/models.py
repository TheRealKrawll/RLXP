from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  fname = models.CharField(max_length=40, null=True, blank=True)
  lname = models.CharField(max_length=40, null=True, blank=True)
  age = models.IntegerField(null=True, blank=True)
  start_date = models.DateTimeField(auto_now_add=True)
  grade_level = models.IntegerField(blank=True, null = True, default=0)
  xp = models.IntegerField(default=0)
  profile_pic = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, null=True, blank=True)

class Class(models.Model):
  student = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  subject = models.CharField(max_length=50)
  start_date = models.DateTimeField(auto_now_add=True)
  done_date = models.DateTimeField(auto_now=True)

class Assignment(models.Model):
  _class = models.ForeignKey(Class, on_delete=models.CASCADE)

  class Difficulty(models.IntegerChoices):
    VERYEASY = 1
    EASY = 2
    NORMAL = 3
    HARD = 4
    VERYHARD = 5

  name = models.CharField(max_length=50)
  difficulty = models.IntegerField(choices=Difficulty.choices)
  xp = models.IntegerField()
  start_date = models.DateTimeField(auto_now_add=True)
  done_date = models.DateTimeField(auto_now=True)
  due_date = models.DateTimeField(null=True, blank=True)

class Chore(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  class Difficulty(models.IntegerChoices):
    VERYEASY = 1
    EASY = 2
    NORMAL = 3
    HARD = 4
    VERYHARD = 5
    
  name = models.CharField(max_length=50)
  difficulty = models.IntegerField(choices=Difficulty.choices)
  recurring = models.BooleanField()
  start_date = models.DateTimeField(auto_now_add=True)
  done_date = models.DateTimeField(auto_now=True)
  due_date = models.DateTimeField(null=True, blank=True)



  


  