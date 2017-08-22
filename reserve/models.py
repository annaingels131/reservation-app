from django.db import models

class SF(models.Model):
    date = models.DateTimeField()
    seat = models.IntegerField()