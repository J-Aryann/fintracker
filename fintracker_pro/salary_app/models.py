from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Salary(models.Model):
    sources=[
        ('salary','salary'),
        ('freelance','freelance'),
        ('business','business'),
        ('intrest','intrest'),
        ('rentelincome','rentelincome'),
        ('other','other')
    ]
    payment_modes=[
        ('bank','bank'),
        ('upi','upi'),
        ('cash','cash'),
        ('cheque','cheque'),
        ('other','other')
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField()
    source = models.CharField(max_length=100,choices=sources)
    date = models.DateField()
    paymentmode = models.CharField(max_length=100,choices=payment_modes)
    
