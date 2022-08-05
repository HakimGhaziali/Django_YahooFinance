from django.db import models

# Create your models here.


class Ticker(models.Model):

    ticker= models.CharField(max_length=50)


    def __str__(self):
        return self.ticker

class Data(models.Model):

    ticker = models.CharField(max_length=50)
    price = models.PositiveIntegerField(blank=True , null=True)
    date = models.PositiveIntegerField( blank=True , null=True )


    def __str__(self):
        
            return "%s %s" % (self.price , self.date)  

    