from django.conf import settings
import requests

def schedule_api():
    response = requests.get("https://nerdnucleusapidjango.onrender.com/api/news/startscrappy/")




