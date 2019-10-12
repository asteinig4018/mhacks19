import urllib.request
import json
from datetime import date

today = date.today().strftime("%Y-%m-%d")

url = "https://projects.fivethirtyeight.com/trump-approval-ratings/approval.json"
data = urllib.request.urlopen(url)
data = json.loads(data.read().decode('utf-8'))

approve_sum = 0
disapprove_sum = 0
count = 0

for dict in data:
    if dict["subgroup"] == "All polls":
        approve_sum = approve_sum + float(dict["approve_estimate"])
        disapprove_sum = disapprove_sum + float(dict["disapprove_estimate"])
        count = count + 1

        if dict["date"] == today:
            approve_avg = approve_sum / count
            disapprove_avg = disapprove_sum / count
            file = open("trump_approval_rating.json", 'w')
            file.write("{\"approve_avg\": " + str(approve_avg) + ", " + "\"disapprove_avg\": " + str(disapprove_avg) + ", ")
            file.write("\"approve\": " + str(dict["approve_estimate"]) + ", " + "\"disapprove\": " + str(dict["disapprove_estimate"]) + "}")
            break
