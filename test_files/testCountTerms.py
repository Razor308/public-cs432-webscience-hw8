import json
import sys

tweets = open("filteredTweets.json", "r")

data = json.load(tweets)
terms = {}

for tweet in data[0:2]:
    text = tweet["tweetText"]
    splitText = text.split()
    for term in splitText:
        terms[term] = ""

for term in terms:
    appearanceCount = 0
    for tweet in data[0:2]:
        text = tweet["tweetText"]
        splitText = text.split()
        if term in splitText:
            appearanceCount += 1
            terms[term] = appearanceCount

print(terms)
tweets.close()
