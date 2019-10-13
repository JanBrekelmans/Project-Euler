# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

import functions

UPPER_BOUND = 1000000

def compute():
    total = 0
    
    primes = functions.prime_sieve(UPPER_BOUND)
    check = functions.prime_check(UPPER_BOUND)
    
    maximum = 0
    max_prime = 0
    
    for i in range(len(primes)):
        
        consecutive = 1
        
        temp_sum = primes[i]
        
        for j in range(i+1,len(primes)):
            
            temp_sum += primes[j]
            consecutive += 1
            
            if temp_sum >= UPPER_BOUND:
                break
            
            if check[temp_sum] and consecutive > maximum:
                maximum = consecutive
                max_prime = temp_sum
            
        
            
    return str(max_prime)
    
    
if __name__ == "__main__":
    print(compute())