#!/bin/python3

import sys

list_of_output=[]
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    n1=int((n-1)//3)
    n2=int((n-1)//5)
    n3=int((n-1)//15)
    sum_of_3=((n1*(n1+1))//2)*3
    sum_of_5=((n2*(n2+1))//2)*5
    sum_of_15=((n3*(n3+1))//2)*15
    list_of_output.append(int(sum_of_3+sum_of_5-sum_of_15))

for item in list_of_output:
    print(item)
