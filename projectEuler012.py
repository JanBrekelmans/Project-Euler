# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

import functions


def compute():
    
    num_divisors = 0
    index = 200
    
    while num_divisors <= 500:
        triangle = index*(index+1)//2
        
        num_divisors = functions.number_of_divisors(triangle)
        
        index += 1

    return str(triangle)
        
        
    
    
if __name__ == "__main__":
    print(compute())