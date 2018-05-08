import urllib.request
from bs4 import BeautifulSoup
import re

def strip(name):
	name = re.sub(r'^a ','',name)
	name = re.sub(r'^an ','',name)
	name = re.sub(r'^the ','',name)
	return name

def convert(name):
	name = re.sub(r'[^a-z0-9]', '', name)
	return name

song = convert(input("Song: ").lower())
singer = convert(strip(input("Artist: ").lower()))

url = "https://www.azlyrics.com/lyrics/" + singer + "/" + song + ".html"

try:
	html = urllib.request.urlopen(url).read()
	print(BeautifulSoup(html, 'html.parser').find_all('div')[21].text)
except:
	print("Incorrect Song name or Artist Name")