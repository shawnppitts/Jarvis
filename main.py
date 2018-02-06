'''
    Author: Shawn Pitts
    Project: Jarvis 1.0
    Project Description: Jarvis helps perform multiple tasks and google searches
    I make everyday and format them in the command line. Jarvis performs
    tasks such as giving me the Boston weather, giving me wired news, telling me the
    price of crypto currencies, and telling me my commute time to college.
'''

# Python modules
import urllib
import json
import requests
import sys
from twilio.rest import Client
from clint.textui import colored

# imported scripts
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

    # change text color depending on temperature
    if (weather_temp <= 32.5):
        weather_temp = colored.cyan(weather_temp)
    elif (weather_temp >= 33):
        weather_temp = colored.cyan(weather_temp)
    else:
        weather_temp = colored.yellow(weather_temp)


    return ("Bostons weather is %sF and %s" % (weather_temp, weather_summary.lower()))


# Function scrapes google news api and returns top article from wired
def get_news():

    news_url = 'https://newsapi.org/v2/top-headlines?sources=wired&apiKey=c8109dec291d46ca9c2de6be910b7d01'

    # requests api for data and responds with json
    news_request = urllib.urlopen(news_url)
    news_response = json.load(news_request)

    # returns the top article from json response
    article = news_response['articles'][0]['title']
    article_description = news_response['articles'][0]['description']

    return ("%s\n%s" % (article, article_description))


def text_report():

    account_sid = "AC31e70abcb2005f067084ce45d5bb85f0"

    # Your Auth Token from twilio.com/console
    auth_token  = "784e24c8676c280242ce66117557a271"

    client = Client(account_sid, auth_token)

    # message being sent to client
    message = client.messages.create(
        to="+16179849939",
        from_="+13392090722",
        body="\nGood Morning Shawn" + "\n\n" + "%s"
            %
            (
                get_boston_weather('42.3601', '-71.0589')
            )
    )


# function calls run in same order of declaration

def main():

    print ('\n----------------------------------------------------------')
    print (get_boston_weather('42.3601', '-71.0589'))
    print ('----------------------------------------------------------\n')

    print ('-------------------------------------------------')
    print ("Commute to Quincy College is {}".format(arrival_time.rockland_to_quincy()))
    print ("Commute to Mom and Dads is {}".format(arrival_time.rockland_to_boston()))
    print ('-------------------------------------------------\n')

    print ('------------------------------------')
    print ('Bitcoin Price Per Coin = {}\n'.format(crypto_script.get_bitcoin_price_from()))
    print ("Litecoin Price Per Coin = {}\n".format(crypto_script.get_litecoin_price_from()))
    print ("Ripple XR Price Per Coin = {}".format(crypto_script.get_xr_price_from()))
    print ('------------------------------------\n')

    print ("wired.com Top Article\n")
    print (get_news())


if __name__ == "__main__":
    main()
