

from collections import deque

def bipartite(node_count, edge_start, edge_end):

    visited = [0 for i in range(0,node_count,1)]
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
                if visited[neighbor] == 0:
                    visited[neighbor] = 1
                    parent[neighbor] = node
                    q.append(neighbor)
                    
                else:
                    if neighbor != parent[node]:
                        return True
                                                                                                                                                                                                                                                                                                                                                                
        return False
        
     
    
      
    components = 0
        
    for v in range(0,node_count,1):
        if visited[v] == 0:
            components += 1
            if components > 1:
                return False
            if bfs(v,adjList):
                return False
                
    return True


                    
print(bipartite(4,[0,0,0],[1,2,3]))
    
    
    
    