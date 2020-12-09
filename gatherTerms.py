import json
import sys

tweets = open("filteredTweets.json", "r")

data = json.load(tweets)
accounts = {}

for tweet in data:
    accountName = tweet["username"]
    accounts[accountName] = []
'''
for terms in accounts.values():
    terms.append("test")

print(accounts)

'''
for account in accounts:
    for tweet in data:
        if account == tweet["username"]:
            text = tweet["tweetText"]
            splitText = text.split()
            for word in splitText:
                accounts[account].append(word)
                

json.dump(accounts, sys.stdout, indent=2)
tweets.close()
