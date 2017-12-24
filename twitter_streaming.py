from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import boto3
import urllib.request
import urllib.parse
from elasticsearch import Elasticsearch


#Variables that contains the user credentials to access Twitter API
access_token = "2801190920-AwZu0nx9BBCVtgLKjD8BpQTLo7M2iep9ZyGRtQM"
access_token_secret = "0CLyy2Hc5M9mSrdxLcoM82naXZg7IAFgZCEvuUt14lN4s"
consumer_key = ""
consumer_secret = ""



#This is a basic listener that just prints received tweets to stdout.

class StdOutListener(StreamListener):

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



    def load_json_multiple(segments):
        chunk = ""
        for segment in segments:
            chunk += segment
            try:
                yield json.loads( chunk )
                chunk = ""
            except ValueError:
                pass

    def on_data(self, data):
        try:
            data=json.loads(data)
            if data['user']['location'] != '':
                with open( 'leaflet/markers.js', 'a+' ) as f:
                    lines = f.readlines()
                    f.close()

                    dict = {"name": data['text']}
                    dict.update(StdOutListener.decode_address_to_coordinates(repr(data['user']['location'])))

                    lines = lines[:-1]
                    with open( 'leaflet/markers.js', 'a+' ) as f:
                        f.writelines(lines)
                        f.write("," + str(dict)+"\n")
                        f.close()

           # s3 = boto3.resource( 's3' )
           # s3.Object( 'elasticbeanstalk-us-east-2-274213482424', 'markers.js' ).upload_file('./leaflet/markers.js')
        except: print("Unable to load")
        return True

    def on_error(self, status):
        print(status)




if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    #api = tweepy.API(auth,wait_on_rate_limit=True)
    stream.filter(track=['music','bollywood','hollywood','car','donald trump','rocknroll','metal'])
