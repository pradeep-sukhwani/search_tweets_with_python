# Search Twitter tweets by word with Twitter's Streaming API
* It gives the latest tweets. Tweets created from last 5 mins. If no tweets it will simply keep on hit the server and will try to get the new tweet if created recently.
* Output: It's a list: Username, tweet created at, and user's total number of tweets. For Ex: [xyz, Sat Dec 01 11:07:56 +0000 2018, 10]

# Step 1: Requirements.txt
>> Tweepy is a python library which uses streaming API. For more info click [here](http://docs.tweepy.org/en/v3.5.0/)
* tweepy
* pytz
* requests

# Step 2: Setup the twitter's developer account (A very important step)
* Go to twitter's developer's account click [here](https://developer.twitter.com/content/developer-twitter/en.html)
* Create an app
* You will ask couple of things I choose as a learning/studying purpose
* At the end go to app/details/key and tokens
* Here you will get Consumer API key, Consumer API secret key, Access token and Access token secret

# Step 3: Setup your Environment Variables (optional)
* Create environment variables as follows:
* consumer_secret = Consumer API secret key
* consumer_key = Consumer API key
* access_token = Access token
* access_token_secret = Access token secret

# Alternative of step 3:
* In main.py file update values from line number 12 to 15 as per your keys and tokens.

# Step 4: Run the file
* python main.py


# Note:
* There is a known issue for timeout, connection error, ssl. For more info please refer [this](https://github.com/tweepy/tweepy/issues/617)
