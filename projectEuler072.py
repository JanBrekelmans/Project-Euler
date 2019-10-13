# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 23:59:24 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

import functions
import math

UPPER_BOUND = 1000001

def compute():
    total = 0
    
    lst = [i for i in range(UPPER_BOUND)]
    
    for i in range(2,UPPER_BOUND):
        if lst[i] == i:
            for j in range(i,UPPER_BOUND,i):
                lst[j] = lst[j] - lst[j]//i
    
            
    return str(sum(lst)-1)
    
    
if __name__ == "__main__":
    print(compute())