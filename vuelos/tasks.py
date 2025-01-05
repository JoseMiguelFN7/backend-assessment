from __future__ import absolute_import, unicode_literals
from django.utils import timezone
from celery import shared_task
import requests
import json

from vuelos.models import Itinerary, Leg, Airline, Agent, Airport

@shared_task
def crearArchivo(text):
    # Crear un archivo de texto y escribir "Hola" en él
    file_path = 'hola.txt'

    with open(file_path, 'w') as file:
        file.write(text)

    return 'archivo creado'

@shared_task
def fetch_json(url):
    response = requests.get(url)
    data = response.json()
    
    #importar aerolineas
    airlines = set({(leg["airline_name"], leg["airline_id"]) for leg in data["legs"]}) #se usa un set para evitar duplicados

    for airline_name, airline_cod in airlines:
        Airline.objects.get_or_create( #si no existe la aerolinea, la crea
            cod=airline_cod,
            defaults={"name": airline_name}
        )
        
    #importar agentes
    agents = set({(itinerary["agent"], itinerary["agent_rating"]) for itinerary in data["itineraries"]}) #se usa un set para evitar duplicados
    
    for agent_name, agent_rating in agents:
        Agent.objects.get_or_create( #si no existe el agente, la crea
            name=agent_name,
            defaults={"rating": agent_rating}
        )
    
    #importar aeropuertos
    airports = set() #se usa un set para evitar duplicados
    
    for leg in data["legs"]:
        airports.add(leg["departure_airport"])
        airports.add(leg["arrival_airport"])

    for airport_name in airports:
        Airport.objects.get_or_create(name=airport_name) #si no existe el aeropuerto, lo crea
    
    #importar legs
    for leg_data in data["legs"]:
        leg_cod = leg_data["id"]
        leg_dep_airp_name = leg_data["departure_airport"]
        leg_arr_airp_name = leg_data["arrival_airport"]
        leg_dep_time = leg_data["departure_time"]
        leg_arr_time = leg_data["arrival_time"]
        leg_stops = leg_data["stops"]
        leg_airline_cod = leg_data["airline_id"]
        leg_duration_mins = leg_data["duration_mins"]
        
        #buscar los aeropuertos
        leg_dep_airp = Airport.objects.get(name = leg_dep_airp_name)
        leg_arr_airp = Airport.objects.get(name = leg_arr_airp_name)
        
        #buscar la aerolinea
        leg_airline = Airline.objects.get(cod = leg_airline_cod)
        
        #Crear Leg si no existe en la BDD
        Leg.objects.get_or_create(
            cod=leg_cod,
            defaults={
                "departure_airport": leg_dep_airp,
                "arrival_airport": leg_arr_airp,
                "departure_time": leg_dep_time,
                "arrival_time": leg_arr_time,
                "stops": leg_stops,
                "airline": leg_airline,
                "duration_mins": leg_duration_mins,
            }
        )
    
    #importar itinerarios
    itineraries_data = data["itineraries"]

    for itinerary_data in itineraries_data:
        itinerary_cod = itinerary_data["id"]
        itinerary_legs = itinerary_data["legs"]
        itinerary_price = itinerary_data["price"]
        itinerary_agent_name = itinerary_data["agent"]
        
        #obtenemos los objetos de las legs
        legs_objects = Leg.objects.filter(cod__in=itinerary_legs)
        
        #buscamos el agente por su nombre
        itinerary_agent = Agent.objects.get(name = itinerary_agent_name)
        
        #crear itinerario si no existe en la bdd (usamos itinerary, created para separar la tupla y quedar con el objeto itinerary)
        itinerary, created = Itinerary.objects.get_or_create(
            cod=itinerary_cod,
            defaults={
                "price": float(itinerary_price[1:]), #cortamos el signo de £ y solo almacenamos el flotante
                "agent": itinerary_agent,
            }
        )
        
        #asociamos el itinerario creado con sus legs
        itinerary.legs.set(legs_objects)
        
        #guardamos el itinerario
        itinerary.save()
    
    return {"status": "success", "message": "Datos importados correctamente."}