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
    
    sieve = functions.prime_sieve(int(10**4))
    
    primes = [False] * int(10**4)
    
    for i in sieve:
        primes[i] = True
    
    for i in sieve:
        
        if i > 10**4/3:
            break
        
        if i > 1000:
            for j in range(1,int(10**4 /3)):
                
                if primes[i+j] and primes[i+2*j]:
                    
                    p1 = str(i)
                    p2 = str(i+j)
                    p3 = str(i+2*j)
                    
                    if sorted(p1) == sorted(p2) and sorted(p2) == sorted(p3):
                        
                        if i is not 1487:
                            total = p1+p2+p3
            
        
            
    return str(total)
    
    
if __name__ == "__main__":
    print(compute())