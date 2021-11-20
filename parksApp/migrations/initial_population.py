from django.db import migrations
from django.db.migrations import operations
import requests
import json

from parksApp.models import Park

def populate(apps, schemea_editor):
    apiKey="CNfDJ9AMlCzEZytqNvovbajRd7cGVcElLeKUS2bz"
    url=f"https://developer.nps.gov/api/v1/parks?api_key={apiKey}"
    response = requests.get(url)
    json_response=json.loads(response.text)
    for parkData in json_response["data"]:
        park = Park()
        park.name=parkData["fullName"]
        park.link_to_website=parkData["url"]
        park.description=parkData["description"]
        park.directionsInfo=parkData["directionsInfo"]
        park.directionsURL=parkData["directionsUrl"]
        park.image=parkData["images"][0]["url"]
        park.marked=False
        park.visited=False
        park.save()



class Migration(migrations.Migration):
    dependencies=[
        ('parksApp','0001_initial'),
    ]
    operations=[
        migrations.RunPython(populate)
    ]