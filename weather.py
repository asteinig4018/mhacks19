import urllib.request
import json
from bs4 import BeautifulSoup
from datetime import datetime

APIKEY = "5299a0c2aaaf8d5780f8c15ca5c1af32"

with open("USstates_avg_latLong.json") as json_file:
    states = json.load(json_file)

file = open("weather_us.json", 'w')
file.write("{")

endOfUrlNum = 3170 # number at end of usclimatedate.com URL that increments

for x in range(50):
    lat = str(states[x]["latitude"])
    lon = str(states[x]["longitude"])
    url = "https://api.darksky.net/forecast/" + APIKEY + "/" + lat + "," + lon + "?exclude=minutely,hourly,daily,alerts,flags"
    weather_data = urllib.request.urlopen(url)
    weather_data = json.loads(weather_data.read().decode('utf-8'))
    weather_data = weather_data["currently"]
    state = states[x]["state"]

    file.write("\"" + states[x]["state"] + "\": {")

    for y in range(len(weather_data)):
        currentData = list(weather_data.keys())[y]
        file.write("\"" + currentData + "\": \"" + str(weather_data[currentData]) + "\", ")

    # Get averages from usclimatedata.com
    state = state.replace(" ", "-")
    print(state + " " + str(endOfUrlNum))
    page = urllib.request.urlopen("https://www.usclimatedata.com/climate/" + state + "/united-states/" + str(endOfUrlNum))
    soup = BeautifulSoup(page, "html.parser")
    highs = []
    lows = []
    for high in soup.find_all("td", {"class": "align_right temperature_red"}):
        highs.append(high.text)
    for low in soup.find_all("td", {"class": "align_right temperature_blue"}):
        lows.append(low.text)

    file.write("\"average_monthly_high\": \"" + str(highs[datetime.now().month-1]) + "\", ")
    file.write("\"average_monthly_low\": \"" + str(lows[datetime.now().month-1] + "\""))

    file.write("}")
    if x < 49:
        file.write(", ")

    endOfUrlNum = endOfUrlNum + 1
    if endOfUrlNum == 3178: # Ignore District of Columbia
        endOfUrlNum = endOfUrlNum + 1
    elif endOfUrlNum == 3190: # Fix bullshit fucking inconsistencies on usclimatedata.com
        endOfUrlNum = 1872
    elif endOfUrlNum == 1873:
        endOfUrlNum = 3191
    elif endOfUrlNum == 3196:
        endOfUrlNum = 919
    elif endOfUrlNum == 920:
        endOfUrlNum = 3197

file.write("}")
