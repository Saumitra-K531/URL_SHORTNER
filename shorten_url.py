# Base Class URL Shortner
class URL_shortner(object):
  shorten_url = False
  # base62 mappings
  base62_mapping = ['0','1','2','3','4','5','6','7','8','9','a',
                'b','c','d','e','f','g','h','i','j','k','l',
                'm','n','o','p','q','r','s','t','u','v','w'
                'x','y','z','A','B','C','D','E','F','G','H'
                'I','J','K','L','U','V','W','X','Y','Z'] 
  
  def __init__(self, input_url):
      self.input_url = input_url

  # Function to convert base 10 value to base 62 value
  def base62_conversion(self, input_val):
      encoded_result = ""
      int_input_val = int(input_val)
      while(int_input_val > 0):
          remainder = int_input_val % 62
          int_input_val = int_input_val // 62
          encoded_result = encoded_result + self.base62_mapping[remainder]
      return encoded_result[::-1]

  # This function calls base62_encoder to encode index value of url
  def url_shortener(self, index):
    result = "http://url_shortner.com/"
    encoded_value = self.base62_conversion(index)
    return result + str(encoded_value)