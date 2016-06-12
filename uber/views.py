from django.http import JsonResponse

from uber_rides.session import Session
from uber_rides.client import UberRidesClient
from .uber_secrets import UBER_SERVER_TOKEN
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
        lat = request.GET.get('lat')
        lng = request.GET.get('lng')
        if lat and lng:
            client = get_uber_rides_client()
            response = client.get_products(lat, lng)
            products = response.json.get('products')
            return JsonResponse(products, status=200, safe=False)
    else:
        return JsonResponse({'status': 'Invalid Request'}, status=406)
