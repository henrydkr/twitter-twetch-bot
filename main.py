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
consumer_key=""
consumer_secret=""

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token=""
access_token_secret=""

 
 
    



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
                    twetch(status.text)
                except AttributeError:
                    twetch(status.text)
            else:
                try:
                    twetch(status.text)#redundant, was trying to fuck w truncated but due to 256 on twetch its thiz
                except AttributeError:
                    twetch(status.text)
        return True
       
if __name__ == '__main__':
    a = MyStreamListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, a)
    stream.filter(follow=[''])#user id











