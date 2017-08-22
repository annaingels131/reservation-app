from django.db import models

# station models


class SanFranciscoTrain(models.Model):
    TO_LOC = (
              
        ('MILROY', 'ML'),
        ('SAN JOSE', 'SJ'),
        ('GILROY', 'GL'),
        ('MERCED', 'MR'),
        ('FRESNO', 'FR'),
        ('KINGSTON', 'KG'),
        ('BAKERSFIELD', 'BK'),
        ('PALMDALE', 'PL'),
        ('BURBANK', 'BR'),
        ('LOS ANGELES', 'LA'),
        ('ORANGE COUNTY', 'OC'),
        ('ANAHEIM', 'AN'),
        
    )
    to = models.CharField(max_length = 20, choices=TO_LOC,)
    date = models.DateField()
    time = models.CharField(max_length = 8)
    seats = models.CharField(max_length = 3)

class MilroyTrain(models.Model):
    TO_LOC = (
              
        ('SAN FRANCISCO', 'SF'),
        ('SAN JOSE', 'SJ'),
        ('GILROY', 'GL'),
        ('MERCED', 'MR'),
        ('FRESNO', 'FR'),
        ('KINGSTON', 'KG'),
        ('BAKERSFIELD', 'BK'),
        ('PALMDALE', 'PL'),
        ('BURBANK', 'BR'),
        ('LOS ANGELES', 'LA'),
        ('ORANGE COUNTY', 'OC'),
        ('ANAHEIM', 'AN'),
              
    )
    to = models.CharField(max_length = 20, choices=TO_LOC,)
    date = models.DateField()
    time = models.CharField(max_length = 8)
    seats = models.CharField(max_length = 3)

class GilroyTrain(models.Model):
    TO_LOC = (
              
        ('SAN FRANCISCO', 'SF'),
        ('MILROY', 'ML'),
        ('SAN JOSE', 'SJ'),
        ('MERCED', 'MR'),
        ('FRESNO', 'FR'),
        ('KINGSTON', 'KG'),
        ('BAKERSFIELD', 'BK'),
        ('PALMDALE', 'PL'),
        ('BURBANK', 'BR'),
        ('LOS ANGELES', 'LA'),
        ('ORANGE COUNTY', 'OC'),
        ('ANAHEIM', 'AN'),
              
    )
    to = models.CharField(max_length = 20, choices=TO_LOC,)
    date = models.DateField()
    time = models.CharField(max_length = 8)
    seats = models.CharField(max_length = 3)

class SanJoseTrain(models.Model):
    TO_LOC = (
              
        ('SAN FRANCISCO', 'SF'),
        ('MILROY', 'ML'),
        ('GILROY', 'GL'),
        ('MERCED', 'MR'),
        ('FRESNO', 'FR'),
        ('KINGSTON', 'KG'),
        ('BAKERSFIELD', 'BK'),
        ('PALMDALE', 'PL'),
        ('BURBANK', 'BR'),
        ('LOS ANGELES', 'LA'),
        ('ORANGE COUNTY', 'OC'),
        ('ANAHEIM', 'AN'),
              
    )
    to = models.CharField(max_length = 20, choices=TO_LOC,)
    date = models.DateField()
    time = models.CharField(max_length = 8)
    seats = models.CharField(max_length = 3)

class MercedTrain(models.Model):
    TO_LOC = (
              
        ('SAN FRANCISCO', 'SF'),
        ('MILROY', 'ML'),
        ('SAN JOSE', 'SJ'),
        ('GILROY', 'GL'),
        ('FRESNO', 'FR'),
        ('KINGSTON', 'KG'),
        ('BAKERSFIELD', 'BK'),
        ('PALMDALE', 'PL'),
        ('BURBANK', 'BR'),
        ('LOS ANGELES', 'LA'),
        ('ORANGE COUNTY', 'OC'),
        ('ANAHEIM', 'AN'),
        
    )
    to = models.CharField(max_length = 20, choices=TO_LOC,)
    date = models.DateField()
    time = models.CharField(max_length = 8)
    seats = models.CharField(max_length = 3)

class FresnoTrain(models.Model):
    TO_LOC = (
              
        ('SAN FRANCISCO', 'SF'),
        ('MILROY', 'ML'),
        ('SAN JOSE', 'SJ'),
        ('GILROY', 'GL'),
        ('MERCED', 'MR'),
        ('KINGSTON', 'KG'),
        ('BAKERSFIELD', 'BK'),
        ('PALMDALE', 'PL'),
        ('BURBANK', 'BR'),
        ('LOS ANGELES', 'LA'),
        ('ORANGE COUNTY', 'OC'),
        ('ANAHEIM', 'AN'),
              
    )
    to = models.CharField(max_length = 20, choices=TO_LOC,)
    date = models.DateField()
    time = models.CharField(max_length = 8)
    seats = models.CharField(max_length = 3)

class KingstonTrain(models.Model):
    TO_LOC = (
              
        ('SAN FRANCISCO', 'SF'),
        ('MILROY', 'ML'),
        ('SAN JOSE', 'SJ'),
        ('GILROY', 'GL'),
        ('MERCED', 'MR'),
        ('FRESNO', 'FR'),
        ('BAKERSFIELD', 'BK'),
        ('PALMDALE', 'PL'),
        ('BURBANK', 'BR'),
        ('LOS ANGELES', 'LA'),
        ('ORANGE COUNTY', 'OC'),
        ('ANAHEIM', 'AN'),
              
    )
    to = models.CharField(max_length = 20, choices=TO_LOC,)
    date = models.DateField()
    time = models.CharField(max_length = 8)
    seats = models.CharField(max_length = 3)

class BakersfieldTrain(models.Model):
    TO_LOC = (
              
        ('SAN FRANCISCO', 'SF'),
        ('MILROY', 'ML'),
        ('SAN JOSE', 'SJ'),
        ('GILROY', 'GL'),
        ('MERCED', 'MR'),
        ('FRESNO', 'FR'),
        ('KINGSTON', 'KG'),
        ('PALMDALE', 'PD'),
        ('BURBANK', 'BR'),
        ('LOS ANGELES', 'LA'),
        ('ORANGE COUNTY', 'OC'),
        ('ANAHEIM', 'AN'),
              
    )
    to = models.CharField(max_length = 20, choices=TO_LOC,)
    date = models.DateField()
    time = models.CharField(max_length = 8)
    seats = models.CharField(max_length = 3)

class PalmdaleTrain(models.Model):
    TO_LOC = (
              
        ('SAN FRANCISCO', 'SF'),
        ('MILROY', 'ML'),
        ('SAN JOSE', 'SJ'),
        ('GILROY', 'GL'),
        ('MERCED', 'MR'),
        ('FRESNO', 'FR'),
        ('KINGSTON', 'KG'),
        ('BAKERSFIELD', 'BK'),
        ('BURBANK', 'BR'),
        ('LOS ANGELES', 'LA'),
        ('ORANGE COUNTY', 'OC'),
        ('ANAHEIM', 'AN'),
              
    )
    to = models.CharField(max_length = 20, choices=TO_LOC,)
    date = models.DateField()
    time = models.CharField(max_length = 8)
    seats = models.CharField(max_length = 3)

class BurbankTrain(models.Model):
    TO_LOC = (
              
        ('SAN FRANCISCO', 'SF'),
        ('MILROY', 'ML'),
        ('SAN JOSE', 'SJ'),
        ('GILROY', 'GL'),
        ('MERCED', 'MR'),
        ('FRESNO', 'FR'),
        ('KINGSTON', 'KG'),
        ('BAKERSFIELD', 'BK'),
        ('PALMDALE', 'PD'),
        ('LOS ANGELES', 'LA'),
        ('ORANGE COUNTY', 'OC'),
        ('ANAHEIM', 'AN'),
              
    )
    to = models.CharField(max_length = 20, choices=TO_LOC,)
    date = models.DateField()
    time = models.CharField(max_length = 8)
    seats = models.CharField(max_length = 3)

class LosAngelesTrain(models.Model):
    TO_LOC = (
              
        ('SAN FRANCISCO', 'SF'),
        ('MILROY', 'ML'),
        ('SAN JOSE', 'SJ'),
        ('GILROY', 'GL'),
        ('MERCED', 'MR'),
        ('FRESNO', 'FR'),
        ('KINGSTON', 'KG'),
        ('BAKERSFIELD', 'BK'),
        ('PALMDALE', 'PD'),
        ('BURBANK', 'BR'),
        ('ORANGE COUNTY', 'OC'),
        ('ANAHEIM', 'AN'),
              
    )
    to = models.CharField(max_length = 20, choices=TO_LOC,)
    date = models.DateField()
    time = models.CharField(max_length = 8)
    seats = models.CharField(max_length = 3)

class OrangeCountyTrain(models.Model):
    TO_LOC = (
              
        ('SAN FRANCISCO', 'SF'),
        ('MILROY', 'ML'),
        ('SAN JOSE', 'SJ'),
        ('GILROY', 'GL'),
        ('MERCED', 'MR'),
        ('FRESNO', 'FR'),
        ('KINGSTON', 'KG'),
        ('BAKERSFIELD', 'BK'),
        ('PALMDALE', 'PD'),
        ('BURBANK', 'BR'),
        ('LOS ANGELES', 'LA'),
        ('ANAHEIM', 'AN'),
              
    )
    to = models.CharField(max_length = 20, choices=TO_LOC,)
    date = models.DateField()
    time = models.CharField(max_length = 8)
    seats = models.CharField(max_length = 3)

class AnaheimTrain(models.Model):
    TO_LOC = (
              
        ('SAN FRANCISCO', 'SF'),
        ('MILROY', 'ML'),
        ('SAN JOSE', 'SJ'),
        ('GILROY', 'GL'),
        ('MERCED', 'MR'),
        ('FRESNO', 'FR'),
        ('KINGSTON', 'KG'),
        ('BAKERSFIELD', 'BK'),
        ('PALMDALE', 'PD'),
        ('BURBANK', 'BR'),
        ('LOS ANGELES', 'LA'),
        ('ORANGE COUNTY', 'OC'),
              
    )
    to = models.CharField(max_length = 20, choices=TO_LOC,)
    date = models.DateField()
    time = models.CharField(max_length = 8)
    seats = models.CharField(max_length = 3)


