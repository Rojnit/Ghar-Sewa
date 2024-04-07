from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class contact(models.Model):
    firstName= models.CharField(max_length=50)
    lastName= models.CharField(max_length = 50)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length = 250)
    description = models.TextField(default='')

