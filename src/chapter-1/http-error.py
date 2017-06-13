from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup

try:
    html = urlopen("http://www.pythonscraping.com/pages.error.html")

    bsObj = BeautifulSoup(html.read(), "html.parser")
    print(bsObj.h1)
except HTTPError as e:
    print(e)
else:
    print("continue...")