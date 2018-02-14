#!env/bin/python

#import from local packages
import config

from tweet_logging import TweetLogger


if __name__ == '__main__':
    tl = TweetLogger(
        api_key = config.api_key,
        api_secret = config.api_secret,
        api_token = config.api_token,
        api_token_secret = config.api_token_secret,
        
        db_host = config.db_host,
        db_user = config.db_user,
        db_password = config.db_password,
        db_name = config.db_name,
        
        db_backend = config.db_backend,
        
        log_file_path = config.log_file_path,
        
        verbose = config.verbose,
        stop_on_error = config.stop_on_error  )
    
    tl.start(config.stream_filter)
