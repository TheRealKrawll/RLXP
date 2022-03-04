from django.db import models

class Duck(models.Model):
    #need some attributes
    d_name = models.CharField(max_length=40)
    #d_image = models.ImageField()
    d_img_url = models.CharField(max_length=150, default="https://media.istockphoto.com/photos/mallard-duck-on-white-background-picture-id464988959")

    