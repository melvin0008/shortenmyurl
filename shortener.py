#!venv/bin/python
from shortenerClass import UrlShortener
from flask import Flask, redirect
import urlparse
from flask import render_template
from flask import request


#from config import Heroku


app = Flask(__name__)
# heroku=Heroku(app)
# heroku.init_app(app)

myurl = "http://www.minurl.in/"
# myurl="127.0.0.1:5000/"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<shorturl>', methods=['GET'])
def lookup(shorturl):
    short = UrlShortener()
    url = short.shortLookup(shorturl)
    if url:
        result = redirect(url)
    else:
        result = "DatabaseConnection Limit Reached .\
        Have To Update Your RedisToCloud Pack"
    return result

if __name__ == '__main__':
        app.run(debug=True)
