from .models import *
from .forms import EventForm
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth  import get_user_model
from django.contrib.auth.decorators import login_required
import datetime


#Page d'accueil
@login_required
def homepage(request):
	logged_in_user = request.user #récupération de l'utilisateur
	now = datetime.datetime.now() #récupération de la date d'aujourd'hui
	logged_in_user_events = Event.objects.filter(host=logged_in_user, end_date__gte=now) #récupération de tous les événements créés par l'utilisateur et exclu les événements passés
	logged_in_user_invitations = Invitation.objects.filter(guest=logged_in_user) #récupération de tous les événements auquel l'utilisateur est invité
	logged_in_user_participations = Participation.objects.filter(user=logged_in_user) #récupération de tous les événements auquel l'utilisateur est invité
	template = 'myGroceries/homepage.html'
	context = {'hostingevents' : logged_in_user_events, 'guesttoevents' : logged_in_user_invitations, 'guesttoparticipants' : logged_in_user_participations, 'user': request.user}
	return render(request, template, context)


#Page de vue de l'événement
@login_required
def event_detail(request, name_event):
	logged_in_user = request.user #récupération de l'utilisateur
	event = get_object_or_404(Event, name=name_event)
	invited = Invitation.objects.filter(event=event)
	guest_groceries = Participation.objects.filter(event=event)
	template = 'myGroceries/event_detail.html'
	context={'event': event, 'invited': invited, 'guest_groceries': guest_groceries}
	return render(request, template, context)


#Page de création d'un événement
@login_required
def create_event(request):
	template = 'myGroceries/create_event.html'
	if request.method == "POST":
		form = EventForm(request.POST)
		if form.is_valid():
			event = form.save(commit=False)
			event.host = request.user #affiliation de l'id de l'utilisateur à l'id_host
			event.save()
			return redirect('myGroceries:invitation_to_my_event', name_event=event.name) #si le formulaire est validé, renvoi vers l'invitation d'utilisateurs à l'event
#		participation = Participation(user=request.user, event=event.name)
#		participation.save()
	else:
		form = EventForm()
	return render(request, template, {'form': form})


#Action de suppression d'un événement
@login_required
def delete_event(request, name_event):
	try:
		event = get_object_or_404(Event, name=name_event)
		event.delete()
	except ObjectDoesNotExist:
		pass
	return redirect("myGroceries:homepage")


#Page de modification d'un événement
#@login_required
#def update_event(request, name_event):
#	try:
#		event = get_object_or_404(Event, name=name_event)
#		if event.start_date != request.POST.get("start_date"):
#			event.start_date = request.POST.get("start_date")
#		if event.end_date != request.POST.get("end_date").replace("\\xa0", ""):
#			event.end_date = request.POST.get("end_date").replace("\\xa0", "")
#		if event.description != request.POST.get("description").replace("\\xa0", ""):
#			event.description = request.POST.get("description").replace("\\xa0", "")
#		event.save()
#	except ObjectDoesNotExist:
#		pass
#	return redirect("/event/" + name_event + "/")



#Page d'invitation à l'événement
@login_required
def invitation_to_my_event(request, name_event):
	logged_in_user = request.user #récupération de l'utilisateur
	event = get_object_or_404(Event, name=name_event, host=logged_in_user) #erreur 404 si l'event n'existe pas ou si l'utilisateur n'a pas créé cet événement
	list_user = get_user_model()
	users = list_user.objects.all()
	template = 'myGroceries/invitation_to_my_event.html'
	context = {'event' : event, 'users': users, 'host': logged_in_user}
	return render(request, template, context)



#Action d'invitation à l'événement
@login_required
def invitation_to_my_event_act(request, name_event):
	logged_in_user = request.user #récupération de l'utilisateur
	event = get_object_or_404(Event, name=name_event, host=logged_in_user) #erreur 404 si l'event n'existe pas ou si l'utilisateur n'a pas créé cet événement
	user_invited = request.POST.getlist("users_post") # récupération de la liste d'user
	# ajout en bdd
	for u in user_invited:
		user = User.objects.get(username=u)
		try:
			# si présent en base pass
			Invitation.objects.get(event=event, guest=user)
		except ObjectDoesNotExist:
			# sinon ajout
			invitation = Invitation(event=event, guest=user)
			invitation.save()
	return redirect("myGroceries:event_detail", name_event=name_event)


#Action d'acceptation de l'invitation à l'événement
@login_required
def invitation_to_event_accept(request, name_event):
	logged_in_user = request.user #récupération de l'utilisateur
	event = get_object_or_404(Event, name=name_event) #erreur 404 si l'event n'existe pas ou si l'utilisateur n'a pas créé cet événement
	# delete invitation add participation
	invitation = Invitation.objects.get(event=event, guest=logged_in_user)
	invitation.delete()
	participation = Participation(user=logged_in_user, event=event)
	participation.save()
	return redirect("myGroceries:homepage")


#Action de refus de l'invitation à l'événement
@login_required
def invitation_to_event_refuse(request, name_event):
	logged_in_user = request.user #récupération de l'utilisateur
	event = get_object_or_404(Event, name=name_event) #erreur 404 si l'event n'existe pas ou si l'utilisateur n'a pas créé cet événement
	# delete invitation
	invitation = Invitation.objects.get(event=event, guest=logged_in_user)
	invitation.delete()
	return redirect("myGroceries:homepage")


#Action d'annulation de la participation à l'événement
@login_required
def participation_to_event_cancel(request, name_event):
	logged_in_user = request.user #récupération de l'utilisateur
	event = get_object_or_404(Event, name=name_event) #erreur 404 si l'event n'existe pas ou si l'utilisateur n'a pas créé cet événement
	# delete invitation
	participation = Participation.objects.get(event=event, user=logged_in_user)
	participation.delete()
	return redirect("myGroceries:homepage")


# Action de suppression d'un participant à mon événement
#@login_required
#def participation_to_my_event_delete(request, name_event, id_invite):
#	event = get_object_or_404(Event, name=name_event) #erreur 404 si l'event n'existe pas ou si l'utilisateur n'a pas créé cet événement
#	participation = Participation.objects.get(event=event, user=id_invite)
#	participation.delete()
#	return redirect("myGroceries:event_detail")


# Action de suppression d'un invité à mon événément
#@login_required
#def invitation_to_my_event_delete(request, name_event, id_invite):
#	event = get_object_or_404(Event, name=name_event) #erreur 404 si l'event n'existe pas ou si l'utilisateur n'a pas créé cet événement
#	invitation = Invitation.objects.get(event=event, guest=id_invite)
#	invitation.delete()
#	return redirect("myGroceries:event_detail")


#Page d'ajout de produits à la liste de courses de l'utilisateur
@login_required
def add_products_to_event(request, name_event):
	event = get_object_or_404(Event, name=name_event) #erreur 404 si l'event n'existe pas ou si l'utilisateur n'a pas créé cet événement
	products = Product.objects.all()
	template = 'myGroceries/add_products_to_event.html'
	context = {'event' : event, 'products': products}
	return render(request, template, context)


#Action d'ajout de produits à la liste de courses de l'utilisateur
@login_required
def add_products_to_event_act(request, name_event):
	logged_in_user = request.user
	products_added = request.POST.getlist("products_post")
	event = get_object_or_404(Event, name=name_event)
	for p in products_added:
		product = Product.objects.get(name=p)
		try:
			participation = get_object_or_404(Participation, event=event)
			participation.product.add(product)
		except ObjectDoesNotExist:
				pass
	return redirect("myGroceries:event_detail", name_event=name_event)

#Action de suppression de produits à la liste de courses de l'utilisateur
#@login_required
#def delete_products_to_event(request, name_event):
#	product = get_object_or_404(Product, name=name)
#	product.delete()
#	return redirect("/event/" + str(name_event))
