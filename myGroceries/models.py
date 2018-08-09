from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


class Event(models.Model):
    name = models.CharField(max_length=250)
    start_date = models.DateField(auto_now = False)
    end_date = models.DateField(auto_now = False)
    description = models.TextField(default='')
    host = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Invitation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.event.name)


class Product(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Participation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)

    def __str__(self):
        return self.user.username + " - " + self.event.name
