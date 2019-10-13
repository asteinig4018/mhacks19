import json

NUM_STORIES = 5

def simplify(filename):
    with open(filename) as json_file:
        trendsDict = json.load(json_file)

    storiesDict = trendsDict["storySummaries"]["trendingStories"]

    file = open(filename, 'w')
    file.write("{")

    for x in range(NUM_STORIES):
        title = storiesDict[x]["articles"][0]["articleTitle"]
        link = storiesDict[x]["articles"][0]["url"]

        file.write("\"" + str(x) + "\": {\"title\": \"" + title + "\", \"link\": \"" + link + "\"}")
        if x != NUM_STORIES-1:
            file.write(",")

    file.write("}")

simplify("trends_realtime.json")
simplify("trends_sports.json")
