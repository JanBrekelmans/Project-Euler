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
    
    for i in range(1,1001):
        total += i**i
        
        total= total%10000000000
            
    return str(total)
    
    
if __name__ == "__main__":
    print(compute())