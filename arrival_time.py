import urllib
import json
import requests
import pprint

def rockland_to_quincy():
    # Google directions API url endpoint shortened
    endpoint_url = "https://tinyurl.com/ydepge9c"

    eta_request = urllib.urlopen(endpoint_url)
    eta_response = json.load(eta_request)

    final_eta = eta_response['routes'][0]['legs'][0]['duration_in_traffic']['text']

    return final_eta
