from django.db import models

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