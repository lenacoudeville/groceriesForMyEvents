from django.conf.urls import url, include
from . import views

app_name = "myGroceries"

urlpatterns = [
	
	url(r'^$', views.homepage, name='homepage'),
	url(r'^event/create/$', views.create_event, name='create_event'),
	url(r'^event/(?P<id>\d+)/$', views.event_detail, name='event_detail'),
]