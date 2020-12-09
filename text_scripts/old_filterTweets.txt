import json
import re
import sys

tweets = open("tweets.json", "r")

data = json.load(tweets)
uri = re.compile('http[s]?:\/\/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

for tweet in data[0:2]:
    text = tweet["tweetText"]
    uriMatch = uri.search(text)
    if (uriMatch != None):
        text = text.replace(uriMatch[0], "")
        print(text)

json.dump(data, sys.stdout, indent=2)
tweets.close()
