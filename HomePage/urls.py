from django.conf.urls import url, include
from . import views

app_name = "HomePage"

urlpatterns = [
	
	url(r'^$', views.HomePage, name='HomePage')
]