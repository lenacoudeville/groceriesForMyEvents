from django.shortcuts import render, get_object_or_404
from .models import Event, Invitation, Product, InvitProd
import datetime


#Page d'accueil
def homepage(request):

	logged_in_user = request.user.id #récupération de l'id de l'utilisateur
	now = datetime.datetime.now() #récupération de la date d'aujourd'hui
	logged_in_user_events = Event.objects.filter(id_host=logged_in_user, end_date__gte=now) #récupération de tous les événements créés par l'utilisateur et exclu les événements passés
	logged_in_user_invitations = Invitation.objects.filter(id_user=logged_in_user) #récupération de tous les événements auquel l'utilisateur est invité
	user_invitations_not_host = logged_in_user_invitations.exclude(id_event_id__id_host=logged_in_user, id_event_id__end_date__gte=now) #exclu des invitations les événements créés par l'utilisateur et les événements passés
	template = 'myGroceries/homepage.html'
	return render(request, template, {'hostingevents' : logged_in_user_events, 'guesttoevents' : user_invitations_not_host})


#Page de création d'un événement
def create_event(request):
	template = 'myGroceries/create_event.html'
	return render(request, template, {})


#Page d'invitation à l'événement
def invitation_to_my_event():
	template = 'myGroceries/invitation_to_my_event.html'
	return render(request, template, {})


#Page de vue de l'événement
def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'myGroceries/event_detail.html', {'event': event})