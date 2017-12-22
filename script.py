'''
This program serves as an assistant to my daily routine
'''

import urllib2
import json
import requests
import pprint

print "\nHi Shawn here is today's dashboard:\n"


# 1. First function returns current weather in Boston, MA
def weather(latitude,longitude):
    weather_api_key = '3faebebd5dd5b4b45f1280a39eec2e55'
    weather_url_endpoint = 'https://api.darksky.net/forecast/'

    destination_req = '{}/{},{}'.format(weather_api_key, latitude, longitude)

    weather_request = weather_url_endpoint + destination_req

    weather_response = urllib2.urlopen(weather_request)
    weather_data = json.load(weather_response)

    boston_weather =  weather_data["currently"]["temperature"]

    return "Boston Weather = {} degrees".format(boston_weather)

print '------------------------------------'
print weather('42.3601', '-71.0589')
print '------------------------------------'



# 2. This function scrapes techcrunch api and returns top article
print "\nHere is TechCrunch's Top Article...\n"
def techcrunch_news():

    techcrunch_api_key = '8d6732ddb67d45ac881138c940cb2733'

    # url endpoint
    techcrunch_url = ('https://newsapi.org/v2/top-headlines?'
           'sources=TechCrunch&'
           'apiKey=8d6732ddb67d45ac881138c940cb2733')

    # Asks api for data
    news_api_response = requests.get(techcrunch_url)

    # api responds with json
    data = news_api_response.json()

    # returns top article
    return data['articles'][0]['description']


print techcrunch_news()
