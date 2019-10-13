# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

import functions

N = 500

def compute():
    total = 0
            
    total += 1
    
    for i in range(1,N+1):
        for k in range(4):
            add = (1+2*i)**2
            add -= 2*k*i
           
            total += add
    
    return str(total)
    
    
if __name__ == "__main__":
    print(compute())