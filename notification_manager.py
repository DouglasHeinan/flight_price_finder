# from twilio.rest import Client
import os
import smtplib

AUTH_TOKEN = os.environ['AUTH_TOKEN']
ACCOUNT_SID = os.environ['ACCOUNT_SID']
FROM_NUM = os.environ['FROM_NUM']
TO_NUM = os.environ['TO_NUM']
MY_EMAIL = os.environ['MY_EMAIL']
MY_PASSWORD = os.environ['MY_PASSWORD']


class NotificationManager:

    # Code no longer runs; twilio api requires paid number.
    # def alert(self, city, city_code, landing, leaving, price):
    #     client = Client(ACCOUNT_SID, AUTH_TOKEN)
    #     message = client.messages.create(
    #         body=f"Your flight from LON to {city_code} has dropped to {price}!
    #           You could be in {city} from {landing} to {leaving}. Book now!",
    #         from_=FROM_NUM,
    #         to=TO_NUM
    #     )

    def send_emails(self, user_info, low_price, city):
        users = [row["firstName"] for row in user_info]
        i = 0
        for user_name in users:
            user_email = user_info[i]["email"]
            price = low_price
            message = f"{user_name},\nWe just wanted to let you know that fares from London to {city} have fallen to " \
                      f"${price}"
            i += 1

            with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=user_email,
                                    msg=f"Subject:Flight Deals!\n\n{message}")
