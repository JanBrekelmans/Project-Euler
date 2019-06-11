# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

NUMBER = 1000

def compute():
    
    total = 0
    
    for a in range(1,NUMBER):
        for b in range(a,NUMBER):
            c = NUMBER - a - b
            
            if a*a + b*b == c*c:
                if total < a*b*c:
                    total = a*b*c
    
            
    return str(total)
    
    
if __name__ == "__main__":
    print(compute())