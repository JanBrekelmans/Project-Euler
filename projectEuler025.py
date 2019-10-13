# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

import math
import functions

LIMIT = 1000

def compute():
    
    # Use that F_n~~ (phi^n)/sqrt(5)
    phi = .5*(1+math.sqrt(5))
    maximum = (LIMIT + 1) * math.log(10)/math.log(phi)
    maximum = math.ceil(maximum)
    
    array = functions.Fibonacci_array(maximum)
    
    total = [x for (x,i) in enumerate(array) if len(str(i)) == LIMIT]
    
    return str(total[0]+2)
    
if __name__ == "__main__":
    print(compute())