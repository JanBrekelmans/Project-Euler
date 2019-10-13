# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

import functions

def compute():
    total = 2**1000
    
    total = str(total)
    
    total = sum([int(i) for i in total])
    
    return str(total)
    
    
if __name__ == "__main__":
    print(compute())