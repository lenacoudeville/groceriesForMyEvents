from django.urls import path, include
from . import views

app_name = "myGroceries"

urlpatterns = [
	
	path('', views.homepage, name='homepage'), #page d'accueil
	path('event/create/', views.create_event, name='create_event'), #création d'événement
	path('event/<name_event>/delete/', views.delete_event, name='delete_event'), #delete l'événement action
	#path('event/<name_event>/update/', views.update_event, name='update_event'), #update l'événement
	path('event/<name_event>/', views.event_detail, name='event_detail'), #détail de l'événement
	path('event/invite/<name_event>/', views.invitation_to_my_event, name='invitation_to_my_event'), #inviter à l'événement
	path('event/invite/<name_event>/act', views.invitation_to_my_event_act, name='invitation_to_my_event_act'), #inviter à l'événement action
	path('event/invite/<name_event>/accept', views.invitation_to_event_accept, name='invitation_to_event_accept'), #accepter l'événement action
	path('event/invite/<name_event>/refuse', views.invitation_to_event_refuse, name='invitation_to_event_refuse'), #refuser l'événement action
	path('event/participe/<name_event>/cancel', views.participation_to_event_cancel, name='participation_to_event_cancel'), #annuler la participation à l'événement action
	#path('event/participe/<name_event>/<id_invite>/delete', views.participation_to_my_event_delete, name='participation_to_my_event_delete'), #supprimer une participation à mon événement action
	#path('event/invite/<name_event>/<id_invite>/delete', views.invitation_to_my_event_delete, name='invitation_to_my_event_delete'), #supprimer une invitation à mon événement action
	path('event/<name_event>/courses/', views.add_products_to_event, name='add_products_to_event'), #ajouter des produits à sa liste de courses
	path('event/<name_event>/courses/act', views.add_products_to_event_act, name='add_products_to_event_act'), #ajouter des courses action
	#path('event/<name_event>/courses/<id_invite>/delete/', views.delete_products_to_event, name='delete_products_to_event'), #suppression de ses courses action
] 