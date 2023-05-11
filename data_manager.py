import requests


class DataManager:

    def __init__(self):
        self.price_response = requests.get("https://api.sheety.co/e4a5077b0a88fb08a874100d083714a9/flightDeals/prices")
        self.prices = self.price_response.json()["prices"]
        self.user_response = requests.get("https://api.sheety.co/e4a5077b0a88fb08a874100d083714a9/flightDeals/users")
        self.users = self.user_response.json()["users"]

    def add_iata(self, iata_codes):
        """Adds a column of iata codes to the spreadsheet."""
        for index, iata in enumerate(iata_codes):
            # Starting from index 2 because spreadsheet starts from index 1 and there's a header.
            index += 2
            params = {
                "price": {
                    "iataCode": iata,
                }
            }
            requests.put(f"https://api.sheety.co/e4a5077b0a88fb08a874100d083714a9/flightDeals/prices/{index}",
                         json=params)
