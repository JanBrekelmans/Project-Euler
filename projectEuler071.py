# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

import functions
import math

UPPER_BOUND = 1000000

def compute():
    solution = 0
    
    best = 0
    
    for b in range(2,UPPER_BOUND):
        for a in range(math.floor(3*b/7),1,-1):
            if functions.GCD(a,b) == 1:
                if a/b > best:
                    solution = a
                    break
    
            
    return str(solution)
    
    
if __name__ == "__main__":
    print(compute())