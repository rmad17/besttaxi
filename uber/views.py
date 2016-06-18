from django.http import JsonResponse
from django.conf import settings

import requests
import math

from uber_rides.session import Session
from uber_rides.client import UberRidesClient
from .uber_secrets import UBER_SERVER_TOKEN
import uber.fares as fares

from besttaxi.base_secrets import GOOGLE_MAPS_DIRECTIONS_API_KEY

# Create your views here.


# Get Uber Session
def get_uber_session():
    session = Session(server_token=UBER_SERVER_TOKEN)
    return session


def get_uber_rides_client():
    session = get_uber_session()
    client = UberRidesClient(session)
    return client


def get_availability(request):
    if request.method == 'GET':
        origin_lat = request.GET.get('olat')
        origin_lng = request.GET.get('olng')
        if origin_lat and origin_lng:
            client = get_uber_rides_client()
            response = client.get_products(origin_lat, origin_lng)
            products = response.json.get('products')
            return JsonResponse(products, status=200, safe=False)
    else:
        return JsonResponse({'status': 'Invalid Request'}, status=406)


def get_directions_data(request):
    if request.method == 'GET':
        origin = request.GET.get('origin')
        destination = request.GET.get('destination')
        directions_url = settings.GOOGLE_MAPS_DIRECTIONS_BASE_API_URL + \
            settings.GOOGLE_MAPS_DIRECTIONS_BASE_API_URL_OUTPUT_FORMAT + \
            '?origin=' + origin + '&destination=' + destination + \
            '&alternatives=true&key=' + GOOGLE_MAPS_DIRECTIONS_API_KEY
        directions_data = requests.get(directions_url)
        prices = get_route_price_map(directions_data)
        return JsonResponse(prices, status=200, safe=False)
    else:
        return JsonResponse({'status': 'Invalid Request'}, status=406)


def get_route_price_map(directions_data):
    routes = directions_data.json().get('routes')
    route_prices = []
    city = fares.BENGALURU
    for route in routes:
        distance = 0
        duration = 0
        route_ubers = {}
        for leg in route.get('legs'):
            distance += leg.get('distance').get('value')
            duration += leg.get('distance').get('value')
        for key, value in city.items():
            route_price = value['base'] + \
                    (math.ceil(duration/60.0) * value['per_min']) + \
                    ((distance/1000.0) * value['per_km'])
            route_ubers[key] = route_price
        route_prices.append(route_ubers)
    return route_prices
