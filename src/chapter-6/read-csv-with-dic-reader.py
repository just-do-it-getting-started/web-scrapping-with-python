from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv")\
    .read()\
    .decode("ascii", "ignore")

dataFile = StringIO(data)
csvReader = csv.reader(dataFile)
dictReader = csv.DictReader(dataFile)

print(dictReader.fieldnames)

for row in dictReader:
    albumName = row["Name"]
    releasedYear = row["Year"]

    print("The album " + albumName + " was released in "+str(releasedYear))