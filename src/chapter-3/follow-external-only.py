from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

pages = set()
random.seed(datetime.datetime.now())

def getInternalLinks(bsObj, includeUrl):
    includeUrl = urlparse(includeUrl).scheme + "://"+urlparse(includeUrl).netloc
    internalLinks = []

    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in internalLinks:
                if(link.attrs["href"].startWith("/")):
                    internalLinks.append(includeUrl+link.attrs["href"]);
                else:
                    internalLinks.append(link.attrs["href"])

    return internalLinks

def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []

    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in externalLinks:
                externalLinks.append(link.attrs["href"])

    return externalLinks

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, "html.parser")
    externalLinks = getExternalLinks(bsObj, urlparse(startingPage).netloc)

    if len(externalLinks) == 0:
        domain = urlparse(startingPage).scheme+"://"+urlparse(startingPage).netloc
        internalLinks = getInternalLinks(bsObj, domain)

        return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])

    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("Random external link is: " + externalLink)
    followExternalOnly(externalLink)

followExternalOnly("https://www.oreilly.com/")