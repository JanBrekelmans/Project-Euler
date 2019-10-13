# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

import functions

UPPER_LIMIT = 354294
exponent = 5

def compute():
    total = 0
    
    for i in range(2,UPPER_LIMIT):
        n = i
        
        summation = 0
        
        while n > 0:
            rem = n % 10
            
            summation += rem**exponent
            
            n = (n-rem) // 10
        
        if i == summation:
            total += i
            
    return str(total)
    
    
if __name__ == "__main__":
    print(compute())