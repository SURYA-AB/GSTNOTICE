from django.db import models

class emp(models.Model):
    name = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=100,null=True)
    val = models.CharField(max_length=100,null=True)
    #point = models.CharField(max_length=100,null=True)
