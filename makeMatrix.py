import json
import sys
import csv

accountsAndWords = open("accountsAndPopularTerms.json", "r")
words = open("1000popularWords.json", "r")

accountsPopularWords = json.load(accountsAndWords)
popularWords = json.load(words)
headers = ["Blog"]

for word in popularWords:
    headers.append(word[0])
'''
for account, terms in accountsPopularWords.items():
    row = []
    row.append(account)
    for term in terms:
        row.append(term[1])
'''
with open("accountTermMatrix.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    for account, terms in accountsPopularWords.items():
        row = []
        row.append(account)
        for term in terms:
            row.append(term[1])
        writer.writerow(row)

#json.dump(accountsPopularWords, sys.stdout, indent=2)
accountsAndWords.close()
words.close()
