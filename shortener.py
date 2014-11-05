from bottle import route, run 
import urllib2
from shortenerClass import UrlShortener

app = Bottle()
short = UrlShortener()

@app.route('/')
def index():
    return "Hello"

@app.route('/<shorturl>', method='GET')
def lookup( shorturl):
	if (shortlookup(shorturl)!=NONE ):
		result = "exists"
	else:
		result = "no"
	return result
     


def site_exists(url):
	try:
		urllib2.urlopen(url)
		return True
	except urllib2.HTTPError, e:
		return False
	except urllib2.URLError, e:
		return False



@app.route('/put/', method='POST')
def add():
	siteurl=request.forms.get('url')
	if(site_exists(siteurl)):
		short.addUrl('siteurl')
		return "Success"
	else:
		return "Site Does Not Exist"




if __name__ == "__main__":
    run(host='localhost', port=8080)


app = bottle.default_app()