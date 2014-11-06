#!venv/bin/python
import urllib2
from shortenerClass import UrlShortener
from flask import Flask, jsonify
from flask import abort
from flask import make_response
import json
from flask import request
from flask import url_for




app = Flask(__name__,static_url_path='')
short = UrlShortener()

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/<shorturl>', methods=['GET'])
def lookup( shorturl):
	if (short.shortLookup(shorturl)):
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



@app.route('/put', methods=['POST'])
def add():
	siteurl=request.form['url']
	#if(site_exists(siteurl)):
	if(True)
		hashid=short.addUrl('siteurl')
		return json.dumps(hashid)
	else:
		return "Site Does Not Exist"



if __name__ == '__main__':
    app.run(debug=True)
