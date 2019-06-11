# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:34:44 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

import functions

def compute():
    upper_bound = 4000000
    
    n = functions.Fibonnaci_ceil(upper_bound)
    
    fibonacci = functions.Fibonacci_array(n)
    
    total = 0
    
    for i in fibonacci:
        if i%2 == 0:
            total += i
            
    return str(total)
    
    
if __name__ == "__main__":
    print(compute())