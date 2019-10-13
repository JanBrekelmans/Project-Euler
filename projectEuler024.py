# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""
from itertools import permutations

LIMIT = 1000000-1

def compute():
    
    perm = [''.join(p) for p in permutations('0123456789')]
    
    perm = sorted(perm)
    
    return perm[LIMIT]
    
    
    
if __name__ == "__main__":
    print(compute())