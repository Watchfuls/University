# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 18:52:55 2015

@author: Greg
"""

str1 = "m"
str2 = "m"
searchlength1 = len(str1)
searchlength2 = len(str2)
z = searchlength1   
print(searchlength1)
print(searchlength2)
v = 0 
while searchlength1 > 0 and searchlength2 > 0 and v < z:
    try:
        for x in range(0, z):
            v = 0
            for y in range(0, z):
                if str1[x] == str2[y]:
                    str1 = str1[0:x] + str1[x+1:len(str1)]
                    str2 = str2[0:y] + str2[y+1:len(str2)]
                    print(str1)
                    print(str2)
                    searchlength1 = len(str1)
                    searchlength2 = len(str2)
                else: v = v + 1
    except:
        z = z - 1
        
print("\""+str1+"\"")
print("\""+str2+"\"")

if searchlength1 == 0 and searchlength2 == 0:
    print("true")
else:
    print("false")