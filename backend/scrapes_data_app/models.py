from django.db import models


# Create your models here.


class Webscrap(models.Model):
    
    name = models.CharField(max_length=150, null=True,)
    price = models.CharField(max_length=150, null=True,)
    hour =  models.CharField(max_length=150, null=True,) 
    twenty_hours= models.CharField(max_length=150, null=True,)
    seven_days= models.CharField(max_length=150, null=True,)  
    market_cap = models.CharField(max_length=150, null=True,)
    volume = models.CharField(max_length=150, null=True,)
    circulating_supply= models.CharField(max_length=150, null=True,)

    def __str__(self):
        return self.name

    class Meta:
        db_table="tbl_webscapes"    
        verbose_name = 'Coin Scrape'


  
