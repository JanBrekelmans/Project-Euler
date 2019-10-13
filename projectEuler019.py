# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

from datetime import *

def compute():
    counter = 0
    year = 1901
    month = 1
    
    curr_day = date(year,month,1)
    
    while curr_day.year < 2001:
        if curr_day.weekday() == 6:
            counter += 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
        
        curr_day = date(year,month,1)
            
    return str(counter)
    
    
if __name__ == "__main__":
    print(compute())