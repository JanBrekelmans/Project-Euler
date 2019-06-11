# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

import functions

NUMBER = int(2e6)

def compute():
    total = 0
    
    primes = functions.prime_sieve(NUMBER)
    
    total = sum(primes)
            
    return str(total)
    
    
if __name__ == "__main__":
    print(compute())