import json
import re
import sys

tweets = open("tweets.json", "r")

data = json.load(tweets)
uris = re.compile('http[s]?:\/\/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
accountNames = re.compile('[@]+[A-Za-z0-9-_]+')
punctuation = re.compile('[^\w\s]')
smallTerms = re.compile(r'\W*\b\w{1,3}\b')
largeTerms = re.compile(r'\W*\b\w{15,}\b')

tweet_data = []

for tweet in data:
    tweet_dict = {}
    tweet_dict["username"] = tweet["username"]
    tweet_dict["tweetId"] = tweet["tweetId"]

    text = tweet["tweetText"]
    text = re.sub(uris, "", text)
    text = re.sub(accountNames, "", text)
    text = text.lower()
    
    splitText = text.split()

    for word in splitText:
        if any(ord(char) >= 128 for char in word):
            splitText.remove(word)
        else:
            pass

    joinedText = " ".join(splitText)
    joinedText = re.sub(punctuation, "", joinedText)
    joinedText = re.sub(smallTerms, "", joinedText)
    joinedText = re.sub(largeTerms, "", joinedText)
    
    tweet_dict["tweetText"] = joinedText
    tweet_data.append(tweet_dict)

json.dump(tweet_data, sys.stdout, indent=2)
tweets.close()
