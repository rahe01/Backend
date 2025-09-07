from django.db import models

# Create your models here.


class Profile(models.Model):

    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    email = models.CharField(max_length=70)
    city = models.CharField(max_length=70)

    def __str__(self):
        return str(self.roll)
    


class Result(models.Model):

    stu_class = models.CharField(max_length=70)
    mark = models.IntegerField()

    def __str__(self):
        return self.stu_class