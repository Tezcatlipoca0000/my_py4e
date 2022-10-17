# Lesson 29 Networking IV Web Scraping

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter a url: ') # https://www.dr-chuck.com/page1.htm
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser') # Return all the html 
print(type(soup)) # class 'bs4.BeautifulSoup'
print(soup) 

tags = soup('a') # Return a list with all the anchor tags
print(type(tags)) # class 'bs4.element.ResultSet'
print(tags) 
for tag in tags :
    print(tag.get('href'))