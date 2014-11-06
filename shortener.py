#!venv/bin/python
import urllib2
from shortenerClass import UrlShortener
from flask import Flask, jsonify ,redirect
from flask import abort
from flask import make_response
import json
from flask import request
from flask import url_for

#from config import Heroku


app = Flask(__name__,static_url_path='')
#heroku=Heroku(app)
#heroku.init_app(app)
short = UrlShortener()
myurl="https://shortenmyurl.herokuapp.com/"
#myurl="127.0.0.1:5000/"

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/<shorturl>', methods=['GET'])
def lookup( shorturl):
	url=short.shortLookup(shorturl)
	if (url):
		result=redirect(url[0])
	else:
		result = "no"
	return result
     


"""def site_exists(url):
	try:
		urllib2.urlopen(url)
		return True
	except urllib2.HTTPError, e:
		return False
	except urllib2.URLError, e:
		return False
"""


@app.route('/put', methods=['POST'])
def add():
	siteurl=request.form['url']
	u = urlparse.urlparse(siteurl)
	if u.netloc == '':
		url = 'http://' + siteurl
	else:
		url = siteurl
	
	if(True):
		hashid=short.addUrl('siteurl')
		return "Visit : "+"<a href='"+hashid+"'>"+myurl+hashid+"</a>" + " for the short url"
	else:
		return "Site Does Not Exist"


if __name__ == '__main__':
	app.run(debug=True)
