from pyexpat import model
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

'''     Note 
# This is model for table in database'''

class adress_data(models.Model):
    add = models.CharField(max_length=200)
    lat = models.DecimalField(max_digits=14,decimal_places=6)
    long = models.DecimalField(max_digits=14,decimal_places=6)
    contact = models.IntegerField(validators=[MinValueValidator(1000000000),MaxValueValidator(9999999999)])