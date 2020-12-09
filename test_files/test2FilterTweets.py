import json
import re
import sys

tweets = open("tweets.json", "r")

data = json.load(tweets)
uris = re.compile('http[s]?:\/\/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
accountNames = re.compile('[@]+[A-Za-z0-9-_]+')

tweet_data = []

for tweet in data[2:4]:
    tweet_dict = {}
    tweet_dict["username"] = tweet["username"]
    tweet_dict["tweetId"] = tweet["tweetId"]
    text = tweet["tweetText"]
    uriMatches = re.findall(uris, text)
    accountNameMatches = re.findall(accountNames, text)
    if (uriMatches != None):
        for uri in uriMatches:
            text = text.replace(uri, "")
    if (accountNameMatches != None):
        for accountName in accountNameMatches:
            text = text.replace(accountName, "")
    tweet_dict["tweetText"] = text
    tweet_data.append(tweet_dict)

json.dump(tweet_data, sys.stdout, indent=2)
tweets.close()
