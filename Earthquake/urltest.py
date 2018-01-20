import csv
import urllib.request
#import codecs

# function to get the data from the usgs website Q8
# you will have to change the url
def readDataFromURL():
	try:
		lines = []
		url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv'
		response = urllib.request.urlopen(url)
		reader = csv.reader(response.read().decode('utf-8').splitlines())
  	#reader = csv.reader(codecs.iterdecode(response, 'utf-8'))
		
		for row in reader:
				lines.append(row)
		return lines
	except (Exception):
		print("Unable to get data from website")

print(readDataFromURL())
