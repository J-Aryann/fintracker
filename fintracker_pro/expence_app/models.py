from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.
class Expence(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    categories = [
        ('food','food' ),
        ('travel','travel'),
        ('bills','bills'),
        ('shopping','shopping'),
        ('other','other')
    ]
    payment_modes=[
        ('cash','cash'),
        ('upi','upi'),
        ('card','card'),
        ('bank_transfer','bank_transfer'),
        ('other','other')
    ]
    amount = models.FloatField(validators=[MinValueValidator(1)])
    category = models.CharField(max_length=100,choices=categories)
    date = models.DateField()
    payment_mode=models.CharField(max_length=100,choices=payment_modes)







