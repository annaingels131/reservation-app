from django.db import models

# Create your models here.

class Item(models.Model):
	stattions = models.CharField(max_length=200)
	description = models.TextField()
	amount = models.DateTimeField()
