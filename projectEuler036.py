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
    
    for i in range(1,LIMIT):
        
        if functions.is_palindrome(i):
            if functions.is_binary_palindrome(i):
                total += i
        
            
    return str(total)
    
    
if __name__ == "__main__":
    print(compute())