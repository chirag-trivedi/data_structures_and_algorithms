#!/bin/python3

import math
import os
import random
import re
import sys

sys.setrecursionlimit(10009)

from collections import deque

def course_schedule(n, prerequisites):
    # build graph
    adjList = [[] for _ in range(n)]
    for a,b in prerequisites:
        adjList[b].append(a)
    visited = [-1] * n
    departure = [-1] * n
    arrival = [-1] * n
    timestamp = 0
    sortedCourses = []
    #dfs
    def dfs(node):
        nonlocal timestamp
        arrival[node] = timestamp
        timestamp += 1
        visited[node] = 1
        for neighbor in adjList[node]:
            if visited[neighbor] == -1:
                if dfs(neighbor):
                    return True
            else:
                if departure[neighbor] == -1:
                    return True
        departure[node] = timestamp
        timestamp += 1
        sortedCourses.append(node)
        return False
        
    #outer loop
    for v in range(n):
        if visited[v] == -1:
            if dfs(v):
                return [-1]
    return reversed(sortedCourses)

if __name__ == '__main__':
    
    n = int(input().strip())
    e = int(input().strip())
    prerequisites_columns = 2

    prerequisites = []

    for _ in range(e):
        prerequisites.append(list(map(int, input().rstrip().split())))

    fptr = sys.stdout

    result = course_schedule(n, prerequisites)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()