from urllib.request import urlopen
from bs4 import BeautifulSoup

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
content = bytes(content, "UTF-8")
content = content.decode("UTF-8")

print(content)