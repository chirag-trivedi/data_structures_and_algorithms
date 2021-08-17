# LC 207 https://leetcode.com/problems/course-schedule/

#!/bin/python3


import math
import os
import random
import re
import sys

sys.setrecursionlimit(100109)

from collections import deque

def can_be_completed(n, a, b):

    visited = [-1 for i in range(n)]
    arrival = [-1 for i in range(n)]
    departure = [-1 for i in range(n)]
    
    tstamp = 0

    def buildadjList(n,a,b):
            
        adjList = [[] for _ in range(n)]
        for i in range(len(a)):
            adjList[a[i]].append(b[i])
        
        
        return adjList
        
        
    def dfs(source,adjList):
        nonlocal tstamp
        
        arrival[source] = tstamp
        tstamp += 1
        
        visited[source] = 1
        
        for neighbor in adjList[source]:
            if visited[neighbor] == -1:
                if dfs(neighbor,adjList):
                    return True
            else:
                if departure[neighbor] == -1:
                    return True
           
        departure[source] = tstamp
        tstamp += 1 
        return False
        
    adjList = buildadjList(a,b)
    print(adjList)
    for v in range(0,n,1):
        if visited[v] == -1:
            if dfs(v,adjList):
                return False
            
    
    return True

if __name__ == '__main__':
    fptr = sys.stdout

    n, m = map(int, input().rstrip().split())

    a = [0] * m
    b = [0] * m

    for i in range(m):
        a[i], b[i] = map(int, input().rstrip().split())

    result = can_be_completed(n, a, b)

    fptr.write(str(int(result)) + '\n')

    fptr.close()
'''
4 4
1 0
1 2
3 1
0 3


'''