#!/bin/python3
#to find all the primes upto n 
# using segmented sieve
#which is the memory enhancement on 
# sieve of eratosthenes

import sys
import math

lar_prime_factor=0
t = int(input().strip())
no_to_hold_last_n=0
for a0 in range(t):
    n = int(input().strip())
    #keep dividing with 2 upto the point n is no more devisible by 2
    while n%2 == 0:
        lar_prime_factor = 2
        n //= 2
    #start from 3 and keep adding on 2 in i
    for i in range(3,int(math.sqrt(n))+1,2):
        #keep deviding with 3/5/7 utpo the sqrt(n)
        while n%i == 0:
            n //= i
            lar_prime_factor = i
    #no_to_hold_last n is greater than 2 then 
    #that is the largest prime factor 
    #otherwise it is 2
    print(max(n,lar_prime_factor))