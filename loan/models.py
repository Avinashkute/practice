from django.db import models

# Create your models here.
class crop_loan(models.Model):
    NAME=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    Acres=models.IntegerField()

