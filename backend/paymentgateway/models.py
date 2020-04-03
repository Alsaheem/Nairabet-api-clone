from django.db import models

# Create your models here.

class Gateway(models.Model):
    # model for payment gateways like stripe and paystack
    name = models.CharField(max_length=20)
    description = models.TextField()
    token = models.CharField(max_length=100)