import ast
import redis
from shorten_url import URL_shortner 

# Redis Cache Class is derived from base class URL_shortner 
class RedisCache(URL_shortner):
    redis_cli = redis.Redis() # Intializing redis client

    # This function adds original_url, index id (incremental), shortened url to redis 
    def add_key(self):
        last_index = 0
        first_index = False
        json_value = {"Shortened_URL": ""}
        shortened_url = ""
        try:
            # Fetching last updated index
            last_index = int(self.redis_cli.lindex("index_list", 0))
        except:
            # To create first index
            first_index = True
            self.redis_cli.lpush("index_list",str(1))
        shortened_url = URL_shortner.url_shortener(self,last_index+1)
        json_value["Shortened_URL"] = shortened_url
        if first_index == False: # Check if not first index since first index is pushed in except block
            self.redis_cli.lpush("index_list", str(last_index + 1))
        self.redis_cli.set(self.input_url,str(json_value))
        return json_value
    
    # This function searches redis cache 
    # If url present in c0ache return it else call add_key
    def search_cache(self):
        redis_search_result = self.redis_cli.get(self.input_url)
        if redis_search_result != None:
            return ast.literal_eval(redis_search_result.decode('UTF-8'))
        else: 
            result = self.add_key()
            return result