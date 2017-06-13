from urllib.request import urlopen
from bs4 import BeautifulSoup

try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
    bsObj = BeautifulSoup(html.read(), "html.parser")
    badContent = bsObj.blhablha
except AttributeError as e:
    print(e)
else:
    if badContent == None:
        print("Tag was not found")
    else:
        print(badContent)