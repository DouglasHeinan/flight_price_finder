from twilio.rest import Client


class NotificationManager:

    def alert(self, city, city_code, landing, leaving, price):
        account_sid = "AC8e8ad8bae34cfeb88fd810a534cf4868"
        auth_token = "9640bf94b75f9a747fe6346d5e0fb56f"
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body=f"Your flight from LON to {city_code} has dropped to {price}! You could be in {city} "
                     f"from {landing} to {leaving}. Book now!",
                from_="+19035013182",
                to="+15305154169"
        )
