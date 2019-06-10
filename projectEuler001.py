# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:17:28 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

def compute():
    total = 0
    
    for i in range(1,1000):
        if i%3 == 0 or i%5 == 0:
            total += i
    
    return str(total)


if __name__ == "__main__":
    print(compute())