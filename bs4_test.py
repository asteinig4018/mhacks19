import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime

state = "iowa"
page = urllib.request.urlopen("https://www.usclimatedata.com/climate/" + state + "/united-states/")
soup = BeautifulSoup(page, "html.parser")

highs = []
lows = []

for high in soup.find_all("td", {"class": "align_right temperature_red"}):
    highs.append(high.text)

for low in soup.find_all("td", {"class": "align_right temperature_blue"}):
    lows.append(low.text)

print(datetime.now().month)

endOfUrlNum = 3170

for x in range(30):
    endOfUrlNum = endOfUrlNum + 1
    if endOfUrlNum == 3178: endOfUrlNum = endOfUrlNum + 1
    elif endOfUrlNum == 920: endOfUrlNum = 3197
    elif endOfUrlNum == 3196: endOfUrlNum = 919
    elif endOfUrlNum == 1873: endOfUrlNum = 3191
    elif endOfUrlNum == 3190: endOfUrlNum = 1872
    print(endOfUrlNum)
