import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html, "html.parser")

table = bsObj.findAll("table", {"class":"wikitable"})[0]
rows = table.findAll("tr")
csvFile = open("./files/editors.csv", "wt")
writer = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(["td", "th"]):
            csvRow.append(cell.get_text().encode("utf8"))
        writer.writerow(csvRow)
finally:
    csvFile.close()