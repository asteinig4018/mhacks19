import json

def getHistoricalData(nHoursAgo):
    currentFileNumber = 0

    with open('TweetDataIndex.txt', 'r') as myfile:
        currentFileNumber = int(myfile.read())

    currentFileNumber -= nHoursAgo
    if (currentFileNumber < 1): currentFileNumber += 8

    with open('AllTweetData' + str(currentFileNumber) + '.json', 'r') as myfile:
        data = myfile.read()#.splitlines()#this puts the dictionary into a string
        return json.loads(data) # results in a mega array