import json
import time

NUM_STORIES = 5

# No extension in filename
def simplify(filename):
    with open(filename + ".json") as json_file:
        trendsDict = json.load(json_file)

    storiesDict = trendsDict["storySummaries"]["trendingStories"]

    file = open(filename + "_simp.json", 'w')
    file.write("{")

    for x in range(NUM_STORIES):
        title = storiesDict[x]["articles"][0]["articleTitle"]
        link = storiesDict[x]["articles"][0]["url"]

        file.write("\"a" + str(x) + "\": {\"title\": \"" + title + "\", \"link\": \"" + link + "\"}")
        if x != NUM_STORIES-1:
            file.write(",")

    file.write("}")

simplify("trends_realtime")
simplify("trends_sports")
