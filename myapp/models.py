from django.db import models

# Create your models here.

class Allowed(models.Model):
    name = models.TextField(blank=True)
    status = models.TextField(blank=True)

class Subnets(models.Model):
    name = models.TextField(blank=True)
    ip = models.TextField(blank=True)
    allowed_subnets = models.ManyToManyField(Allowed)

class Firewall(models.Model):
    firewall_Name = models.TextField(blank=True)
    rows = models.ManyToManyField(Subnets)
