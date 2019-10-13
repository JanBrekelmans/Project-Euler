# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

import functions

def compute():
    maximal = 0
    total = 0
    
    # Construct lists for a and b
    zeroth = functions.prime_sieve(1000)
    first = [-i for i in zeroth]
    first = first + zeroth
    
    # Construct list for checking if prime
    temp = functions.prime_sieve(3*1000*1000)
    checking = 3*1000000 * [False]
    for i in temp:
        checking[i] = True
    
    for a in first:
        for b in zeroth:
            
            maximum = 0
            n = 0
            
            while checking[n*n + a*n + b]:
                n += 1
                maximum += 1
            
            if maximum > maximal:
                maximal = maximum
                total = a*b
            
    
            
    return str(total)
    
    
if __name__ == "__main__":
    print(compute())