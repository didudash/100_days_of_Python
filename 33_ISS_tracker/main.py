import requests

"""
requests response codes: 
1XX: Informational
2XX: Success 
3XX: Redirection
4XX: Client Error  
5XX: Server Error 
"""

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]
iss_position = (latitude, longitude)
print(iss_position)
