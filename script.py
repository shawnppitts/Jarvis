'''
This program serves as an assistant to my daily routine
'''

import urllib2
import json
import requests
import pprint
import scrape

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

    return "Boston Weather is {} degrees and {}".format(boston_weather, boston_weather_summary)


# 2. This function scrapes techcrunch api and returns top article
def wired_news():

    # url endpoint
    wired_url = ('https://newsapi.org/v2/top-headlines?'
           'sources=wired&'
           'apiKey=8d6732ddb67d45ac881138c940cb2733')

    # Asks api for data
    news_api_response = requests.get(wired_url)

    # api responds with json
    data = news_api_response.json()

    # returns top article
    article_one = data['articles'][0]['title']
    article_two = data['articles'][1]['title']
    article_three = data['articles'][2]['title']

    return "1. {}\n\n2. {}\n\n3. {}\n".format(article_one, article_two, article_three)



# Function calls
print ('--------------------------------------------')
print (weather('42.3601', '-71.0589'))
print ('--------------------------------------------\n')

print ('--------------------------------------------')
print ("Litecoin Price Per Coin = {}".format(scrape.get_lp('https://coinmarketcap.com/currencies/litecoin/')))
print ('--------------------------------------------')


print "\n\nWired.com Top Articles\n"
print wired_news()
