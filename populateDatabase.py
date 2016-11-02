__author__ = 'Jason'
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'startUp.settings')

import django
django.setup()

from racks.models import BikeRack
from racks.models import UserProfile
from racks.models import FavBikeRack
from racks.models import UsedRack
from racks.__init__ import racks
from racks.__init__ import parsexml

# for each bike rack currently in the db we want to clear it first before we add anything else
def populate():
    parsexml()
    for rack in racks:
       addRack(rack.address, rack.number, rack.lat, rack.lon, rack.skytrain)




def addRack(address,number,lat,lon,skytrain):
    r = BikeRack.objects.get_or_create(address=address)[0]
    r.address = address
    r.number = number
    r.lat = lat
    r.lon = lon
    r.skytrain = skytrain
    r.save()

def addUser(user):
    u = UserProfile.objects.get_or_create(user=user)[0]
    u.user = user
    u.save()
    return u

def addFavRack(user, address, number, lat, lon):
    r = FavBikeRack.objects.get_or_create(user=user,address=address)[0]
    r.address = address
    r.number = number
    r.lat = lat
    r.lon = lon
    r.save()
    return r


def addUsed(user, address, number):
    r = UsedRack.objects.get_or_create(user=user,address=address)[0]
    r.address = address
    r.number = number
    r.save()
    return r


    # Start execution here!
if __name__ == '__main__':
    print("Starting population script...")
    populate()