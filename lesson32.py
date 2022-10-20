# Lesson 32 an API example

import urllib.request, urllib.parse, urllib.error
import json

service = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True :
    location = input('Enter a location: ')
    if len(location) < 1 : break

    url = service + urllib.parse.urlencode({'address': location})
    handle = urllib.request.urlopen(url)
    data = handle.read().decode()
    print('data', data)

    try :
        js = json.loads(data)
    except :
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('Failure to retrieve')
        continue
    
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    loc = js['results'][0]['formatted_address']
    print('Latitude:',lat,'Longitude:',lng,'Location:',loc)

# RETURNS >>>> You must use an API key to authenticate