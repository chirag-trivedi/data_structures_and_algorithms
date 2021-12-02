def largest(arr):
        
    
    length = len(arr)
    
    idx = 0
    
    if length == 1:
        return arr[idx]
    
    for i in range(0,length,1):
        if arr[i] > arr[idx]:
            
            idx = i
            
    return idx

arr = [-3,-2,-5,-1,0,11,10,3,4]
print(largest(arr))

# Time Complexity O(n)
# Space Complexity O(1)