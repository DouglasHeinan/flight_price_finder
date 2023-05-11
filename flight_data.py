from flight_search import FlightSearch
from datetime import datetime, timedelta


class FlightData:
    def __init__(self):
        self.data = {"lowest_prices": {}, "iata_codes": {}}

    def load_data(self, cities):
        today = datetime.now().strftime("%d/%m/%Y")

        six_months = datetime.now() + timedelta(days=180)
        six_months = six_months.strftime("%d/%m/%Y")

        self.data["iata_codes"] = {city: FlightSearch().find_iata(city) for city in cities}

        for city in cities:
            print(f"Loading lowest prices for {city}")
            try:
                self.data["lowest_prices"][city] = FlightSearch().find_prices(
                    self.data["iata_codes"][city], today, six_months
                    )[0]
            except IndexError:
                print(f"No fares found for {city}")
                continue


