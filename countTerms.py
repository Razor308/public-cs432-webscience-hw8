import json
import sys

tweetTerms = open("accountsAndTerms.json", "r")

data = json.load(tweetTerms)
wordCount = {}
wordList = {}


for terms in data.values():
    for term in terms:
        wordCount[term] = ""

for term in wordCount:
    count = 0
    for termList in data.values():
        if term in termList:
            count += 1
        else:
            continue
    wordCount[term] = count

for word, accountCount in wordCount.items():
    frac=float(accountCount)/100
    if frac>0.1 and frac<0.5:
        wordList[word] = ""

for word in wordList:
    appearanceCount = 0
    for listOfWords in data.values():
        if word in listOfWords:
            appearanceCount = appearanceCount + listOfWords.count(word)
        else:
            continue
    wordList[word] = appearanceCount

popularWords = sorted(wordList.items(), key=lambda word: word[1], reverse=True)

json.dump(popularWords[0:1000], sys.stdout, indent=2)
#json.dump(wordCount, sys.stdout, indent=2)
tweetTerms.close()
