import urllib.request
import json

APIKEY = "F62MHL3VDUMCEMGP"

# AlphaVantage API call and parse
url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=INX&interval=1min&apikey=" + APIKEY

data = urllib.request.urlopen(url)

data = json.loads(data.read().decode('utf-8'))

if list(data.keys())[0] == "Note":
    print("Exceeded 5 API calls per minute")
else:
    recent_refresh = data["Meta Data"]["3. Last Refreshed"]
    price = float(data["Time Series (1min)"][recent_refresh]["4. close"])
    file = open("sp500_price.json", 'w')
    file.write("{\"price\": " + str(price) + "}")
