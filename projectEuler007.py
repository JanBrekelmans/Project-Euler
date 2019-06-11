# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

import functions
import numpy as np

def compute():
    index = 10001
    
    n = functions.prime_upper_bound(index)
    
    primes = functions.prime_sieve(n)
    
    return str(primes[index-1])
    
    
if __name__ == "__main__":
    print(compute())