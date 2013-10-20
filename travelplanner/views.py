# Create your views here.
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from travelplanner.models import *

def index(request):
    return render_to_response('travelplanner/index.html')

def travel(request, travel_uri):
    return render_to_response('travelplanner/travel.html', {'travel_uri': travel_uri})

@csrf_exempt
def travel_name_edit(request):
    if request.method == 'POST':
        travel_uri = request.POST.get('travel_uri', None) 
        name = request.POST.get('name', None)

        try:
            travel = Travel.objects.get(uri=travel_uri)
        except Travel.DoesNotExist:
            travel = None
        
        save = travel and name
        if save:
            travel.name = name
            travel.save()
            return HttpResponse(travel.id)
    return HttpResponse('error')

@csrf_exempt
def map_add_place(request):
    if request.method == 'POST':
        travel_uri = request.POST.get('travel_uri', None) 
        latti = request.POST.get('latti', None)
        longi = request.POST.get('longi', None)
        properties = request.POST.get('properties', None)
        location_name = request.POST.get('location_name', None)
        datetime = request.POST.get('datetime', None)

        try:
            travel = Travel.objects.get(uri=travel_uri)
        except Travel.DoesNotExist:
            travel = None

        save = travel and latti and longi

        if save:
            place = Places()
            place.travel = travel
            place.latti = latti
            place.longi = longi
            place.properties = properties
            place.location_name = location_name
            place.date_time = datetime
            place.save()
            return HttpResponse(place.id)
    return HttpResponse('error')

@csrf_exempt
def map_remove_place(request):
    if request.method == 'POST':
        travel_uri = request.POST.get('travel_uri', None) 
        latti = request.POST.get('latti', None)
        longi = request.POST.get('longi', None)

        try:
            travel = Travel.objects.get(uri=travel_uri)
        except Travel.DoesNotExist:
            travel = None

        try:
            place = Places.objects.get(travel=travel, latti=latti, longi=longi)
            place_id = place.id
            place.delete()
            return HttpResponse(place_id)
        except:
            pass

    return HttpResponse('error')

@csrf_exempt
def activity_add(request):
    if request.method == 'POST':
        place_id = request.POST.get('place_id', None)
        comment = request.POST.get('comment', None)

        try:
            place = Places.objects.get(id=place_id) 
        except Place.DoesNotExist:
            place = None

        save = place and comment
        if save:
            activity = Activity(place=place, comment=comment)
            activity.save()
            return HttpResponse(activity.id)
    return HttpResponse('error')

@csrf_exempt
def activity_remove(request):
    if request.method == 'POST':
        activity_id = request.POST.get('activity_id', None)

        try:
            activity = Activity.objects.get(id=activity_id)
        except Activity.DoesNotExist:
            activity = None
        if activity:
            activity_id = activity.id
            activity.delete()
            return HttpResponse(activity_id)
    return HttpResponse('error')

@csrf_exempt
def activity_edit(request):
    if request.method == 'POST':
        activity_id = request.POST.get('activity_id', None)
        comment = request.POST.get('comment', None)

        try:
            activity = Activity.objects.get(id=activity_id)
        except Activity.DoesNotExist:
            activity = None
        
        save = activity and comment
        if save:
            activity.comment = comment
            activity.save()
            return HttpResponse(activity.id)
    return HttpResponse('error')
