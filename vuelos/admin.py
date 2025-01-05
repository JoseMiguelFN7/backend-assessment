from django.contrib import admin
from .models import Itinerary, Leg, Airline, Agent, Airport

class ItineraryAdmin(admin.ModelAdmin):
    list_display = ['cod', 'price', 'agent', 'agent_rating']  # Esto muestra los campos en la lista de itinerarios
    filter_horizontal = ('legs',)  # Esto muestra las legs de forma horizontal
    def agent_rating(self, obj):
        return obj.agent.rating  # Devuelve la calificación del agente
    agent_rating.short_description = 'Agent Rating'  # Etiqueta para la columna

admin.site.register(Itinerary, ItineraryAdmin)
admin.site.register(Leg)
admin.site.register(Airline)
admin.site.register(Agent)
admin.site.register(Airport)