from rest_framework.response import Response
from rest_framework.decorators import api_view
from vuelos.models import Itinerary, Leg, Airline, Agent, Airport
from .serializers import ItinerarySerializer, LegSerializer, AirlineSerializer, AgentSerializer, AirportSerializer

#Funciones para los endpoints de la API

@api_view(["GET"])
def get_itineraries(request): #Obtener todos los itinerarios
    itineraries = Itinerary.objects.all()
    serializer = ItinerarySerializer(itineraries, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_itinerary(request, itinerary_id): #Obtener un itinerario
    itinerary = Itinerary.objects.filter(id=itinerary_id)
    serializer = ItinerarySerializer(itinerary, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_itineraries_by_agent(request, agent_id): #Obtener itinerarios de un agente
    if(agent_id):
        itineraries = Itinerary.objects.filter(agent_id=agent_id)
        
        if not (itineraries.exists()):
            return Response("No se encontraron itinerarios del agente proporcionado")
        
        serializer = ItinerarySerializer(itineraries, many=True)
        return Response(serializer.data)
    else:
        return Response("No se ha proporcionado un agente")

@api_view(["GET"])
def get_itineraries_with_leg(request, leg_id): #Obtener itinerarios que contengan una leg especifica
    if(leg_id):
        itineraries = Itinerary.objects.filter(legs__id=leg_id)
        
        if not (itineraries.exists()):
            return Response("No se encontraron itinerarios que contengan esta leg")
        
        serializer = ItinerarySerializer(itineraries, many=True)
        return Response(serializer.data)
    else:
        return Response("No se ha proporcionado una leg")

@api_view(["GET"])
def get_legs(request): #Obtener todas las legs
    legs = Leg.objects.all()
    serializer = LegSerializer(legs, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_leg(request, leg_id): #Obtener una leg
    leg = Leg.objects.filter(id=leg_id)
    serializer = LegSerializer(leg, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_airlines(request): #Obtener todas las aerolineas
    airlines = Airline.objects.all()
    serializer = AirlineSerializer(airlines, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_airline(request, airline_id): #Obtener una aerolinea
    airline = Airline.objects.filter(id=airline_id)
    serializer = AirlineSerializer(airline, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_agents(request): #Obtener todos los agentes
    agents = Agent.objects.all()
    serializer = AgentSerializer(agents, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_agent(request, agent_id): #Obtener un agente
    agent = Agent.objects.filter(id=agent_id)
    serializer = AgentSerializer(agent, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_airports(request):
    airports = Airport.objects.all() #Obtener todos los aeropuertos
    serializer = AirportSerializer(airports, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_airport(request, airport_id):
    airport = Airport.objects.filter(id=airport_id) #Obtener un aeropuerto
    serializer = AirportSerializer(airport, many=True)
    return Response(serializer.data)