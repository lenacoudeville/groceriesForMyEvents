from django.db import models
from  django.contrib.auth.models import User


class event(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.TextField(default='')
	start_date = models.DateField(auto_now = False)
	end_date = models.DateField(auto_now = False)
	description = models.CharField(max_length=500)
	id_host = models.ForeignKey(User, on_delete=models.PROTECT)
	level_total = models.IntegerField()


class invitation(models.Model):
    id_invit = models.AutoField(primary_key=True)
    id_event = models.ForeignKey(event, on_delete=models.PROTECT)
    id_user = models.ForeignKey(User, on_delete=models.PROTECT)
    accepted = models.BooleanField(default=0)


class product(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.TextField()


class invitProd(models.Model):
	id_invit = models.ForeignKey(invitation, on_delete=models.PROTECT)
	id_prod = models.ForeignKey(product, on_delete=models.PROTECT)