def leaders(arr):
    
    res = []
    length = len(arr)
    
    if length == 1:
        res.append(arr[0])
        return res
    
    res.append(arr[length-1])
    curr_leader = arr[length-1]
    
    for i in range(length-2,-1,-1):
        
        if arr[i] > curr_leader:
            res.append(arr[i])
            curr_leader = arr[i]
        
    return res
    
arr = [3,2,1]
print(leaders(arr))

# Time Complexity O(n)
# Space Complexity O(1)