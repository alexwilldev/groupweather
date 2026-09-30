import urllib.request
import json

# Partners: Alex Williams, Stephen Oliver and Makhari Russom 
# Hometown: Clemmons, NC

latitude = 36.07
longitude = -79.79

url = ("https://api.open-meteo.com/v1/forecast?latitude=" + str(latitude)
       + "&longitude=" + str(longitude)
       + "&hourly=temperature_2m,precipitation_probability"
       + "&temperature_unit=fahrenheit&timezone=America%2FNew_York&forecast_days=2")

response = urllib.request.urlopen(url, timeout=15)
data = json.loads(response.read())

times = data["hourly"]["time"]
temps = data["hourly"]["temperature_2m"]
rain = data["hourly"]["precipitation_probability"]

print(len(times), "hours of forecast")



