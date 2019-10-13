# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

import functions

LIMIT = 1000 + 1

def compute():
    total = 0
    maximum = 0
    
    for p in range(1,LIMIT):
        temp = 0
        
        for a in range(1,p):
            for b in range(a,(p-a)//2 + 1):
                
                if a*a + b*b == (p-a-b)*(p-a-b):
                    temp += 1
        
        if temp > maximum:
            maximum = temp
            total = p
        
            
    return str(total)
    
    
if __name__ == "__main__":
    print(compute())