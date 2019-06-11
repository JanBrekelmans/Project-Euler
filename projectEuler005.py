# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

import functions

def compute():
    numbers = range(1,21)
    
    answer = 1
    
    for i in numbers:
        answer = functions.LCM(answer,i)
    
    return str(answer)
    
    
if __name__ == "__main__":
    print(compute())