from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager


def main():

    sheet_data = DataManager()
    users = sheet_data.users
    cities = [row["city"] for row in sheet_data.prices]
    flight_data = FlightData()
    flight_data.load_data(cities)
    iata_list = flight_data.data["iata_codes"].values()

    # If iata codes don't exist, add them
    if sheet_data.prices[2]["iataCode"] == "":
        sheet_data.add_iata(iata_list)

    for row in sheet_data.prices:
        try:
            current_info = flight_data.data["lowest_prices"][row["city"]]
        except KeyError:
            print("keyerror")
            continue
        if current_info["price"] < row["lowestPrice"]:
            city = current_info["cityTo"]
            leave = current_info["local_arrival"].split("T")[0]
            home = current_info["local_departure"].split("T")[0]
            # *****THE 2 LINES BELOW ARE COMMENTED OUT SINCE TWILIO BEGAN CHARGING FOR PHONE NUMBERS...*****
            # print(f"Sending you an SMS to alert you to the lowest fares for {city}!")
            # NotificationManager().alert(city, flight_data.data["iata_codes"][city], home, leave, current_info["price"])
            print("Sending your users an email notification!")
            NotificationManager().send_emails(users, current_info["price"], city)


if __name__ == '__main__':
    main()
