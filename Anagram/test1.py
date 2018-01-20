# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 18:29:28 2015

@author: Greg
"""

str1 = "excellent"
str2 = "excelentl"
searchlength1 = len(str1)
searchlength2 = len(str2)
if len(str1) == len(str2):
        for x in range(0, searchlength1):
            for y in range(0, searchlength2):
                if str1[x] == str2[y]:
                    str1 = str1[0:x] + str1[x+1:len(str1)]
                    str2 = str2[0:x] + str2[x+1:len(str2)]
                    print(str1)
                    print(str2)
                    searchlength1 = len(str1)
                    searchlength2 = len(str2)
        if len(str1) + len(str2) == 0:
            print("true")
else:
    print("false")
