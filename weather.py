import urllib.request
import json

# Partners: Alex Williams, Stephen Oliver and Makhari Russom 
# Hometown: Anchorage, AK

latitude = 61.2181
longitude = -149.9003

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

counter = 0
while counter <= (len(times)-1):
    print(f"{times[counter]} {temps[counter]} F")
    counter = counter + 1
#     print(counter) # used to check incrementing in terminal

# counter2 = 0
# while counter2 <= (len(times)):
#     print(counter2)
#     counter2 = counter2 + 1
# check total number of values
#

#Task 2


desired = float(input("Enter a temperature to check for: "))

count_at_or_above = 0

counter = 0
while counter < len(temps):
    if temps[counter] >= desired:
        count_at_or_above += 1
    counter += 1

print(f"{count_at_or_above} hours at or above {desired} F")
