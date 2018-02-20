#!env/bin/python

from sys import stderr
from traceback import format_exc

# local imports
from .db_connection import DBConnection


class TweetHandler:
    
    def __init__(self, **config):
        """
        all config options are described in the config module.
        most relevant are: db backend to use, 
        credentials to access db, log file path.
        -----------------------------------------------------
        Connect with db
        """
        self._dbcon = DBConnection.new(**config)
        self._verbose = config["verbose"]
        self._stop_on_error = config["stop_on_error"]
        self._log_file_path = config["log_file_path"]
    
    
    ###########################
    # public instance methods #
    ###########################
    def handle_tweet(self, tweet):
        """
        insert tweet data into db, 
        if self._verbose = Trueprint tweet,
        log any error to self._log_file
        """
        id = tweet.get_id()
        user_id = tweet.get_user_id()
        lang = tweet.get_lang()
        text = tweet.get_text()
        hashtag_set = tweet.get_hashtag_set()
        in_reply_id = tweet.get_in_reply_id()
        retweet_id = tweet.get_retweet_id()
        if self._verbose:
            # print tweet
            self._print_tweet(tweet)
        try:
            # insert data into db
            data = (id, user_id, lang, text, in_reply_id, retweet_id)
            self._dbcon.update(self._insert_tweet_sql, data)
            for hashtag in hashtag_set:
                data = (id, hashtag)
                self._dbcon.update(self._insert_hashtag_sql, data)
        except Exception as exc:
            # on error: write error into log_file and stderr
            error_msg = "ERROR occurred on Tweet id: %d" %(id)
            self._log_error(error_msg, exc)
            if self._stop_on_error:
                raise exc
    
    def handle_connection_error(self, errno):
        """
        @errno: int
        --------------
        print errno to stderr and 
        log it to self._log_file_path.
        """
        error_msg = "ERROR %s occurred during connection" %(errno)
        self._log_error(msg)
    
    
    ############################
    # private static variables #
    ############################
    _insert_tweet_sql = """
    INSERT INTO tweet (id, user_id, lang, text, in_reply_id, retweet_id) 
    VALUES 
    (%s, %s, %s, %s, %s, %s)
    """
    
    _insert_hashtag_sql = """
    insert into hashtag_tweet (tweet_id, hashtag_text) 
    values 
    (%s, %s) 
    """
    
    
    ##########################
    # private static methods #
    ##########################
    @staticmethod
    def _print_tweet(tweet):
        print("id: ")
        print(tweet.get_id())
        print("user_id: ")
        print(tweet.get_user_id())
        print("lang: ")
        print(tweet.get_lang())
        print("text: ")
        print(tweet.get_text())
        print("hashtags: ")
        print(tweet.get_hashtag_set())
        print("in_reply_id: ")
        print(tweet.get_in_reply_id())
        print("retweet_id: ")
        print(tweet.get_retweet_id())
        print("###########################################")
        
        
    ############################
    # private instance methods #
    ############################
    def _log_error(self, msg, traceback=False):
        # write error on stderr
        print(msg, end="\n", file=stderr)
        if traceback:
            stacktrace_str = format_exc()
            print(stacktrace_str, end="\n", file=stderr)
        try:
            # write error on log_file
            log_file = open(self._log_file_path, "a")
            print(msg, end="\n", file=log_file_path)
            if traceback:
                stacktrace_str = format_exc()
                print(stacktrace_str, end="\n", file=self._log_file_path)
            log_file.close()
        except Exception:
            error_msg = "WARNING: can not write error on log_file"
            print(error_msg, end="\n", file=stderr)
        
        
        
        
        
