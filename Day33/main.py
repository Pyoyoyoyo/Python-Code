# import requests
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# data = response.json()
# response.raise_for_status()
# print(data)
import requests
from datetime import datetime

MY_LAT = 47.263489
MY_LON = -101.778008

parameters = {
    "lat": MY_LAT,
    "lng": MY_LON,
    "formatted": 0,
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
time_now = datetime.now()
print(time_now.hour)

