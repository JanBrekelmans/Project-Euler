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
    totalLength = 0
    
    # We will use memoization
    
    upper_bound = 1000001
    
    memoization = [0]*upper_bound
    
    for i in range(1,upper_bound):
        length = 0
        collatz = i
        
        while collatz > 1:
            collatz = functions.Collatz(collatz)
            length += 1
            
            if collatz < upper_bound:
                if memoization[collatz] > 0:
                    length = length + memoization[collatz]
                    break
            
        memoization[i] = length
            
        if totalLength < length:
            total = i
            totalLength = length
            
    return str(total)
    
    
if __name__ == "__main__":
    print(compute())