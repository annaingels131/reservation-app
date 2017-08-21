from django.db import models

# Create your models here.



class SanFranTrain(models.Model):
    TO_LOC = (
        ('A', 'LA'),
        ('B', 'SJ'),
        ('C', 'FR'),
        ('D', 'AN'),
              #add more to locs ...
    )
    to = models.CharField(max_length = 1, choices=TO_LOC,)
    date = models.DateField()
    time = models.CharField(max_length = 6)
    seats = models.CharField(max_length = 3)

