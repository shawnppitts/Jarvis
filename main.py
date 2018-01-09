# Python modules
import urllib2
import json
import requests
import pprint
import scrape_cryptoprice


# Api keys
weather_api_key = '3faebebd5dd5b4b45f1280a39eec2e55'
wired_api_key = '8d6732ddb67d45ac881138c940cb2733'

# Api endpoints
weather_api_endpoint = 'https://api.darksky.net/forecast/'


# Global param variables
boston_lat = '42.3601'
boston_long = '-71.0589'

# Function returns current weather in Boston, MA
def weather(boston_lat,boston_long):

    destination = '{}/{},{}'.format(weather_api_key, boston_lat, boston_long)

    weather_request = weather_api_endpoint + destination

    weather_response = urllib2.urlopen(weather_request)
    weather_data = json.load(weather_response)

    boston_temp =  weather_data["currently"]["temperature"]
    boston_summary = weather_data["minutely"]["summary"]

    return ("Bostons weather is %sF and %s" % (boston_temp, boston_summary.lower()))




# Function scrapes google news api and returns top article from wired
def get_news(url):

    # Asks api for data
    news_api_response = requests.get(url)

    # api responds with json
    data = news_api_response.json()

    # returns top article
    article = data['articles'][0]['title']
    article_description = data['articles'][0]['description']

    return ("%s\n%s" % (article, article_description))






# The main function calls all functions and formats the CLI
def main():

    print ('--------------------------------------------')
    print (weather(boston_lat, boston_long))
    print ('--------------------------------------------\n')

    print ('--------------------------------------------')
    print ("Litecoin Price Per Coin = {}\n".format(scrape_cryptoprice.get_lp('https://coinmarketcap.com/currencies/litecoin/')))
    print ("Ripple XR Price Per Coin = {}".format(scrape_cryptoprice.get_xr('https://coinmarketcap.com/currencies/ripple/')))
    print ('--------------------------------------------\n')

    print "wired.com Top Article\n"
    print get_news('https://newsapi.org/v2/top-headlines?sources=wired&apiKey=c8109dec291d46ca9c2de6be910b7d01')


print main()
