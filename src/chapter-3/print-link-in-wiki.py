from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html, "html.parser")

for link in bsObj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])