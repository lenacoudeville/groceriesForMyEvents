from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


class Event(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.TextField(default='')
	start_date = models.DateField(auto_now = False)
	end_date = models.DateField(auto_now = False)
	description = models.CharField(max_length=250)
	id_host = models.ForeignKey(User, on_delete=models.CASCADE)


class Invitation(models.Model):
    id_invit = models.AutoField(primary_key=True)
    id_event = models.ForeignKey(Event, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=0)


class Product(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.TextField()


class InvitProd(models.Model):
	id_invit = models.ForeignKey(Invitation, on_delete=models.CASCADE)
	id_prod = models.ForeignKey(Product, on_delete=models.CASCADE)