import urllib.request
import json

# Partners: Alex Williams, Stephen Oliver and Makhari Russom 
# Hometown: Anchorage, AK, also task 5

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

# task 1 (lines per hour)
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

#Task 2 (hours above an hour)


desired = float(input("Enter a temperature to check for: "))

count_at_or_above = 0

counter = 0
while counter < len(temps):
    if temps[counter] >= desired:
        count_at_or_above += 1
    counter += 1

print(f"{count_at_or_above} hours at or above {desired} F")

# task 3 (hottest hour)
hottest_temp = temps[0]
hottest_index = 0

counter = 0
while counter < len(temps):
       if temps[counter] > hottest_temp:
              hottest_temp = temps[counter]
              hottest_index = counter
       counter += 1
print(f'Hottest hour: {times[hottest_index]} at {hottest_temp} F')

       

# task 4 (first chance of rain)
increment = 0
while increment < len(rain):
    if rain[increment] >= 50:
        print(f"First rain chance: {times[increment]} ({rain[increment]}%)")
        break
    increment += 1
else:
    print("No rain likely today or tomorrow.")

