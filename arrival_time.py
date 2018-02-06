import urllib
import json
import requests
import pprint

# 87+Marlborough+Street+Boston,MA
# 1+Charles+Street+Rockland,MA

def rockland_to_quincy():
    # Google directions API url endpoint shortened
    endpoint_url = "https://maps.googleapis.com/maps/api/directions/json?origin=&destination=1250+Hancock+Street+Quincy,MA&key=AIzaSyBA9_TNdq1Sg9idLBsSvGi30pQqm0YfSZc"

    eta_request = urllib.urlopen(endpoint_url)
    eta_response = json.load(eta_request)

    final_eta = eta_response['routes'][0]['legs'][0]['duration']['text']

    return final_eta


def rockland_to_boston():

    endpoint_url = "https://maps.googleapis.com/maps/api/directions/json?origin=&destination=&key=AIzaSyBA9_TNdq1Sg9idLBsSvGi30pQqm0YfSZc"

    eta_request = urllib.urlopen(endpoint_url)
    eta_response = json.load(eta_request)

    final_eta = eta_response['routes'][0]['legs'][0]['duration']['text']

    return final_eta
