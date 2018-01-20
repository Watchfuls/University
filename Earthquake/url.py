import urllib.request

# function to get the data from the usgs website Q8
# you will have to change the url
def readDataFromURL():
	try:
		lines = []
		url = 'http://www.leeds.ac.uk'
		response = urllib.request.urlopen(url)
		reader = csv.reader(read.response().decode('utf-8').splitlines())
		
		for row in reader:
				lines.append(row)
		return lines
	except (Exception):
		print("Unable to get data from website")

print(readDataFromURL())
