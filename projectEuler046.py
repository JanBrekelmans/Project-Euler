# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

import functions
import math

# random upper bound
UPPER_BOUND = 10000

def compute():
    total = 0
    
    sieve = functions.prime_sieve(UPPER_BOUND)
    
    numbers = UPPER_BOUND * [0]
    
    for i in sieve:
        
        for j in range(0,int(math.sqrt(UPPER_BOUND)/2)):
            if i + 2*j*j >= UPPER_BOUND:
                break
            
            numbers[i+2*j*j] += 1
    
    for i in range(UPPER_BOUND):
        if numbers[i] == 0 and i%2 == 1 and i > 5:
            total = i
            break
            
    return str(total)
    
    
if __name__ == "__main__":
    print(compute())