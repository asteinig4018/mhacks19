import json
import math
from HistoricalTweetDataFetcher import getHistoricalData

joelsarray = getHistoricalData(0)
arrs = []
arrm = []
arrp = []
arrsTotal = 0
arrmTotal = 0
ncount = 0
ccount = 0
lcount = 0
time = joelsarray[0]["h"]
for dictionary in joelsarray:
    arrs.append(dictionary["s"])
    arrm.append(dictionary["m"])
    arrp.append(dictionary["p"])

for x in range(len(arrs)):
    arrsTotal += arrs[x]
    arrmTotal += arrm[x]
    if arrp[x]=='l':
        lcount += 1
    elif arrp[x]=='c':
        ccount += 1
    elif arrp[x]=='n':
        ncount += 1


arrsAvg = arrsTotal/len(arrs)#sentiment value
arrmAvg = arrmTotal/len(arrm)#magnitude value
#print(arrsTotal)
#print(len(arrs))
#rint(arrsAvg)
#print(arrmAvg)
#print(lcount)
#print(ccount)
###################################################################
filename2 = "weather_us.json"

if filename2:
    with open(filename2, 'r') as f:
        weatherstore = json.load(f)

for x in range(50):
    statearray = list(weatherstore.keys())

statesAverage = 0
for state in statearray:
    for x in range(50):
        temptemp = float(weatherstore[state]["temperature"])
        temphigh = float(weatherstore[state]["average_monthly_high"])
        templow = float(weatherstore[state]["average_monthly_low"])

        statesAverage+=((temptemp-temphigh)*(templow-temptemp))/(math.pow(((temphigh+templow)/2),2))


statesAverage = statesAverage/50 #this is the average tempeature multiplyer
print(statesAverage)
#####################################################################################
filename3 = "sp500_price.json"

if filename3:
    with open(filename3, 'r') as f:
        stockdata = json.load(f)

stockpricecurrent = stockdata["current_price"]
stockpricechange = stockdata["percent_change"]#percent change of S&P500
if stockpricechange <= 0.73 and stockpricechange >=-0.73:
    stockmultiply = 0;
else:
    stockmultiply = stockpricechange*0.5*0.73
print(stockpricechange)

#########################################################################################
filename4 = "trump_approval_rating.json"

if filename4:
    with open(filename4, 'r') as f:
        approvalratingdata = json.load(f)

approveAvg = approvalratingdata["approve_avg"]#approval average data
currentApproval = approvalratingdata["approve"]#current approval percentage

########################################################################################


def equation(sentiment, stockmultiply, pollcurrent, pollaverage, avgtemp, lvalue, cvalue, ltweets, ctweet, time, const1 = 70, const2 = 60, const3 = 50, const4 = 45, const5 = 25, slideInput = True):


    point = const1*(sentiment) + const2*(stockmultiply)+const3*((pollcurrent-pollaverage)/(pollaverage))+const4*avgtemp + const5/2*lvalue*ltweets+ const5/2*cvalue+ctweet+const5


    filename5 = "data.json"

    if(slideInput==True):
        if filename5:
            with open(filename5, 'r') as f:
                outputdata = json.load(f)
        print(outputdata)

        outputdata["chartData"]["labels"][0]=outputdata["chartData"]["labels"][1]
        outputdata["chartData"]["labels"][1]=outputdata["chartData"]["labels"][2]
        outputdata["chartData"]["labels"][2]=outputdata["chartData"]["labels"][3]
        outputdata["chartData"]["labels"][3]=outputdata["chartData"]["labels"][4]
        outputdata["chartData"]["labels"][4]=outputdata["chartData"]["labels"][5]
        outputdata["chartData"]["labels"][5]=outputdata["chartData"]["labels"][6]
        outputdata["chartData"]["labels"][6] = str(time)+":00"
        outputdata["chartData"]["thisWeek"][0]=outputdata["chartData"]["thisWeek"][1]
        outputdata["chartData"]["thisWeek"][1]=outputdata["chartData"]["thisWeek"][2]
        outputdata["chartData"]["thisWeek"][2]=outputdata["chartData"]["thisWeek"][3]
        outputdata["chartData"]["thisWeek"][3]=outputdata["chartData"]["thisWeek"][4]
        outputdata["chartData"]["thisWeek"][4]=outputdata["chartData"]["thisWeek"][5]
        outputdata["chartData"]["thisWeek"][5]=outputdata["chartData"]["thisWeek"][6]
        outputdata["chartData"]["thisWeek"][6] = point

        with open(filename5, 'w') as f:
            json.dump(outputdata, f)
    else:
        if filename5:
            with open(filename5, 'r') as f:
                outputdata = json.load(f)
        print(outputdata)

        outputdata["chartData"]["labels"][0]=outputdata["chartData"]["labels"][1]
        outputdata["chartData"]["labels"][1]=outputdata["chartData"]["labels"][2]
        outputdata["chartData"]["labels"][2]=outputdata["chartData"]["labels"][3]
        outputdata["chartData"]["labels"][3]=outputdata["chartData"]["labels"][4]
        outputdata["chartData"]["labels"][4]=outputdata["chartData"]["labels"][5]
        outputdata["chartData"]["labels"][5]=outputdata["chartData"]["labels"][6]
        outputdata["chartData"]["labels"][6] = str(time) + ":00"
        outputdata["chartData"]["thisWeek"][0]=outputdata["chartData"]["thisWeek"][1]
        outputdata["chartData"]["thisWeek"][1]=outputdata["chartData"]["thisWeek"][2]
        outputdata["chartData"]["thisWeek"][2]=outputdata["chartData"]["thisWeek"][3]
        outputdata["chartData"]["thisWeek"][3]=outputdata["chartData"]["thisWeek"][4]
        outputdata["chartData"]["thisWeek"][4]=outputdata["chartData"]["thisWeek"][5]
        outputdata["chartData"]["thisWeek"][5]=outputdata["chartData"]["thisWeek"][6]
        outputdata["chartData"]["thisWeek"][6] = point
        with open(filename5, 'w') as f:
            json.dump(outputdata, f)

    return point


my_list = equation(arrsAvg, stockmultiply, currentApproval, approveAvg, statesAverage, 0, 0, lcount, ccount, 17, 70, 60, 50, 45, 25)
