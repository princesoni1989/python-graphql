from django.db import models


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    technology = models.CharField(max_length=100, blank=True, default='')
    address = models.CharField(max_length=100, blank=True, default='')
    country = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
