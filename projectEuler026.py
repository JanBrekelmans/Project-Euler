# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

import functions

def compute():
    total = 1
    length = 1
    
    for i in range(3,1001,2):
        p = 1
        
        if i % 5 == 0:
            continue
        
        while (10**p) % i != 1:
            p += 1
        
        if p > length:
            length = p
            total = i
            
    return str(total)
    
    
if __name__ == "__main__":
    print(compute())