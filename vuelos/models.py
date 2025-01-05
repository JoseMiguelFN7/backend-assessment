from django.db import models

#---- modelos de la base de datos ----

class Itinerary(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    id_agent = models.ForeignKey('Agents', on_delete=models.CASCADE)
    legs = models.ManyToManyField('Leg', related_name='legs') #relacion n-n con la tabla Leg
    def __str__(self):
        return f"{self.price} - {self.agent} ({self.agent_rating}★)" # resultado: £95 - Agencia 1 (4.5★)

class Leg(models.Model(models.Model)):
    departure_airport = models.ForeignKey('Airports', on_delete=models.CASCADE)
    arrival_airport = models.ForeignKey('Airports', on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    stops = models.IntegerField()
    airline_id = models.ForeignKey('Airlines', on_delete=models.CASCADE)
    duration_mins = models.IntegerField()
    
    def __str__(self):
        return f"{self.departure_airport} --> {self.arrival_airport} ({self.airline_name})" # resultado: LHR --> JFK (British Airways)

class Airline(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Agent(models.Model):
    name = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name

class Airport(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name