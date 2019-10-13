# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

import functions
import math

def compute():
    
    total = functions.convergent_e(100)
    
    den, num = functions.convergent_to_fraction(total)
    
    total = sum([int(x) for x in str(num)])
            
    return str(total)
    
    
if __name__ == "__main__":
    print(compute())