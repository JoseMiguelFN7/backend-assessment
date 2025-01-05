from django.db import models

#---- modelos de la base de datos ----

class Itinerary(models.Model):
    cod = models.CharField(max_length=5, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    agent = models.ForeignKey('Agent', on_delete=models.CASCADE)
    legs = models.ManyToManyField('Leg', related_name='legs') #relacion n-n con la tabla Leg
    def __str__(self):
        return f"£{self.price} - {self.agent} ({self.agent.rating}★)" # resultado: £95 - Agencia 1 (4.5★)

class Leg(models.Model):
    cod = models.CharField(max_length=5, null=True, default=None)
    departure_airport = models.ForeignKey('Airport', on_delete=models.CASCADE, related_name='departure_airport')
    arrival_airport = models.ForeignKey('Airport', on_delete=models.CASCADE, related_name='arrival_airport')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    stops = models.IntegerField()
    airline = models.ForeignKey('Airline', on_delete=models.CASCADE)
    duration_mins = models.IntegerField()
    
    def __str__(self):
        return f"{self.departure_airport} --> {self.arrival_airport} ({self.airline.name})" # resultado: LHR --> JFK (British Airways)

class Airline(models.Model):
    name = models.CharField(max_length=100)
    cod = models.CharField(max_length=5, null=True, default=None)
    
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