import tweepy
import json
import sys

auth = tweepy.OAuthHandler("TLJQi8hQ0E7UjEoqd2zu5Of1v", "b2qwnhOl0bYmQm3ebgtuJP8qIWMeMOcVOEPqflN5ipjHG7PEgg")
auth.set_access_token("895646075670986753-0V8x7OjnoLl91JXApMewvl7nGGZjPfQ", "zzZkM4OMOGgRknvI6vCAhNlp8AZG0IGAqlw6n9CfsPxJY")

api = tweepy.API(auth, wait_on_rate_limit=True)

tweet_data = []
tweets = api.user_timeline(screen_name="NewYorker", count=200, include_rts=False, exclude_replies=True)

for tweet in tweets:
    tweet_dict = {}
    tweet_dict["username"] = tweet.user.screen_name
    tweet_dict["tweetId"] = tweet.id_str
    tweet_dict["tweetText"] = tweet.text
    tweet_data.append(tweet_dict)

json.dump(tweet_data, sys.stdout, indent=2)
