from django.contrib import admin
from .models import Itinerary, Leg, Airline, Agent, Airport

admin.site.register(Itinerary)
admin.site.register(Leg)
admin.site.register(Airline)
admin.site.register(Agent)
admin.site.register(Airport)