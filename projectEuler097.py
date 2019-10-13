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


def compute():
    
    total = functions.square_and_multiply(2,7830457,10000000000)
    
    total = (28433*total + 1) % 10000000000
    
            
    return str(total)
    
    
if __name__ == "__main__":
    print(compute())