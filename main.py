'''
This program serves as an assistant to my daily routine
'''

import urllib2
import json
import requests
import pprint
import scrape_cryptoprice

weather_api_key = '3faebebd5dd5b4b45f1280a39eec2e55'
wired_api_key = '8d6732ddb67d45ac881138c940cb2733'


print ("\nHi Shawn here is today's dashboard:\n")
# 1. First function returns current weather in Boston, MA
def weather(latitude,longitude):
    weather_url_endpoint = 'https://api.darksky.net/forecast/'

    destination_req = '{}/{},{}'.format(weather_api_key, latitude, longitude)

    weather_request = weather_url_endpoint + destination_req

    weather_response = urllib2.urlopen(weather_request)
    weather_data = json.load(weather_response)

    boston_weather =  weather_data["currently"]["temperature"]
    boston_weather_summary = weather_data["currently"]["summary"]

    return "Boston Weather is %s degrees and %s" % (boston_weather, boston_weather_summary)


# 2. This function scrapes techcrunch api and returns top article
def get_news(url):

    # Asks api for data
    news_api_response = requests.get(url)

    # api responds with json
    data = news_api_response.json()

    # returns top article
    article = data['articles'][0]['title']
    article_description = data['articles'][0]['description']

    return ("%s\n%s" % (article, article_description))


# Function calls
print ('--------------------------------------------')
print (weather('42.3601', '-71.0589'))
print ('--------------------------------------------\n')

print ('--------------------------------------------')
print ("Litecoin Price Per Coin = {}\n".format(scrape_cryptoprice.get_lp('https://coinmarketcap.com/currencies/litecoin/')))
print ("Ripple XR Price Per Coin = {}".format(scrape_cryptoprice.get_xr('https://coinmarketcap.com/currencies/ripple/')))
print ('--------------------------------------------\n')

print "wired.com Top Article\n"
print get_news('https://newsapi.org/v2/top-headlines?sources=wired&apiKey=c8109dec291d46ca9c2de6be910b7d01')
