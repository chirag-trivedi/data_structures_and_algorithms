
# Complete the function below
# The function accepts an INTEGER node_count, two INTEGER_ARRAYs edge_start and edge_end as parameters and 
# is expected to return a BOOLEAN
from collections import deque

def is_it_a_tree(node_count, edge_start, edge_end):

    visited = [-1 for i in range(0,node_count,1)]
    parent = [-1 for i in range(0,node_count,1)]

    def buildadjList(node_count, edge_start, edge_end):
        adjList = [[] for i in range(0,node_count,1)]
        
        result = zip(edge_start,edge_end)
        for start,end in result:
            adjList[start].append(end)
            adjList[end].append(start)
            
        return adjList
        
    adjList = buildadjList(node_count, edge_start, edge_end)
        
    def bfs(source,adjList):
        
        q = deque()
        q.append(source)
        visited[source] = 1
        
        
        while len(q) > 0:
            node = q.popleft()
           
            
            for neighbor in adjList[node]:
                if visited[neighbor] == -1:
                    visited[neighbor] = 1
                    parent[neighbor] = node
                    q.append(neighbor)
                    
                else:
                    if neighbor != parent[node]:
                        return True
                        
        return False
        
     
    
      
    components = 0
        
    for v in range(0,node_count,1):
        if visited[v] == -1:
            components += 1
            if components > 1:
                return False
            if bfs(v,adjList):
                return False
                
    return True

'''
4 3
0 1
0 2
0 3

'''
                    
print(is_it_a_tree(4,[0,0,0,3],[1,2,3,0]))
    
    
    
    