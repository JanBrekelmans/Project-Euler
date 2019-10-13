# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

import functions

def compute():
    total = 0
    
    names = open("p022_names.txt","r")
    names = names.read()
    names = names.replace('"',"")
    names = names.split(',')
    
    names.sort()
    
    for i in range(0,len(names)):
        value = sum((ord(char) - 96) for char in names[i].lower())
        
        total += value*(i+1)
            
    return str(total)
    
    
if __name__ == "__main__":
    print(compute())