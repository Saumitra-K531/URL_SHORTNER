#!/usr/bin/env python3
from flask import Flask
from flask import request
from shorten_url import URL_shortner
from redis_cache import RedisCache
import re

app = Flask(__name__)

@app.route('/', methods=['POST'])
def url_shortener_api():
    input_url = request.args.get('input_url')
    print(type(input_url))
    valid_url_regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")
    compile_regex = re.compile(valid_url_regex)
    
    # Check if valid URL
    if re.match(compile_regex, input_url):
        RedisObj = RedisCache(input_url)
        shortened_url = RedisObj.search_cache()
        return shortened_url
    else:
        return "Please enter valid URL !\n"

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)