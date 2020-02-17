from django.db import models
class User(models.Model):
    name = models.CharField(max_length=40)
    coins = models.DecimalField(decimal_places=2,max_digits=5)
# Create your models here.
    def returnName(self):
        return self.name
    def returnCoins(self):
        return self.coins

