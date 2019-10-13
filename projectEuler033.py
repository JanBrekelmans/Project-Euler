# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:52:08 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

import functions

def compute():
    total = 0
    
    dem = 1
    nom = 1
    
    for d in range(10,100):
        for n in range(10,d):
            
            n1 = n // 10
            n2 = n % 10
            
            d1 = d // 10
            d2 = d % 10
            
            if (n1 == d2 and d*n2 == n*d1) or (n2 ==d1 and d*n1 == n*d2):
                dem *= d
                nom *= n
                        
    total = dem // functions.GCD(dem,nom)            
    
    return str(total)
    
    
if __name__ == "__main__":
    print(compute())