from django.db import models

# Create your models here.
class posts(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    body = models.CharField(max_length=1000)