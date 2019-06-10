# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

import functions

def compute():
    maximum = 0
    
    for i in range(100,1000):
        for j in range(i,1000):
            
            product = i*j
            
            if functions.is_palindrome(product):
                if product > maximum:
                    maximum = product

     
    return str(maximum)
    
    
if __name__ == "__main__":
    print(compute())