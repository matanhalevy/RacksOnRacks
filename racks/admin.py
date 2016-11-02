__author__ = 'Jason'
from django.contrib import admin
from racks.models import BikeRack
from racks.models import UserProfile
from racks.models import FavBikeRack
from racks.models import UsedRack

admin.site.register(BikeRack)
admin.site.register(UserProfile)
admin.site.register(FavBikeRack)
admin.site.register(UsedRack)