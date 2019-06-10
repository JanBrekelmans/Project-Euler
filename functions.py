# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 15:58:30 2019

@author: 
    Jan Brekelmans
    j.j.w.c.brekelmans@gmail.com
"""

"""
Functions used for Project Euler solutions
"""

import numpy as np

# Test if the integer n is prime
def is_prime(n):
    if n == 1:
        return False
    elif n == 2 or n == 3:
        return True
    elif n%2 == 0:
        return False
    elif n%3 == 0:
        return False
    else:
        for i in range(5,int(n**.5) + 1,2):
            if n%i == 0:
                return False
        return True

# Get a list of the prime factors of n, according to their multiplicity
# Example: primeFactors(24)= [2,2,2,3]
def primeFactors(n):
    factors = []
    
    while n%2 == 0 and n > 1:
        factors.append(2)
        n = n//2
        
    while n%3 ==0 and n > 1:
        factors.append(3)
        n = n//3
        
    
    for i in range(3,n+1,2):
        if n < 1.5:
            break
        while n%i == 0:
            factors.append(i)
            n = n//i
            
            
    return factors

# Check if the number n is a palindrome
def is_palindrome(n):
    lst = [int(i) for i in str(n)]
    if lst == lst[::-1]:
        return True
    return False

# Compute the greatest common divisor of the integers x and y
def GCD(x,y):
    
    while y is not 0:
        x,y = y, x%y
    return x

# Compute the lowest common multiple of the integers x and y
def LCM(x,y):
    return x*y//GCD(x,y)

# Generate a list of the n first prime numbers
def prime_sieve(n):
    sieve = [True]*n
    
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((n-i*i-1)//(2*i)+1)
    return [2]+[i for i in range(3,n,2) if sieve[i]]

# Compute the number of divisors of integer n.
def number_of_divisors(n):
    primes = primeFactors(n)
    
    count = np.bincount(np.array(primes))
    count = count+1
    
    total = np.prod(count)
    
    return total

# Compute the Euler totient function of n, the number of integers 1<=k<=n 
# such that gcd(n,k)=1
def Euler_totient(n):
    factors = primeFactors(n)
    
    factors = set(factors)
    
    total = n
    
    for i in factors:
        total = total - total//i
    print(total)

# Compute the Collatz sequence chain of the integer n, which halts when it 
# reaches 1
def Collatz_sequence_chain(n):
    chain = [n]
    while n is not 1:
        if n%2 == 0:
            n = n//2
        else:
            n = 3*n+1
        chain.append(n)
    
    return chain

# Computes the next number in the Collatz sequence
def Collatz(n):
    if n == 1:
        return 1
    elif n%2 == 0:
        return n//2
    else:
        return 3*n+1

# Returns the number n in words, n<= 1000
def to_words(n):
    ones = ["zero","one", "two", "three", "four", "five", "six", "seven", "eight",\
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",\
            "fifteen", "sixteen", "seventeen", "eighteen","nineteen"]
    tens = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    
    if n < 20:
        return ones[n] + " "
    elif n < 100:
        return tens[n//10] + " " + ((to_words(n%10) + " ") if (n%10 is not 0) else "")
    elif n < 1000:
        return ones[n//100] + " hundred " + \
        (("and " + to_words(n%100)) if (n%100 is not 0) else "")
    elif n < 10000:
        return ones[n//1000] + " thousand " + \
        ((to_words(n%1000)) if (n%1000 is not 0) else "")

# Calculate the proper divisors of integer n
def proper_divisors(n):
    return [x for x in range(1,(n+1)//2+1) if n%x == 0 and n!=x]

# Calculate the divisors of integer n
def divisors(n):
    lst = proper_divisors(n)
    lst.append(n)
    return lst

# Check if the integer n is perfect.
def is_perfect(n):
    if n == sum(proper_divisors(n)):
        return True
    return False

# Check if the integer n is abundant.
def is_abundant(n):
    if n < sum(proper_divisors(n)):
        return True
    return False

# Check if the integer n is deficient.
def is_deficient(n):
    if n > sum(proper_divisors(n)):
        return True
    return False

# Compute the n-th Fibonacci number., F1 = 1, F2 = 1
# We use Fn = floor(phi^n / sqrt(5)  + 1)
# Only availabe for n such that F_n fits in a double
def Fibonacci_quick(n):
    phi = (1+5**.5)/2
    
    F = np.floor(phi**(n+1)/(5**.5)+1/2)
    
    return int(F)

# Compute the first n Fibonacci numbers, and returns the array of these values
def Fibonacci_array(n):
    numbers = [0]*n
    
    numbers[0] = 1
    numbers[1] = 2
    
    for i in range (n-2):
        numbers[i+2] = numbers[i] + numbers[i+1]
    
    return numbers

# Compute the index of the lowest Fibonacci number greater or equal to x
def Fibonnaci_ceil(x):
    phi = (1+5**.5)/2
    
    n = np.ceil(np.log(x*5**.5 + .5)/np.log(phi)) - 1
    
    return int(n)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        i = 1
        for j in range(1,n+1):
            i = i * j
    return i

def is_binary_palindrome(n):
    binary = bin(n)
    binary = str(binary)[2:]
    
    if binary == binary[::-1]:
        return True
    return False
