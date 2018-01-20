# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 13:13:46 2015

@author: Greg
"""

data = False

def changedata():
    global data
    data = True
    
changedata()
print(data)