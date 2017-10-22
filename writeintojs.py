import json
import urllib.request
import urllib.parse
import time
import requests


def decode_address_to_coordinates(address):
    params = {'address': address, 'sensor': 'false', }
    url = 'http://maps.google.com/maps/api/geocode/json?' + urllib.parse.urlencode( params )
    response = urllib.request.urlopen( url )
    result = json.load( response )
    try:
        print( "The Location for this tweet is %s\n" % result['results'][0]['geometry']['location'] )
        return result['results'][0]['geometry']['location']
    except:
        return None

with open('./leaflet/markers.js','r') as f:
    lines=f.readlines()

dict={"name":"India","url":"https://en.wikipedia.org/wiki/India"}
dict.update(decode_address_to_coordinates('India'))
print(dict)

lines=lines[:-1]
with open('./leaflet/markers.js','w') as f:
    f.writelines(lines)
    f.write(","+str(dict)+"];")





"""
with open('./leaflet/markers.js','a+') as f:
    f.write(",\n"+str(dict)+"];")
"""




