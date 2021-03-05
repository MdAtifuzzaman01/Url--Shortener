"""
I have created an url shortener and expander   by using pyshortener 
"""
 

from pyshorteners import Shorteners
ACCESS_TOKEN = 'Your token' #you can get one from https://bitly.is/accesstoken

#Shorten long url 

long_url = input("Enter the url")
url_shortener = Shortener('Bitly ' , bitly_token = ACCESS_TOKEN)
print('Short url is {}'.format(url_shortener.short(long_url)))


#Expand short url

short_url = input('Enter Short url')
url_expander = Shortener('Bitly' , bitly_token = ACCESS_TOKEN)
print('Long url is {}'.format(url_expander.expand(short_url)))