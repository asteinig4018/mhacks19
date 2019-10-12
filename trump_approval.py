import urllib.request
import json
from datetime import date

today = date.today().strftime("%Y-%m-%d")

url = "https://projects.fivethirtyeight.com/trump-approval-ratings/approval.json"
data = urllib.request.urlopen(url)
data = json.loads(data.read().decode('utf-8'))

for dict in data:
    if dict["date"] == today:
        if dict["subgroup"] == "All polls":
            file = open("trump_approval_rating.json", 'w')
            file.write("{\"approve\": " + str(dict["approve_estimate"]) + ", " + "\"disapprove\": " + str(dict["disapprove_estimate"]) + "}")
