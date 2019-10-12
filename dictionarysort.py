#with open('PoliticalDictionary.txt') as f:
    #content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
#content = [x.strip() for x in content]
#content.split(",")
#print(content)

arr = []#declaring an empty array to be used later

with open('PoliticalDictionary.txt', 'r') as myfile:
  data = myfile.read().splitlines()#this puts the dictionary into a string


for x in data:
    x = x.lower()#lowercase every element inside the dictionary
    arr.append(x.split(","))#then split every element into a package of one word and one classification

def classify_tweet(tweet, arr):#function declaration
    tweet = tweet.lower()#lower case the tweet

    Lcount = 0#initiate counters
    Ccount = 0

    for element in arr:#loop through every word of dictionary
        location = tweet.find(element[0])#see if the tweet contatins the word
        if (location != -1):
            if(element[1]=='l'):
                Lcount += 1
            if(element[1]=='c'):
                Ccount += 1
    if(Lcount > Ccount):#return the max of the types of words
        return 'l'
    elif(Ccount > Lcount):
        return 'c'
    elif(Ccount == Lcount):
        return 'n'
