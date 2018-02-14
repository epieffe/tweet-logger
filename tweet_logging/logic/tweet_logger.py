from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener

# local imports
from .tweet_handler import TweetHandler

from ..model import Tweet

class TweetLogger():
    
    def __init__(self, **config):
        """
        all config options are described in the config module.
        Most relevant are: credentials to access Twitter API, 
        db backend to use, credentials to access db.
        --------------------------------------------
        Connect to Twitter API and db
        """
        # create StreamListener
        self._sl = _MyStreamListener(**config)
        # authenticate to Twitter API
        self._auth = OAuthHandler(
            config["api_key"], 
            config["api_secret"] )
        self._auth.set_access_token(
            config["api_token"], 
            config["api_token_secret"] )
        # create Stream
        self._stream = Stream(
            auth = self._auth, 
            listener = self._sl, 
            tweet_mode = "extended" )
    
    
    def start(self, filter):
        """
        @filter: list of str
        ---------------------
        stream from Twitter API all the tweets matching the keywords 
        in filter in real time, saving tweets data on db as they arrive.
        This method is blocking and never returning. 
        The only way to stop is with KeyboardInterrupt!
        """
        self._stream.filter(track = filter)
        
        
class _MyStreamListener(StreamListener):
    """
    Helper class of Stream handler.
    Implements tweepy.streaming.StreamListener interface
    """
    def __init__(self, **config):
        super().__init__()
        self.th = TweetHandler(**config)
    
    def on_status(self, status):
        tweet = self._get_tweet_from_status(status)
        self.th.handle_tweet(tweet)
        return True

    def on_error(self, status_code):
        return self.th.handle_connection_error(status_code)
        
    @staticmethod
    def _get_tweet_from_status(status):
        """
        Build Tweet object from tweepy.Status object
        """
        # get id
        id = status.id
        # get user_id
        user_id = int( status.user.id_str )
        # get lang
        lang = status.lang
        # get retweet_id (if any)
        retweet_id = None
        if 'retweeted_status' in dir(status):
            status = status.retweeted_status
            retweet_id = status.id
        # get in_reply_id (if any)
        in_reply_id = status.in_reply_to_status_id
        # get text
        text = status.extended_tweet['full_text'] \
                   if 'extended_tweet' in dir(status) \
                   else status.text
        # get hashtags                
        hashtags = status.extended_tweet['entities']['hashtags'] \
                   if 'extended_tweet' in dir(status) \
                   else status.entities['hashtags']
        hashtag_set = set([ht["text"].lower() for ht in hashtags])
        # return Tweet
        return Tweet(
            id, 
            user_id, 
            lang, 
            text, 
            hashtag_set, 
            in_reply_id, 
            retweet_id  )

            
           

