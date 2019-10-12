import urllib.request
import json

APIKEY = "5299a0c2aaaf8d5780f8c15ca5c1af32"

with open("USstates_avg_latLong.json") as json_file:
    states = json.load(json_file)

file = open("weather_us.json", 'w')
file.write("{")

for x in range(50):
    lat = str(states[x]["latitude"])
    lon = str(states[x]["longitude"])
    url = "https://api.darksky.net/forecast/" + APIKEY + "/" + lat + "," + lon + "?exclude=minutely,hourly,daily,alerts,flags"
    weather_data = urllib.request.urlopen(url)
    weather_data = json.loads(weather_data.read().decode('utf-8'))
    weather_data = weather_data["currently"]

    file.write("\"" + states[x]["state"] + "\": {")

    for y in range(len(weather_data)):
        currentData = list(weather_data.keys())[y]
        file.write("\"" + currentData + "\": \"" + str(weather_data[currentData]) + "\"")
        if y < len(weather_data) - 1:
            file.write(",")

    file.write("}")
    if x < 49:
        file.write(", ")

file.write("}")
