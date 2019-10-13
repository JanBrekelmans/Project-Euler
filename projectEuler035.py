# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

import functions

LIMIT = 1000000

def compute():
    total = 0
    
    primes = functions.prime_sieve(LIMIT)
    
    check = [False]*LIMIT
    
    for i in primes:
        check[i] = True
    
    for i in primes:
        string = str(i)
        
        length = len(string)
        
        score = 1
        
        for i in range(length):
            temp = ""
            for j in range(length):
                temp += string[(i+j)%length]
            
            if not check[int(temp)]:
                score = 0
                break
        
        total += score
    
    return str(total)
    
    
if __name__ == "__main__":
    print(compute())