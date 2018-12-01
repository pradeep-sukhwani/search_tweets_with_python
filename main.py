# source: http://adilmoujahid.com/posts/2014/07/twitter-analytics/

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from datetime import datetime, timedelta
import json
import httplib
import urlparse
import os

consumer_key = os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret")
access_token = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")


class ListenerStream(StreamListener):
    def __init__(self):
        self.tweet_data = {}
        self.start_time = datetime.today().replace(microsecond=0, second=0) # calculating tweet start from here

    def on_data(self, data):
        print "Searching tweets..."
        data = json.loads(data) # str to dictionary
        created_date = datetime.strptime(data['created_at'], '%a %b %d %H:%M:%S +0000 %Y') # tweet create date time object
        if created_date >= self.start_time - timedelta(minutes=5): # tweet create date time checking if there are tweets in >= from last 5 mins based on current date time
            current_data = [data["user"]["name"], data['created_at'], data["user"]["statuses_count"]]
            if created_date <= (self.start_time - timedelta(minutes=1)): # check - tweet create date <= last one min from start time
                if self.tweet_data.get('one_min'):
                    self.tweet_data.get('one_min').append(current_data)
                else:
                    self.tweet_data.update({'one_min': current_data})
            if created_date > self.start_time - timedelta(minutes=1) <= self.start_time  - timedelta(minutes=2): # check - tweet create date > 3 mins but <= last 2 mins start time
                if self.tweet_data.get('two_min'):
                    self.tweet_data.get('two_min').append(current_data)
                else:
                    self.tweet_data.update({'two_min': current_data})
            if created_date > self.start_time - timedelta(minutes=2) <= self.start_time  - timedelta(minutes=3): # check - tweet create date > 3 mins but <= last 3 mins start time
                if self.tweet_data.get('three_min'):
                    self.tweet_data.get('three_min').append(current_data)
                else:
                    self.tweet_data.update({'three_min': current_data})
            if created_date > self.start_time - timedelta(minutes=3) <= self.start_time  - timedelta(minutes=4): # check - tweet create date > 3 mins but <= last 4 mins start time
                if self.tweet_data.get('four_min'):
                    self.tweet_data.get('four_min').append(current_data)
                else:
                    self.tweet_data.update({'four_min': current_data})
            if created_date > self.start_time - timedelta(minutes=4) <= self.start_time  - timedelta(minutes=5): # check - tweet create date > 4 mins but <= last 5 mins from start time
                if self.tweet_data.get('five_min'):
                    self.tweet_data.get('five_min').append(current_data)
                else:
                    self.tweet_data.update({'five_min': current_data})
        current_time = datetime.today().replace(microsecond=0, second=0) # need current (real) time to compare with 1, 2, 3, 4, 5 mins
        if current_time == self.start_time + timedelta(minutes=1):
            print self.tweet_data.get('one_min')
        if current_time == self.start_time + timedelta(minutes=2):
            print self.tweet_data.get('two_min')
        if current_time == self.start_time + timedelta(minutes=3):
            print self.tweet_data.get('three_min')
        if current_time == self.start_time + timedelta(minutes=4):
            print self.tweet_data.get('four_min')
        if current_time >= self.start_time + timedelta(minutes=5):
            print self.tweet_data.get('five_min')
            self.start_time = datetime.today().replace(microsecond=0, second=0) # after five mins reseting the time to now.
        return True

    def on_error(self, status):
        print status


def user_input():
    user_input = raw_input("Enter the keyword that you want to search with:\nFORMAT: `python` if multiple: `python,django` - without quotes:\n>> ")
    return user_input.split(",")

def main():
    l = ListenerStream()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=user_input())

if __name__ == '__main__':
    main()
