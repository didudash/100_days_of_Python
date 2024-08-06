from dotenv import load_dotenv
import os
import requests

load_dotenv()
api_key = os.getenv("WEATHER_API_KEY")
lat = float(os.getenv("LATITUDE"))
lon = float(os.getenv("LONGITUDE"))
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
    print("Bring an umbrella")
else:
    print(
        """

                |
                |
      `.        |        .'
        `.    .---.    .'
           .~       ~.
              O   O   
-- -- -- (             ) -- -- --
               `-'     
           ~.       .~
        .'    ~---~    `.
      .'        |        `.
                |
                |    
                              

        """
    )
