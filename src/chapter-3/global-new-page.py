from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import re

pages = set()

def getLinks(articleUrl):
    global pages
    html = urlopen("https://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")

    for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

links = getLinks("")