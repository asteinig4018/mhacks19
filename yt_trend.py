# importing the requests library
import requests
import json
# api-endpoint
#URL = "https://www.googleapis.com/youtube/v3/videos"
URL = "https://www.googleapis.com/youtube/v3/videos?part=localizations&chart=mostPopular&maxResults=50&key=AIzaSyBs77i9SlqK1n4dX9zu482AtTh92LBmOEg"
# HTTP/1.1
#AIzaSyBs77i9SlqK1n4dX9zu482AtTh92LBmOEg"
#Authorization: Bearer 397250219029-eu1mpur8so3fhcc677k7d0gajqinm71e.apps.googleusercontent.com
#Accept: application/json"


# defining a params dict for the parameters to be sent to the API
PARAMS = {}

# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)

# extracting data in json format
ytdata = r.json()

print(ytdata)

with open('yt_trends_output.json', 'w') as f:
    json.dump(ytdata, f)
