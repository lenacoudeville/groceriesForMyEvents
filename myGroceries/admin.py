from django.contrib import admin
from .models import Event, Invitation, InvitProd, Product

admin.site.register(Event)
admin.site.register(Invitation)
admin.site.register(InvitProd)
admin.site.register(Product)