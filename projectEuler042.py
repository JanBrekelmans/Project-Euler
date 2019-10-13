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
    
    names = open("p042_words.txt","r")
    names = names.read()
    names = names.replace('"',"")
    names = names.split(',')
    
    
    check = [False]*1000
    
    i = 1
    while functions.triangle(i) < 1000:
        check[functions.triangle(i)] = True
        i += 1
    
    for i in names:
        temp = 0
        for j in i:
            temp += functions.char_place(j)
        
        if check[temp]:
            total += 1
            
    return str(total)
    
    
if __name__ == "__main__":
    print(compute())