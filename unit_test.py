#!/usr/bin/env python3
# Note: Make sure redis server is started before performing unit tests
import redis
from shorten_url import URL_shortner
from redis_cache import RedisCache

# Test base62 conversion
# Validates base62 conversion for 1000
def test_base62_encoding():
    mock_obj = URL_shortner("1000")
    if mock_obj.base62_conversion("1000") == "g8":
        print("Base62 conversion passed")
    else:
       print("Base62 conversion failed")

# Test add key 
def test_add_key():
    mock_obj = RedisCache("http://mock_link.com")
    mock_obj.add_key()
    redis_cli = redis.Redis()
    db_value = redis_cli.get("http://mock_link.com") # get value from db
    if db_value:    # Checks if value is present in redis
        print("Add key Passed")
        redis_cli.delete("http://mock_link.com")
        last_index = int(redis_cli.lindex("index_list", 0))
        redis_cli.lrem("index_list", 0, last_index) # Cleanup Step
    else:
        print("Add key Failed")

# Test Search Cache
def test_search_cache():
    mock_obj = RedisCache("http://mock_link.com")
    mock_obj.add_key()
    cached_value = mock_obj.search_cache()
    if cached_value:
        print("Search Cache Passed")
        redis_cli = redis.Redis()
        redis_cli.delete("http://mock_link.com")
        last_index = int(redis_cli.lindex("index_list", 0))
        redis_cli.lrem("index_list", 0, last_index) # Cleanup step 
    else:
        print("Search Cache Failed")

try:
    redis_cli = redis.Redis()
    redis_cli.ping()
    test_base62_encoding()
    test_add_key()
    test_search_cache()
except:
    print("Make sure your redis server is started !")
