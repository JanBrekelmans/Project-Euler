# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

import functions

def compute():
    upper_bound = 100
    
    numbers = range(1,upper_bound+1)
    
    sum_of_squares = 0
    square_of_sum = 0
    
    for i in numbers:
        sum_of_squares += i*i
        square_of_sum += i
    
    square_of_sum *= square_of_sum
    
    return str(square_of_sum-sum_of_squares)
    
    
if __name__ == "__main__":
    print(compute())