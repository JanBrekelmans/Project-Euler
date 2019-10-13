# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

import functions

LIMIT = 1000000

def compute():
    total = 0
    
    primes = functions.prime_sieve(LIMIT)
    
    check = [False]*LIMIT
    
    for i in primes:
        string = str(i)
        
        length = len(string)
        
        summation = i
        
        for j in range(length-1):
            
            if not check[int(string[j+1:])]:
                summation = 0
                break
            
            if not check[int(string[:j-1])]:
                summation = 0
                break
        
        total += summation
        
        
            
    return str(total)
    
    
if __name__ == "__main__":
    print(compute())