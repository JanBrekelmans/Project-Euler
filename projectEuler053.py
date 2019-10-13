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
    
    for n in range(1,101):
        for r in range(1,n+1):
            if functions.binomial(n,r) > 1000000:
                total += 1
            
    return str(total)
    
    
if __name__ == "__main__":
    print(compute())