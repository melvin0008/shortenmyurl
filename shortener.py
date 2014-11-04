from hashids import Hashids
import Redis
import random


class UrlShortener:
    def __init__(self):
        self.redis = redis.StrictRedis(host=config.REDIS_HOST,
                                       port=config.REDIS_PORT,
                                       db=config.REDIS_DB)
        self.dict={}
        
    def shortcode(self, url):
		randomno=random.randint(100,99999)
		hashids = Hashids()
		hashid = hashids.encrypt(randomno)
		self.dict[randomno]=url
		redis.set(hashid,dict)
        return 

    def shorten(self, url):
        """
        The shortening workflow is very minimal. We try to
        set the redis key to the url value. We catch any
        exception in the process to properly report failures
        in the client
        """

        code = self.shortcode(url)
        
        try:
            self.redis.set(config.REDIS_PREFIX + code, url)
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


