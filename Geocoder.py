import urllib.request
import urllib.parse
import json
import time
import requests

# Google API to get lat/long
def decode_address_to_coordinates(address):
        params = {
                'address' : address,
                'sensor' : 'false',
        }
        url = 'http://maps.google.com/maps/api/geocode/json?' + urllib.parse.urlencode(params)
        response = urllib.request.urlopen(url)
        result = json.load(response)
        try:
                print("The Location for this tweet is %s\n" % result['results'][0]['geometry']['location'])
                return result['results'][0]['geometry']['location']
        except:
                return None

#Google API to get all geo info
def GoogGeoAPI(address,api="",delay=5):
  base = r"https://maps.googleapis.com/maps/api/geocode/json?"
  addP = "address=" + address.replace(" ","+")
  GeoUrl = base + addP + "&key=" + api
  response = urllib.request.urlopen(GeoUrl)
  jsonRaw = response.read()
  jsonData = json.loads(jsonRaw)
  if jsonData['status'] == 'OK':
    resu = jsonData['results'][0]
    finList = [resu['formatted_address'],resu['geometry']['location']['lat'],resu['geometry']['location']['lng']]
  else:
    finList = [None,None,None]
  time.sleep(delay) #in seconds
  return finList

def coodtoAddress(latitude,longitude,sensor=True):
    base = "http://maps.googleapis.com/maps/api/geocode/json?"
    params = "latlng={lat},{lon}&sensor={sen}".format( lat=latitude, lon=longitude, sen=sensor )
    url = "{base}{params}".format( base=base, params=params )
    response = requests.get( url )
    print(response.json()['results'][0]['formatted_address'])
    return response.json()['results'][0]['formatted_address']

print(decode_address_to_coordinates('India'))

