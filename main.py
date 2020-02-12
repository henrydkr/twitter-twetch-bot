from __future__ import absolute_import, print_function
import tweepy
import os
from tweepy import OAuthHandler, Stream, StreamListener


#runs twetch cli , make sure you have set up
def twetch(data):
    text= ' "'+data+'"'

    
    my_cmd='twetch post --content'+text

    
    os.system(my_cmd)
    print(my_cmd)#just checking



# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="l15bTjR7RMGbl8mLDt9qFWP7k"
consumer_secret="WwCtEI2Y9tZOUgxNWL3mk4Yx8TZmdigrVFM5qGio9XaqdxEGHX"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="226707500-eidOyVv6klvDCscBQFlhqFZqmvRWoJYb9RwAMBoC"#trumpbot
access_token_secret="vk3m8Rlz0CeLrdfPsKJpAjUgAUa4UkIxsy7EjuFI8wZeJ"

 
 
    



class MyStreamListener(tweepy.StreamListener):
    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening

    
    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening

    def on_status(self, status):
        if (status.user.screen_name=='realDonaldTrump'):
            
            
            if hasattr(status, 'retweeted_status'):
                try:
                    twetch(status.retweeted_status.extended_tweet["full_text"])
                except AttributeError:
                    twetch(status.retweeted_status.text)
            else:
                try:
                    twetch(status.extended_tweet["full_text"])
                except AttributeError:
                    twetch(status.text)
        return True
       
if __name__ == '__main__':
    a = MyStreamListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, a)
    stream.filter(follow=['25073877'])#trump user id




