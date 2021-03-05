"""
I have created an url shortener by using bitly_api
You can use it by creating a free account on bitly
"""

import bitly_api
BITLY_ACCESS_TOKEN = " Put your access token here"  # get the token from https://bitly.is/accesstoken
access  = bitly_api.Connection(acess_token = BITLY_ACCESS_TOKEN)
full_link = input('Enter the full token')
short_url = access.shorten(full_link)
print('Short url = ' , short_url [ 'url'])