import tweepy
import json
import sys

auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")

api = tweepy.API(auth, wait_on_rate_limit=True)

screenNames = open("100screen_names.txt", "r")

tweet_data = []

for screenName in screenNames:
    try:
        noNewlineName = screenName.replace('\n', '')
        tweets = api.user_timeline(screen_name=noNewlineName, count=200, include_rts=False, exclude_replies=True, lang="en", tweet_mode="extended") 
        for tweet in tweets:
            tweet_dict = {}
            tweet_dict["username"] = tweet.user.screen_name
            tweet_dict["tweetId"] = tweet.id_str
            tweet_dict["tweetText"] = tweet.full_text
            tweet_data.append(tweet_dict)
    except:
        continue

json.dump(tweet_data, sys.stdout, indent=2)
screenNames.close()
