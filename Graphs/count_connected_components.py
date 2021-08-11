from collections import deque

def number_of_connected_components(n, edges):
    # Write your code here
    visited = [0 for i in range(0,n,1)]
    
    def buildadjList(n, edges):
    
        adjList = [[] for i in range(0,n,1)]
        
        for (src,dst) in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
            
        return adjList
        
        
    def bfs(source,adjList):
        
        
        q = deque()
        q.append(source)
        
        visited[source] = 1
        
        while len(q) > 0:
            node = q.popleft()
            
            for neighbor in adjList[node]:
                if visited[neighbor] == 0:
                    visited[neighbor] = 1
                    q.append(neighbor)
                    
                    
    def outer(n, edges, visited, adjList):
        components = 0
        for v in range(0,n,1):
            if visited[v] == 0:
                components += 1
                bfs(v,adjList)
           
        return components
        
    adjList = buildadjList(n, edges)
    return outer(n, edges, visited, adjList)
    
    
        