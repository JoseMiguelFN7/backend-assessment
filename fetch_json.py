import os
import django

# Configura Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()

from vuelos.tasks import fetch_json

url = 'https://raw.githubusercontent.com/Skyscanner/full-stack-recruitment-test/main/public/flights.json'
fetch_json.delay(url)