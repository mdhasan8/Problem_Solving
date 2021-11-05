# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 10:54:58 2021

@author: Easin
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'primeCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#
list1 = []
list2 = []
for val in range(1000000+1):
    list1.append(0)
    var1 = 1

for elem in range(2,len(list1)):
    flag = True
    if list1[elem] ==0:
        list2.append(elem)
        for elem1 in range(len(list1)):
            if elem*elem1 > 1000000:
                break
            list1[elem*elem1] = 1
#print(list2)

def primeCount(n):
    count = 0
    var1 = 1
    for elem2 in range(len(list2)):
        count += 1
        var1 = var1 * list2[elem2]
        if var1 > n:
            return elem2 
            break
    return count 

print(primeCount(500))



'''
Leonardo loves primes and created  queries where each query takes the form of an integer, . For each , count the maximum number of distinct prime factors of any number in the inclusive range .

Note: Recall that a prime number is only divisible by  and itself, and  is not a prime number.

Example

The maximum number of distinct prime factors for values less than or equal to  is . One value with  distinct prime factors is . Another is .

Function Description

Complete the primeCount function in the editor below.

primeCount has the following parameters:

int n: the inclusive limit of the range to check
Returns

int: the maximum number of distinct prime factors of any number in the inclusive range .
Input Format

The first line contains an integer, , the number of queries.
Each of the next  lines contains a single integer, .

Constraints

Sample Input

6
1
2
3
500
5000
10000000000
Sample Output

0
1
1
4
5
10
Explanation

 is not prime and its only factor is itself.
 has  prime factor, .
The number  has  prime factor, ,  has  and  has  prime factors.
The product of the first four primes is . While higher value primes may be a factor of some numbers, there will never be more than  distinct prime factors for a number in this range.
'''