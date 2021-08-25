#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countWaysToClimb function below.
def countWaysToClimb(steps, n):
    
    stairs = [0 for _ in range(n+1)]
    
    stairs[0] = 1
    
    for i in range(1,n+1):
        for j in steps:
            if i-j<0:
                continue
            else:
                stairs[i] += stairs[i-j]
    return stairs[n]



if __name__ == "__main__":
    fptr = sys.stdout

    steps_count = int(input())

    steps = []

    for _ in range(steps_count):
        steps_item = int(input())
        steps.append(steps_item)

    n = int(input())

    res = countWaysToClimb(steps, n)

    fptr.write(str(res) + '\n')

    fptr.close()