# Python modules
import urllib
import json
import requests
from twilio.rest import Client

# scripts imported
import crypto_script
import arrival_time


# Function returns current weather in Boston, MA
def get_boston_weather(boston_lat,boston_long):

    weather_api_key = '3faebebd5dd5b4b45f1280a39eec2e55'

    # This code handles the url endpoint for the api
    weather_api_endpoint = 'https://api.darksky.net/forecast/'
    destination = '{}/{},{}'.format(weather_api_key, boston_lat, boston_long)
    weather_url = weather_api_endpoint + destination

    # makes a request to api and responds with json
    weather_request = urllib.urlopen(weather_url)
    weather_response = json.load(weather_request)

    # sorting json for temperature and weather summary
    weather_temp =  weather_response["currently"]["temperature"]
    weather_summary = weather_response["minutely"]["summary"]

    return ("Bostons weather is %sF and %s" % (weather_temp, weather_summary.lower()))


# Function scrapes google news api and returns top article from wired
def get_news():

    news_url = 'https://newsapi.org/v2/top-headlines?sources=wired&apiKey=c8109dec291d46ca9c2de6be910b7d01'

    # Asks api for data
    news_request = urllib.urlopen(news_url)
    news_response = json.load(news_request)

    # returns top article
    article = news_response['articles'][0]['title']
    article_description = news_response['articles'][0]['description']

    return ("%s\n%s" % (article, article_description))


def text_report():

    account_sid = "AC31e70abcb2005f067084ce45d5bb85f0"

    # Your Auth Token from twilio.com/console
    auth_token  = "784e24c8676c280242ce66117557a271"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+16179849939",
        from_="+13392090722",
        body="\nGood Morning Shawn" + "\n\n" + "%s"
            %
            (
                get_boston_weather('42.3601', '-71.0589')
            )
    )


# The main function calls all functions and formats the CLI
def main():

    # text_report()

    print ('\n----------------------------------------------------------')
    print (get_boston_weather('42.3601', '-71.0589'))
    print ('----------------------------------------------------------\n')

    print ('-------------------------------------------------')
    print ("It will take you {} to get to Quincy College".format(arrival_time.rockland_to_quincy()))
    print ('-------------------------------------------------\n')

    print ('------------------------------------')
    print ("Litecoin Price Per Coin = {}\n".format(crypto_script.get_litecoin_price_from()))
    print ("Ripple XR Price Per Coin = {}".format(crypto_script.get_xr_price_from()))
    print ('------------------------------------\n')

    print ("wired.com Top Article\n")
    print (get_news())


print (main())
