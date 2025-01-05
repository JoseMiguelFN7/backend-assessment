from django.urls import path
from . import views

urlpatterns = [
    path('itineraries', views.get_itineraries), #ruta para obtener todos los itinerarios
    path('itinerary/<int:itinerary_id>', views.get_itinerary), #ruta para obtener un itinerario
    path('itineraries/agent/<int:agent_id>/', views.get_itineraries_by_agent), #ruta para obtener los itinerarios de un agente
    path('itineraries/leg/<int:leg_id>/', views.get_itineraries_with_leg), #ruta para obtener los itinerarios que contienen una leg
    path('legs', views.get_legs), #ruta para obtener todas las legs
    path('leg/<int:leg_id>', views.get_leg), #ruta para obtener una leg
    path('airlines', views.get_airlines), #ruta para obtener todas las aerolineas
    path('airline/<int:airline_id>', views.get_airline), #ruta para obtener una aerolinea
    path('agents', views.get_agents), #ruta para obtener todos los agentes
    path('agent/<int:agent_id>', views.get_agent), #ruta para obtener un agente
    path('airports', views.get_airports), #ruta para obtener todos los aeropuertos
    path('airport/<int:airport_id>', views.get_airport), #ruta para obtener un aeropuerto
]