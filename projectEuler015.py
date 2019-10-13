# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

import functions

def compute():
    n = 40
    k = 20

    return str(functions.binomial(n,k))
    
    
if __name__ == "__main__":
    print(compute())