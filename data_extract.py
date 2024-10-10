import requests
from dotenv import load_dotenv
import os
from get_weekend import getNextWeekend
import json
import random
from datetime import datetime


load_dotenv()

def extractData():
    # load api key from .env
    api_key = os.getenv('API_KEY')
    url = "https://app.ticketmaster.com/discovery/v2"

    # currently hardcoded parameters
    city = ["London"]
    unit = "km"
    startDateTime, endDateTime = getNextWeekend()
    size = "100"
    onsaleEndDate = str(datetime.now())

    # request 100 events that meet the criteria
    params1 = {"onsaleEndDate":onsaleEndDate,"sort":"random","size":size,"apikey": api_key, "city": city, "unit":unit,"startDateTime":startDateTime,"endDateTime":endDateTime}
    findEvent = requests.get(f"{url}/events",params=params1)

    # extract events' ids
    eventIds = []
    for event in findEvent.json()['_embedded']['events']:
        eventIds.append(event["id"])

    # randomly choose an event
    eventId = eventIds[random.randint(0,len(eventIds))]

    # call that event's details
    params2 = {"id":eventId, "apikey": api_key}
    eventDetails = requests.get(f"{url}/events/{eventId}", params=params2)

    return eventDetails.json()



