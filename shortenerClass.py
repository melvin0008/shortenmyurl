from hashids import Hashids
import redis
import random
import config
import time
from flask import request
import urlparse
import math

class UrlShortener:
    def __init__(self):
        self.redis = redis.StrictRedis(host=config.REDIS_HOST,
                                       port=config.REDIS_PORT,
                                       db=config.REDIS_DB)
        
        self.dict={}

    def shortcode(self, url):
        hashids = Hashids(min_length=5)
        randomno = self.randomuniquegenerator()
        hashid = hashids.encrypt(randomno)
        return hashid

    def randomuniquegenerator(self):
        tm=int (math.floor(time.time()/10000))
        randomno=random.randrange(100000,999999)
        if randomno > tm:
            return randomno - tm
        else:
            return tm -randomno


    def addUrl(self, url):
        u = urlparse.urlparse(request.form['url'])
        if u.netloc == '':
            url = 'http://' + request.form['url']
        else:
            url = request.form['url']
        hashid = self.shortcode(url)
        
        self.dict['url']=url
        self.dict['hits']=0;
        if(not self.redis.exists(hashid)):
            self.redis.hmset(hashid,self.dict)
            return {'success': True,
                    'url': url,
                    'shorturl': hashid}
        else:
            return self.addUrl(url)

    def shortLookup(self, hashid):
        try:
            return self.redis.hvals(hashid)
        except:
            return None


