from hashids import Hashids
import Redis
import random
import config
import time

class UrlShortener:
    def __init__(self):
        self.redis = redis.StrictRedis(host=config.REDIS_HOST,
                                       port=config.REDIS_PORT,
                                       db=config.REDIS_DB)
        
        self.dict={}

    def shortcode(self, url):
		
		hashids = Hashids(min_length=5)
        randomno= self.randomuniquegenerator()
		hashid = hashids.encrypt(randomno)
        return hashid

    def randomuniquegenerator():
        tm=(time.time()/10000)
        random=random.randrange(100000,99999)
        if random > tm:
            return random - tm
        else:
            return tm -random

    def shorten(self, url):
        hashid = self.shortcode(url)
        
        try:
            self.dict['url']=url
            self.dict['']
            self.redis.hmset(hashid,)
            self.redis.hmset(config.REDIS_PREFIX + code, url)
            return {'success': True,
                    'url': url,
                    'code': code,
                    'shorturl': config.URL_PREFIX + code}
        except:
            return {'success': False}

    def lookup(self, code):
        """
        The same strategy is used for the lookup than for the
        shortening. Here a None reply will imply either an
        error or a wrong code.
        """
        try:
            return self.redis.get(config.REDIS_PREFIX + code)
        except:
            return None


