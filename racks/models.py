__author__ = 'Jason'

from django.db import models

from django.contrib import admin
# Create your models here.

class BikeRack(models.Model):
        address = models.CharField(max_length=128)
        number = models.IntegerField(default=0)
        lat = models.FloatField(default=0)
        lon = models.FloatField(default=0)
        skytrain = models.CharField(max_length=128,null=True,blank=True)


        def save(self, *args, **kwargs):
                if not self.skytrain:
                        self.skytrain = ''
                super(BikeRack, self).save(*args, **kwargs)


        def __unicode__(self):
                return self.address

class UserProfile(models.Model):
        user = models.CharField(max_length=128)

        def save(self, *args, **kwargs):
                super(UserProfile, self).save(*args, **kwargs)

        def __unicode__(self):
                return self.user

class FavBikeRack(models.Model):
        user = models.ForeignKey(UserProfile)
        address = models.CharField(max_length=128)
        number = models.IntegerField(default=0)
        lat = models.FloatField(default=0)
        lon = models.FloatField(default=0)

        def save(self, *args, **kwargs):
                super(FavBikeRack, self).save(*args, **kwargs)

        def __unicode__(self):
                return self.address

class UsedRack(models.Model):
        user = models.ForeignKey(UserProfile)
        address = models.CharField(max_length=128)
        number = models.IntegerField(default=0)

        def save(self, *args, **kwargs):
                super(UsedRack, self).save(*args, **kwargs)

        def __unicode__(self):
                return self.address