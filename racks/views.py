__author__ = 'Jason'

from django.shortcuts import render
from django.core import serializers
json_serializer = serializers.get_serializer("json")()
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
#from the six

from populateDatabase import addFavRack, addUser, addUsed
from django.http import HttpResponse, JsonResponse
from django.template.context_processors import csrf


from racks.models import BikeRack, UserProfile, FavBikeRack, UsedRack



def home(request):
    rack_list = BikeRack.objects.all()
    context_dict = {'racks': rack_list}
    return render(request, 'racks/home.html', context_dict)

def map(request):
    # context_dict = {}
    rack_list = BikeRack.objects.all()

    context_dict = {'racks': rack_list}

    # Render the response and send it backs

    return render(request, 'racks/map.html', context_dict)

def about(request):
    return render(request, 'racks/about.html',{})


def map_locs(request):
    if request.method == 'GET':
        rack_list = BikeRack.objects.all()

        rackJson = []
        for rack in rack_list:
            rackJson.append([rack.address, rack.lat, rack.lon, rack.number, rack.skytrain])

        return JsonResponse({"racks":rackJson})
    else:
        return HttpResponse('')


def get_users(request):
    if request.method == 'GET':
        user_list = UserProfile.objects.all()

        userJson = []
        for user in user_list:
            userJson.append([user.user])

        return JsonResponse({"users":userJson})
    else:
        return HttpResponse('')

def get_faves(request):
    if request.method == 'GET':
        fave_list = FavBikeRack.objects.all()

        faveJson = []
        for fave in fave_list:
            faveJson.append([fave.user.user, fave.address, fave.lat, fave.lon, fave.number])

        return JsonResponse({"faves":faveJson})
    else:
        return HttpResponse('')

user = 0
@csrf_exempt
def add_favorite(request):
    if request.method == 'POST':
        address = request.POST.getlist('address')[0]
        number = request.POST.getlist('number')[0]
        lat = request.POST.getlist('lat')[0]
        lon = request.POST.getlist('lon')[0]
        global user
        user = request.POST.getlist('u')[0]


       # u = request.POST.getlist('user')[0]
        addFavRack(addUser(user), address, number, lat, lon)
    rack_list = FavBikeRack.objects.filter(user=addUser(user))
    context_dict = {'racks': rack_list}
    # return HttpResponse('')
    return render(request, 'racks/favoriteracks.html', context_dict)
useduser = 0
@csrf_exempt
def add_used(request):
    if request.method == 'POST':
        address = request.POST.getlist('address')[0]
        number = request.POST.getlist('number')[0]
        global useduser
        useduser = request.POST.getlist('u')[0]

        addUsed(addUser(useduser), address, number)


    rack_list = UsedRack.objects.filter(user=addUser(useduser)).order_by('-id')
    context_dict = {'racks': rack_list}
    # return HttpResponse('')
    return render(request, 'racks/usedracks.html', context_dict)
