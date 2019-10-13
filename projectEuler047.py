# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""



UPPER_BOUND = 1000000
consec = 4

def compute():
    
    lst = [0]*(UPPER_BOUND)
    
    for i in range(2,len(lst)):
        
        if lst[i] == 0:
            for j in range(i,UPPER_BOUND,i):
                lst[j] += 1
    
    for i in range(1,UPPER_BOUND):
        temp = True
        
        for j in range(consec):
            if lst[i+j] != consec:
                temp = False
        
        if temp:
            total = i
            break
    
    return str(total)
    
            
    
    
if __name__ == "__main__":
    print(compute())