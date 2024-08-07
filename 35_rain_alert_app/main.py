from dotenv import load_dotenv
import os
import requests
from twilio.rest import Client

load_dotenv()
api_key = os.getenv("WEATHER_API_KEY")
lat = float(os.getenv("LATITUDE"))
lon = float(os.getenv("LONGITUDE"))
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_phone = os.getenv("FROM_PHONE")
from_phone_whatsapp = os.getenv("FROM_PHONE_WHATSAPP")
to_phone = os.getenv("TO_PHONE")

owm_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

# cnt:4 is equal to 12 hours because the api give data every 3 hours
# If no cnt has been provided it gives for 5 days (40 timestamps)
weather_params = {"lat": lat, "lon": lon, "appid": api_key, "cnt": 4}
response = requests.get(owm_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
condition_codes = []
for timestamp in range(len(weather_data["list"])):
    # first weather id
    condition_codes.append(int(weather_data["list"][timestamp]["weather"][0]["id"]))
if any(map(lambda x: x < 700, condition_codes)):
    message_body = "Bring an umbrella ( ͡° ʖ̯ ͡°)"
else:

    message_body = "Sunny vibez (=^･ｪ･^=))ﾉ彡"

client = Client(account_sid, auth_token)

message = client.messages.create(
    body=message_body,
    # from_=from_phone,
    from_=f"whatsapp:{from_phone_whatsapp}",
    # to=to_phone,
    to=f"whatsapp:{to_phone}",
)
print(message.status)
