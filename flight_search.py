import requests
import os

API_KEY = os.environ['API_KEY']

class FlightSearch:

    def __init__(self):

        self.header = {
            "apikey": API_KEY
        }

    def find_iata(self, city):
        parameters = {
            "term": city
        }
        response = requests.get("https://tequila-api.kiwi.com/locations/query",
                                params=parameters, headers=self.header)
        if len(response.json()['locations'][0]['code']) == 3:
            return response.json()['locations'][0]['code']
        else:
            return response.json()['locations'][0]['locations_nearby'][0]['id']

    def find_prices(self, city, today, six_months):
        parameters = {
            "fly_from": "LON",
            "fly_to": city,
            "dateFrom": today,
            "dateTo": six_months,
            "sort": "price",
        }
        response = requests.get("https://tequila-api.kiwi.com/v2/search",
                                params=parameters, headers=self.header)
        return response.json()["data"]
