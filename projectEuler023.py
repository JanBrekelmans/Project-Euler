# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

import functions

UPPER_BOUND = 28123 + 1

def compute():
    total = 0
    
    abundant_numbers = UPPER_BOUND * [0]
    
    for i in range(1,UPPER_BOUND):
        for j in range(2*i,UPPER_BOUND,i):
            abundant_numbers[j] += i
    
    abundant_numbers = [i for i in range(1,UPPER_BOUND) if abundant_numbers[i] > i]
    
    numbers = UPPER_BOUND * [0]
    
    for i in abundant_numbers:
        for j in abundant_numbers:
            if i + j < UPPER_BOUND:
                numbers[i+j] = i+j
            else:
                break
    
    total = 28123*(28123+1)//2 - sum(numbers)
    
    return str(total)
    
    
if __name__ == "__main__":
    print(compute())