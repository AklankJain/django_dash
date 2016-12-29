from __future__ import unicode_literals

from django.db import models

from django.utils import timezone


class Store(models.Model):
	name = models.CharField(max_length = 200)



class Zone(models.Model):
	store = models.ForeignKey(Store , on_delete = models.CASCADE)
	zone_number = models.PositiveIntegerField()
	footfall = models.PositiveIntegerField()
	date = models.DateTimeField(auto_now_add = True , blank = True)
