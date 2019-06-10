# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:49:35 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

import functions

def compute():
    number = 600851475143
    
    factors = functions.primeFactors(number)
            
    return str(max(factors))
    
    
if __name__ == "__main__":
    print(compute())