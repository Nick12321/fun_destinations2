from django.db import models

# Create your models here.
class Places(models.Model):
	name = models.CharField(max_length=100)
	country = models.CharField(max_length=50)
