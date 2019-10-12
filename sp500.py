import urllib.request
import json

APIKEY = "F62MHL3VDUMCEMGP"

url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=INX&apikey=" + APIKEY
data = urllib.request.urlopen(url)
data = json.loads(data.read().decode('utf-8'))

if list(data.keys())[0] == "Note":
    print("Exceeded 5 API calls per minute")
else:
    recent_refresh = data["Meta Data"]["3. Last Refreshed"]
    current_price = float(data["Time Series (Daily)"][recent_refresh]["4. close"])
    dates = list(data["Time Series (Daily)"].keys())
    yesterday_price = float(data["Time Series (Daily)"][dates[1]]["4. close"])
    file = open("sp500_price.json", 'w')
    file.write("{\"current_price\": " + str(current_price) + ", \"yesterday_price\": " + str(yesterday_price) + ", ")
    file.write("\"percent_change\": " + str(100*(current_price-yesterday_price)/yesterday_price) + "}")
