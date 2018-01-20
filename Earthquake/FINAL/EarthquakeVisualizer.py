# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 18:59:03 2015

@author: Greg
"""
NewData = False
filename = 'earthquakedata.csv'
lines = []
import csv
import sys
import urllib.request


def csvimport(filename):
    try: #error handling
        eqdata = []
        with open(filename, newline='',) as csvfile: #opens csvfile
            readdata = csv.reader(csvfile, delimiter=' ', quotechar='|') #read the data from the file 
            for row in readdata:
                eqdata.append(row) #adds each row to an array
            del eqdata[0] # deleted first row
            print(eqdata)
    except: 
       print("An error occured.")       
def csvpresent(filename):
    eqtime = []
    eqlatitude = []    
    eqlongitude = []
    eqdepth = []
    eqmagnitude = []
    eqlatlen = 0
    eqlonlen = 0
    eqdeplen = 0
    with open(filename, newline='') as f: # opens csv
        if NewData == True:
            reader = readDataFromURL.reader #considers if new data has been imported, and if so replaces it 
        else: reader = csv.reader(f)
        print("Set(" + "Number" + "): " + "Time" + " | " + "Latitude" + " | " + "Longitude" + " | " + "Depth" + " | " + "Magnitude") #header
        for row in reader:
             eqtime.append(row[0])  #adds each of the 5 variables to its own indiviual array, for this line it adds time to the eqtime array

             eqlatitude.append(row[1])
             if len(row[0]) > eqlatlen: #as it goes through it measures the character length of the longest peice of data and records it
                 eqlatlen = len(row[0])
             
             eqlongitude.append(row[2])
             if len(row[0]) > eqlonlen:
                 eqlonlen = len(row[0])

             eqdepth.append(row[3])
             if len(row[0]) > eqdeplen:
                 eqdeplen = len(row[0])

             eqmagnitude.append(row[4])

        del eqtime[0] #deletes headers
        del eqlatitude[0]
        del eqlongitude[0]
        del eqdepth[0]
        del eqmagnitude[0]
        csvpresent.eqtime = eqtime #allows the data to be accessable outside of the function
        csvpresent.eqlatitude =eqlatitude
        csvpresent.eqlongitude = eqlongitude
        csvpresent.eqdepth = eqdepth
        csvpresent.eqmagnitude = eqmagnitude
        for i in range(len(eqtime)):
            print("Set(" + str(i) + "): " + eqtime[i] + " | " + eqlatitude[i], end='') #writes the data for each row
            lenadd = eqlatlen - len(eqlatitude[i])
            for j in range(lenadd): #prints a number of spaces after the data relavent to the longest peice of data
                print(" ", end='')
            print(" | " + eqlongitude[i], end='')
            lenadd = eqlonlen - len(eqlongitude[i])
            for j in range(lenadd):
                print(" ", end='')
            print( " | " + eqmagnitude[i], end='')    
            lenadd = eqdeplen - len(eqdepth[i])
            for j in range(lenadd):
                print(" ", end='')
            print( " | " + eqdepth[i])

def writeHTML(filename):
    #opens a html file to be created
    with open("index.html","w") as html:
        # write the boilerplate html stuff
        html.write("<!DOCTYPE html>\n")
        html.write("<html>\n")
        html.write("<head>\n")
        html.write("<meta charset=\"UTF-8\">\n")
        html.write("<style>\n")
        html.write("table, th, td {\n")
        html.write("border: 1px solid black;\n")
        html.write("border-collapse: collapse;\n")
        html.write("}\n")
        html.write("</style>\n")
        html.write("<title>Earthquake Data</title>\n")
        html.write("</head>\n")
        html.write("<body>\n")
        html.write("<h2>Earthquake Data</h2>\n")
        html.write("<table>\n")
        
        # open a csv file to read data from
        with open(filename,"r") as f:
            f.readline()
            # format the table header 
            html.write("<tr>\n")
            html.write("<th> Time </th>\n")	
            html.write("<th> Longitude </th>\n")
            html.write("<th> Latitude </th>\n")
            html.write("<th> Depth </th>\n")
            html.write("<th> Magnitude </th>\n")
            html.write("<th> Magnitude Type </th>\n")
            html.write("<th> NST </th>\n")
            html.write("<th> Gap </th>\n")
            html.write("<th> Dmin </th>\n")
            html.write("<th> RMS </th>\n")
            html.write("<th> Net </th>\n")	
            html.write("<th> ID </th>\n")
            html.write("<th> Updated </th>\n")
            html.write("<th> Place </th>\n")
            html.write("<th> Type </th>\n")
            html.write("</tr>\n")
        #considers if new data has been imported
            if NewData  == True:
                reader = readDataFromURL.reader 
            else: reader = csv.reader(f)
            
            # iterate over the lines in the file printing out formatted html
            for row in reader:
                html.write("<tr>\n")
                for elm in row:
                    html.write("<td>"+ elm + "</td>\n")
                html.write("</tr>\n")
                    
                    # close all the opened html tags
            html.write("</table>\n")
            html.write("</body>\n")
            html.write("</html>>\n")
                    
def numberOfQuakes(filename):
    numberofrows = 0
    with open(filename, newline='',) as csvfile:
        
        readdata = csv.reader(csvfile, delimiter=' ', quotechar='|') 
        for row in readdata:
            numberofrows = numberofrows + 1
    if NewData  == True:
        numberofrows = len(lines)
    print("Number of earthquakes: "+ str(numberofrows - 1))
    numberOfQuakes.numberofrows = numberofrows - 1



def averageDepth(filename):
    eqdepth = []
    eqdepth_average = 0
    with open(filename, newline='') as file:
        if NewData == True:
            url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv'
            response = urllib.request.urlopen(url) #defines response as the csv file form the url
            reader = csv.reader(response.read().decode('utf-8').splitlines()) #reads and formats the csv file
        else: reader = csv.reader(file)        
        for row in reader:
             eqdepth.append(row[3])
        del eqdepth[0]
        for i in range(len(eqdepth)):
            eqdepth_average = eqdepth_average + float(eqdepth[i])
    eqdepth_average = eqdepth_average / len(eqdepth)
    print("Average Depth: " + str(eqdepth_average))
    averageDepth.eqdepth_average = eqdepth_average

def MagMax(filename):
    readDataFromURL()
    eqmagnitude = []
    MagMax_Compare  = 0
    MagMaxRow = 0
    rows = []
    with open(filename, newline='') as file:
        if NewData == True:
            url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv'
            response = urllib.request.urlopen(url) #defines response as the csv file form the url
            reader = csv.reader(response.read().decode('utf-8').splitlines()) #reads and formats the csv file
        else: reader = csv.reader(file)
        for row in reader:       
            rows.append(row)
            eqmagnitude.append(row[4])
        del eqmagnitude[0]
        for i in range(len(eqmagnitude)):
            if float(eqmagnitude[i]) > float(MagMax_Compare):
                MagMax_Compare = eqmagnitude[i]
                MagMaxRow = i
        print("Data of the maximum magnitude earthquake:")
        print(rows[MagMaxRow + 1])
        MagMax.MagMaxRow = MagMaxRow

def MagMin(filename):
    eqmagnitude = []
    MagMin_Compare  = 0
    MagMinRow = 0
    rows = []
    with open(filename, newline='') as file:
        if NewData == True:
            url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv'
            response = urllib.request.urlopen(url) #defines response as the csv file form the url
            reader = csv.reader(response.read().decode('utf-8').splitlines()) #reads and formats the csv file
        else: reader = csv.reader(file)
        for row in reader:       
            rows.append(row)
            eqmagnitude.append(row[4])
        del eqmagnitude[0]
        for i in range(len(eqmagnitude)):
            if float(eqmagnitude[i]) < float(MagMin_Compare):
                MagMin_Compare = eqmagnitude[i]
                MagMinRow = i
        print("Data of the maximum magnitude earthquake:")
        print(rows[MagMinRow + 1])
        MagMin.MagMinRow = MagMinRow
        
        
        #this was a section of the program i made after reading a task incorrectly
       #what it does is created a html file but using only the 5 selected columns of data from the previous task      

#def writeHTML_Modified2(filename):                                                 
#    csvpresent(filename) 
#    with open("indexModified2.html","w") as html:
#        # write the boilerplate html stuff
#        html.write("<!DOCTYPE html>\n")
#        html.write("<html>\n")
#        html.write("<head>\n")
#        html.write("<meta charset=\"UTF-8\">\n")
#        html.write("<style>\n")
#        html.write("table, th, td {\n")
#        html.write("border: 1px solid black;\n")
#        html.write("border-collapse: collapse;\n")
#        html.write("}\n")
#        html.write("</style>\n")
#        html.write("<title>Title of the document</title>\n")
#        html.write("</head>\n")
#        html.write("<body>\n")
#        html.write("<h2>Header title</h2>\n")
#        html.write("<table>\n")
#        
#        # open a csv file to read data from
#        with open(filename,"r") as students:
#            students.readline()
#            # format the table header 
#            html.write("<tr>\n")
#            html.write("<th> Time </th>\n")	
#            html.write("<th> Longitude </th>\n")
#            html.write("<th> Latitude </th>\n")
#            html.write("<th> Depth </th>\n")
#            html.write("<th> Magnitude </th>\n")
#            html.write("</tr>\n")
#            
#         #   reader = csv.reader(students)
#                                                                                    #for i in range of items in one of the arrays from the file
#            # iterate over the lines in the file printing out formatted html
#          #  for row in reader:
#            for i in range(len(csvpresent.eqtime)):
#                html.write("<td>"+ csvpresent.eqtime[i] + "</td>\n")
#                html.write("<td>"+ csvpresent.eqlatitude[i] + "</td>\n")
#                html.write("<td>"+ csvpresent.eqlongitude[i] + "</td>\n")
#                html.write("<td>"+ csvpresent.eqdepth[i] + "</td>\n")
#                html.write("<td>"+ csvpresent.eqmagnitude[i] + "</td>\n")
#                html.write("</tr>\n")
#                    
#         # close all the opened html tags
#            html.write("</table>\n")
#            html.write("</body>\n")
#            html.write("</html>>\n")
                    
def writeHTMLModified(filename): #modified HTML code where only the values from question 5 are shown
    numberOfQuakes(filename)
    averageDepth(filename)
    MagMax(filename)
    MagMin(filename)
    with open("indexModified.html","w") as html:
        # write the boilerplate html stuff
        html.write("<!DOCTYPE html>\n")
        html.write("<html>\n")
        html.write("<head>\n")
        html.write("<meta charset=\"UTF-8\">\n")
        html.write("<style>\n")
        html.write("table, th, td {\n")
        html.write("border: 1px solid black;\n")
        html.write("border-collapse: collapse;\n")
        html.write("}\n")
        html.write("</style>\n")
        html.write("<title>Earthquake Data [Modified]<title>\n")
        html.write("</head>\n")
        html.write("<body>\n")
        html.write("<h2>Earthquake Data [Modified] </h2>\n")
        html.write("<table>\n")
        
        # open a csv file to read data from
        with open(filename,"r") as f:
            f.readline()
            # format the table header 
            html.write("<tr>\n")
            html.write("<th> Time </th>\n")	
            html.write("<th> Longitude </th>\n")
            html.write("<th> Latitude </th>\n")
            html.write("<th> Depth </th>\n")
            html.write("<th> Magnitude </th>\n")
            html.write("<th> Magnitude Type </th>\n")
            html.write("<th> NST </th>\n")
            html.write("<th> Gap </th>\n")
            html.write("<th> Dmin </th>\n")
            html.write("<th> RMS </th>\n")
            html.write("<th> Net </th>\n")	
            html.write("<th> ID </th>\n")
            html.write("<th> Updated </th>\n")
            html.write("<th> Place </th>\n")
            html.write("<th> Type </th>\n")
            html.write("<th> numberOfQuakes </th>\n")
            html.write("<th> averageDepth </th>\n")
            html.write("</tr>\n")
            
            if NewData == True:
                reader = readDataFromURL.reader
            else: reader = csv.reader(f)
            
            # iterate over the lines in the file printing out formatted html
            x = 0            
            for row in reader:
                if x == MagMax.MagMaxRow or x == MagMin.MagMinRow:
                    html.write("<tr>\n")
                    for elm in row:
                        html.write("<td>"+ elm + "</td>\n")  
                    html.write("<td>"+ str(numberOfQuakes.numberofrows) + "</td>\n")                    
                    html.write("<td>"+ str(averageDepth.eqdepth_average) + "</td>\n")   
                    html.write("</tr>\n")     
                x = x + 1
            # close all the opened html tags
        html.write("</table>\n")
        html.write("</body>\n")
        html.write("</html>>\n")

def Menu(filename):
     print("")
     print("")
     print("What would you like to do? : ")
     print("")
     print("Type \"1\" to - Veiw the data")
     print("Type \"2\" to - View the statistics")
     print("Type \"3\" to - Created a HTML document")
     print("Type \"4\" to - Import new data from the internet")
     print("Type \"5\" to - Close the program")
     print("")
     print("") 
     UserInput = 0
     UserInput = input()
     Menu.UserInput = UserInput
     if UserInput == "1":
         csvpresent(filename)
     elif UserInput == "2":
        averageDepth(filename)
        numberOfQuakes(filename)
        print("Time" + " | " + "Latitude" + " | " + "Longitude" + " | " + "Depth" + " | " + "Magnitude")
        MagMax(filename)
        MagMin(filename)
     elif UserInput == "3":
        writeHTML(filename)
     elif UserInput == "4": #runs the function to import new data
        readDataFromURL()
        print(str(NewData))
     elif UserInput == "5":
        sys.exit()
     else:
        print("Something wasn't quite right, please try again")
        

def readDataFromURL():
	try: #considers errors
 
		global NewData	
		NewData = True 
		global lines
		 #tells the program new data has been imported
  
		LinesIn = []
		url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv'
		response = urllib.request.urlopen(url) #defines response as the csv file form the url
		reader = csv.reader(response.read().decode('utf-8').splitlines()) #reads and formats the csv file
  	#reader = csv.reader(codecs.iterdecode(response, 'utf-8'))              this was a section fo code suggested to be more efficiant, but the code provided works fine
		
		for row in reader:
				LinesIn.append(row) #add the rows of the file to an array
		del LinesIn[0] #deletes header
		return LinesIn
  
		lines = LinesIn
  
	except (Exception):
		print("Unable to get data from website")	
		global NewData	
		NewData = True 
#print(readDataFromURL())
        


#import codecs
print("")
print("")
print("Welcome to....") 
print("")
print("")                
print("███████╗ █████╗ ██████╗ ████████╗██╗  ██╗ ██████╗ ██╗   ██╗ █████╗ ██╗  ██╗███████╗")
print("██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██║  ██║██╔═══██╗██║   ██║██╔══██╗██║ ██╔╝██╔════╝")
print("█████╗  ███████║██████╔╝   ██║   ███████║██║   ██║██║   ██║███████║█████╔╝ █████╗  ")
print("██╔══╝  ██╔══██║██╔══██╗   ██║   ██╔══██║██║▄▄ ██║██║   ██║██╔══██║██╔═██╗ ██╔══╝  ")
print("███████╗██║  ██║██║  ██║   ██║   ██║  ██║╚██████╔╝╚██████╔╝██║  ██║██║  ██╗███████╗")
print("╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚══▀▀═╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝")
print("`7MM\"\"\"Yb.      db   MMP\"\"MM\"\"YMM   db      ")
print("  MM    `Yb.   ;MM:  P'   MM   `7  ;MM:     ")
print("  MM     `Mb  ,V^MM.      MM      ,V^MM.    ")
print("  MM      MM ,M  `MM      MM     ,M  `MM    ")
print("  MM     ,MP AbmmmqMA     MM     AbmmmqMA   ")
print("  MM    ,dP'A'     VML    MM    A'     VML  ")
print(".JMMmmmdP'.AMA.   .AMMA..JMML..AMA.   .AMMA.")
Menu(filename)
while Menu.UserInput != 5 :
    Menu(filename)

sys.exit()

























#.