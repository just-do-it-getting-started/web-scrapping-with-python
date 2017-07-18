from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv")\
    .read()\
    .decode("ascii", "ignore")

dataFile = StringIO(data)
csvReader = csv.reader(dataFile)

for row in csvReader:
    albumName = row[0]
    releasedYear = row[1]

    print("The album " + albumName + " was released in "+str(releasedYear))