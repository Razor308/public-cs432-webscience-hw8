import json
import sys

accountsAllTerms = open("accountsAndTerms.json", "r")
popularTerms = open("1000popularWords.json", "r")

accounts = json.load(accountsAllTerms)
terms = json.load(popularTerms)

accountsPopularWords = {}

def getWordCount(accountName, term):
    wordAndCount = (term, accounts[accountName].count(term))
    return wordAndCount

for account in accounts:
    accountsPopularWords[account] = []


for account in accountsPopularWords:
    for term in terms:
        wordWithCount = getWordCount(account, term[0])
        accountsPopularWords[account].append(wordWithCount)


json.dump(accountsPopularWords, sys.stdout, indent=2)
accountsAllTerms.close()
popularTerms.close()
