# Create your views here.
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect

from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.api import channel

from travelplanner.models import *
from travelplanner.utils import travel_uri_generator
from travelplanner.utils import is_loggedin

def index(request):
    travel_uri = travel_uri_generator()
    try:
        Travel.objects.get(uri=travel_uri)
        return HttpResponse('Some error occured. Try again!')
    except:
        travel = Travel(name='Untitled Title', uri=travel_uri)
        travel.save()
        return redirect('/travel/'+travel_uri)

def travel(request, travel_uri):
    try:
        travel = Travel.objects.get(uri=travel_uri)
        email = travel.email
        token = channel.create_channel(travel_uri)
        return render_to_response('travelplanner/travel.html',
                {'email':email, 'token':token})
    except:
        return HttpResponse('Some error occured. <a href="/">Try again!</a>')

@csrf_exempt
def travel_name_edit(request):
    if request.method == 'POST':
        print request.POST
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
            return HttpResponse(travel.name)
    return HttpResponse('error')

@csrf_exempt
def travel_get_name(request):
    if request.method == 'POST':
        travel_uri = request.POST.get('travel_uri', None) 

        try:
            travel = Travel.objects.get(uri=travel_uri)
            return HttpResponse(travel.name)
        except Travel.DoesNotExist:
            pass
    return HttpResponse('')

@csrf_exempt
def map_add_place(request):
    if request.method == 'POST':
        print request.POST
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

@csrf_exempt
def map_get_places(request):
    if(request.method=='POST'):
        travel_uri = request.POST.get('travel_uri', None)
        
        try:
            travel = Travel.objects.get(uri=travel_uri)
        except Travel.DoesNotExist:
            travel = None
        
        place = Places.objects.filter(travel=travel)
        places_json = serializers.serialize('json', place)
        return HttpResponse(places_json, content_type="application/json")
    return HttpResonse('[]')

@csrf_exempt
def place_get_activities(request):
    if(request.method=='POST'):
        place_id = request.POST.get('place_id', None)
        
        try:
            place = Places.objects.get(id=place_id)
            activity = Activity.objects.filter(place=place)
            activity_json = serializers.serialize('json', activity)
        return HttpResponse(activity_json, content_type="application/json")
        except Travel.DoesNotExist:
            place = None
        
    return HttpResonse('[]')

@csrf_exempt
def invite_friends(request):
    if(request.method=='POST'):
        travel_uri = request.POST.get('travel_uri', None)
        to = request.POST.get('to', None)
        subject = request.POST.get('subject', None)
        message = request.POST.get('message', None)

        try:
            travel = Travel.objects.get(uri=travel_uri)
            sender = travel.email
            reciever = to.split(',')
            for r in reciever:
                mail.send_mail(sender, r, subject, message)
            return HttpResponse('Invite sent to %s' % reciever)
        except:
            travel = None
    return HttpResponse('error')

@csrf_exempt
def set_my_email(request):
    if(request.method=='POST'):
        travel_uri = request.POST.get('travel_uri', None)
        email = request.POST.get('email', None)
        try:
            travel = Travel.objects.get(uri=travel_uri)
        except:
            travel = None
        if travel and email:
            travel.email = email
            travel.save()
            mail.send_mail('admin@tripnote.com', 'luckyk1592@gmail.com', 'Your new trip',
                    '<a href="localhost:8080/travel/%s">Url</a>' % travel_uri)
            return HttpResponse('We have mailed you this unique url for future editing!')
    return HttpResponse('error')
