import requests
from dotenv import load_dotenv
import os
from get_weekend import getNextWeekend
import json
import random
from datetime import datetime


load_dotenv()

api_key = os.getenv('API_KEY')
url = "https://app.ticketmaster.com/discovery/v2"

city = ["London"]
unit = "km"
startDateTime, endDateTime = getNextWeekend()
size = "100"
onsaleEndDate = str(datetime.now())

params1 = {"onsaleEndDate":onsaleEndDate,"sort":"random","size":size,"apikey": api_key, "city": city, "unit":unit,"startDateTime":startDateTime,"endDateTime":endDateTime}
findEvent = requests.get(f"{url}/events",params=params1)

eventIds = []
for event in findEvent.json()['_embedded']['events']:
    eventIds.append(event["id"])
eventId = eventIds[random.randint(0,len(eventIds))]
print(eventId)
params2 = {"id":eventId, "apikey": api_key}
eventDetails = requests.get(f"{url}/events/{eventId}", params=params2)

with open('data.json', 'w') as f:
    json.dump(eventDetails.json(), f)


