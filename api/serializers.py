from rest_framework import serializers
from vuelos.models import Itinerary, Leg, Airline, Agent, Airport

#Serializadores para que Django REST Framework pueda convertir los modelos en JSON

class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = "__all__"

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = "__all__"

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = "__all__"

class LegSerializer(serializers.ModelSerializer):
    departure_airport = AirportSerializer() # Expande los datos de departure_airport
    arrival_airport = AirportSerializer()   # Expande los datos de arrival_airport
    airline = AirlineSerializer()           # Expande los datos de airline
    
    class Meta:
        model = Leg
        fields = "__all__"

class ItinerarySerializer(serializers.ModelSerializer):
    legs = LegSerializer(many=True)  # Expande los datos de legs
    agent = AgentSerializer()        # Expande los datos de agent
    
    class Meta:
        model = Itinerary
        fields = "__all__"