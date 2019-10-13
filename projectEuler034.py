# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

import functions

LIMIT = 100000

def compute():
    total = 0
    
    fac = [0] * 10
    
    for i in range(10):
        fac[i] = functions.factorial(i)
    
    for i in range(3,LIMIT):
        temp = 0
        
        temp = sum(fac[int(i)] for i in str(i))
        
        if temp == i:
            total += i
            
    return str(total)
    
    
if __name__ == "__main__":
    print(compute())