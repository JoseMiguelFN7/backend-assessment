from django.urls import path
from . import views

urlpatterns = [
    path('itineraries', views.get_itineraries), #ruta para obtener todos los itinerarios
    path('itineraries/agent/<int:agent_id>/', views.get_itineraries_by_agent), #ruta para obtener los itinerarios de un agente
    path('legs', views.get_legs), #ruta para obtener todas las legs
    path('airlines', views.get_airlines), #ruta para obtener todas las aerolineas
    path('agents', views.get_agents), #ruta para obtener todos los agentes
    path('airports', views.get_airports), #ruta para obtener todos los aeropuertos
]