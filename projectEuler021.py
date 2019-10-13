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
    
    
    for a in range(2,10000):
        b = sum(functions.proper_divisors(a))
        
        if b > a:
            if sum(functions.proper_divisors(b)) == a:
                total = total + a + b
            
    return str(total)
    
    
if __name__ == "__main__":
    print(compute())