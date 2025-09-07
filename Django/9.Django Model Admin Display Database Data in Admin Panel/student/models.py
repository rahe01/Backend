from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    roll = models.IntegerField()
    city = models.CharField(max_length=70)

    




class Result(models.Model):

    stu_class = models.CharField(max_length=70)
    marks = models.IntegerField()
