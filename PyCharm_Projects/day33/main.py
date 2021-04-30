import json
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

response.raise_for_status()

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (latitude, longitude)
# print(iss_position)

my_address = {"latitude": 51.399930, "longitude": 5.488560}

parameters = {
    "lat": 51.399930,
    "lng": 5.488560
}

# # sunset_api = f"https://api.sunrise-sunset.org/json?lat={my_address['latitude']}&lng={my_address['longitude']}&date=today"
# sunset_api = "https://api.sunrise-sunset.org/json"
#
# # print(sunset_api)
# # response = requests.get(url=sunset_api)
# response = requests.get(url=sunset_api, params=parameters)
#
# response.raise_for_status()
#
# sunset_data = response.json()
#
# if sunset_data["status"] == "OK":
#     print(f"Sunrise at {sunset_data['results']['sunrise']} and Sunset at {sunset_data['results']['sunset']}")
# else:
#     print("Data is NOT VALID")






