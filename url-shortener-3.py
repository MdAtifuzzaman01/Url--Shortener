"""
This url shortener is created by using cuttly api and I used requests
"""
import requests 
api_key = "Your_Api_key"
url = input()
api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
data = requests.get(api_url).json() ['url']
if data["status"] == 7:
    shortened_url = data["shortLink"]
    print("Shortened URL:", shortened_url)
else:
    print("[!] Error Shortening URL:", data)