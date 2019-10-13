# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

import functions
import math

def compute():
    total = 0
    
    for D in range(2,1001):
        d = int(math.sqrt(D))
        
        if D//d != d:
            print(D)
            
    return str(total)
    
    
if __name__ == "__main__":
    print(compute())