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
    
    for a in range(1,101):
        for b in range(1,101):
            temp = [int(x) for x in str(a**b)]
            temp = sum(temp)
            
            if temp > total:
                total = temp
            
    return str(total)
    
    
if __name__ == "__main__":
    print(compute())