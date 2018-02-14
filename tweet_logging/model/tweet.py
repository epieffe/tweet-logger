#!env/bin/python

class Tweet:
    def __init__ (self, id, user_id, lang, text, hashtag_set, in_reply_id=None, retweet_id=None):
        self.id = id
        self.user_id = user_id
        self.lang = lang
        self.text = text
        self.hashtag_set = hashtag_set
        self.in_reply_id = in_reply_id
        self.retweet_id = retweet_id
        
    def get_id(self):
        return self.id
        
    def get_user_id(self):
        return self.user_id
        
    def get_lang(self):
        return self.lang
    
    def get_text(self):
        return self.text
            
    def get_hashtag_set(self):
        return self.hashtag_set
        
    def get_in_reply_id(self):
        return self.in_reply_id
    
    def get_retweet_id(self):
        return self.retweet_id
    
    def is_retweet(self):
        return self.retweet_id != None
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
