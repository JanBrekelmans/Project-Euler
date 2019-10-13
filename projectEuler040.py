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
    
    string = ''.join(str(i) for i in range(1,1000000))
    
    for i in range(1,7):
        total *= int(string[10**i-1])
    
    return str(total)
    
    
if __name__ == "__main__":
    print(compute())