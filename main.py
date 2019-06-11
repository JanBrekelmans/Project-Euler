# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:16:18 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

import importlib
import time

def main():
    starting_time = time.time()
    current_time = starting_time
    
    for (number,answer) in PROBLEMS.items():
        module = importlib.import_module("projectEuler{:03d}".format(number))
        ans = module.compute()
        
        print("Problem {:03d}, Answer {}".format(number,answer))
        if str(answer) != ans:
            raise Exception("Error in problem {:03d}: Answer computed not the same as given in PROBLEMS".format(number))
            
        print("This problem took: {} seconds\n".format(time.time()-current_time))
        
        current_time = time.time()
            
    print("Total time = ", time.time() - starting_time)


PROBLEMS = {
        1: "233168",
        2: "4613732",
        3: "6857",
        4: "906609",
        5: "232792560",
        6: "25164150",
        7: "104743",
        8: "23514624000",
        9: "31875000",
        10: "142913828922",
        11: "70600674"
        }

if __name__ == "__main__":
    main()