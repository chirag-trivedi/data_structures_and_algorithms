#!/bin/python3

import math
import os
import random
import re
import sys


def minimum_coins(coins, value):
    # Write your code here


    table = [0 for i in range(value+1)]
    
    
    
    table[0] = 0
    
    
    
    for i in range(1,value+1,1):
        temp = float('inf')
        for j in coins:
            if i - j < 0:
                continue
            else:
                temp = min(table[i-j]+1,temp)
        
        table[i] = temp
        
                
    return table[value]


if __name__ == '__main__':
    n = int(input().strip())
    coins = []

    for _ in range(n):
        coins.append(int(input().strip()))
    
    value = int(input().strip())
    
    fptr = sys.stdout

    result = minimum_coins(coins, value)
    
    fptr.write(str(result))
    fptr.close()