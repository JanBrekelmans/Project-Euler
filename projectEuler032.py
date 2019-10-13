# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

import math

LIMIT = 10000

def is_pandigital(c):
    
    for a in range(1,int(math.sqrt(c)+1)):
        if c%a == 0:
            b = c//a
            
            string = str(c) + str(a) + str(b)
            
            string = "".join(sorted(string))
            
            if string == "123456789":
                return True
    
    return False

def compute():
    total = 0
    
    for c in range(2,LIMIT):
        if is_pandigital(c):
            total += c
            
    return str(total)
    
    
if __name__ == "__main__":
    print(compute())