# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""


COINS = [1,2,5,10,20,50,100,200]
AMOUNT = 200 + 1

def compute():
    total = 0
    
    ways = AMOUNT * [0]
    
    ways[0] = 1
    
    for i in range(len(COINS)):
        for j in range(COINS[i],AMOUNT):
            ways[j] = ways[j] + ways[j-COINS[i]]
    
    total = ways[-1]
            
    return str(total)
    
    
if __name__ == "__main__":
    print(compute())