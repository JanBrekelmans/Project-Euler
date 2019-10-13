# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

import functions

def compute():
    total = {4}
    
    for a in range(2,101):
        for b in range(2,101):
            total.add(a**b)
    
    total = len(total)
    
    
            
    return str(total)
    
    
if __name__ == "__main__":
    print(compute())