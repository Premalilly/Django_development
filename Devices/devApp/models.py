from __future__ import unicode_literals
from django.db import models
from datetime import datetime

# Create your models here.

class DeviceModel(models.Model):
    name = models.CharField(max_length=30, default=False)
    image = models.ImageField(max_length=None, default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    payment_expiry = models.FloatField(default=False)

    class Meta:
        ordering = ('payment_expiry',)

    def __str__(self):
        return '%s' % self.payment_expiry







