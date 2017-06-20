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

    try:
        print("TITLE: "+bsObj.h1.get_text())
        print("CONTENT: "+bsObj.find(id="mw-content-text").findAll("p")[0].get_text())
        print("LINK URL: "+bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("[ERROR] This page is missing something! No worries though!")

    for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print("-----------------------\n"+newPage)
                pages.add(newPage)
                getLinks(newPage)

links = getLinks("")