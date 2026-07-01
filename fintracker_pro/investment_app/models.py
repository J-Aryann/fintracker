from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.
class Investment(models.Model):
    investment_type=[
        ('stock','stock'),
        ('mutual_fund','mutual_fund'),
        ('crypto','crypto'),
        ('fd','fd'),
        ('gold','gold'),
        ('other','other')
    ]
    platforms=[
        ('zerodha','zerodha'),
        ('groww','groww'),
        ('upstox','upstox'),
        ('angelone','angelone'),
        ('icicidirect','icicidirect'),
        ('hdfcsecurities','hdfcsecurities'),
        ('paytammoney','paytammoney'),
        ('kuvera','kuvera'),
        ('etmoney','atmoney'),
        ('fd','fd'),
        ('rd','rd'),
        ('ppf','ppf'),
        ('hdfcbank','hdfcbank'),
        ('icicibank','icicibank'),
        ('indiapost','indiapost'),
        ('indmoney','indmoney'),
        ('vested','vested'),
        ('interactivebrocker','interactivebrocker'),
        ('other','other')
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type_invest=models.CharField(max_length=100,choices=investment_type)
    amount_invest=models.FloatField(validators=[MinValueValidator(1)])
    platform =models.CharField(max_length=100,choices=platforms)
    returnio = models.FloatField()
    



