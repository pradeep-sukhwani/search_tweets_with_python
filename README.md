# Search Twitter tweets with Twitter's Streaming API

# Step 1: Requirements.txt
>> Tweepy is a python library which uses streaming API. For more info click [here](http://docs.tweepy.org/en/v3.5.0/)
* pip install tweepy

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
* In main.py file update values of line number from 12 to 15 as per your key and tokens.

# Step 4: Run the file
* python main.py
