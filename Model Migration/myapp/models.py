from django.db import models

# Create your models here.

class BookRahe(models.Model):
    
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    des = models.TextField( null=True)