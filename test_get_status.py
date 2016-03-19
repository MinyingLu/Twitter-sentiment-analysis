#!/usr/bin/python
# -*- coding: <utf-8> -*-
import oauth2
from twython import Twython

#url = "https://api.twitter.com/1.1/statuses/show.json?id=1464599533"
#key =  "48r56upQvsnTiSDfY4CNwIpCQ"
#secret =  "VqZhFW7GqogdKXJnpuS0umVe211bFgoCdaQlRdRMayvrbdDh3k"
#token = "18000528-Scl8a1pLinqP4KWtaa3f8EN0M1vqAGTyYXMtsLIGm"
#token_secret = "NcIvLeqVbwwBegabvo7946FVIaDN0CAaJ7aS2aV7pZFzC"

#    consumer = oauth2.Consumer(key, secret)
#    token = oauth2.Token(key=key, secret=secret)
#    client = oauth2.Client(consumer, token)
#    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
#    return content
#
#single_status = oauth_req(url, key, secret)
CONSUMER_KEY = "48r56upQvsnTiSDfY4CNwIpCQ"
CONSUMER_SECRET = "VqZhFW7GqogdKXJnpuS0umVe211bFgoCdaQlRdRMayvrbdDh3k"
OAUTH_TOKEN = "18000528-Scl8a1pLinqP4KWtaa3f8EN0M1vqAGTyYXMtsLIGm"
OAUTH_TOKEN_SECRET = "NcIvLeqVbwwBegabvo7946FVIaDN0CAaJ7aS2aV7pZFzC"

twitter = Twython(
    CONSUMER_KEY, CONSUMER_SECRET,
    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

tweet = twitter.show_status(id=524349343353294848)
print tweet

#auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
#api = tweepy.API(auth)
#
#tweet = api.get_status(id_of_tweet)
#print(tweet.text)
