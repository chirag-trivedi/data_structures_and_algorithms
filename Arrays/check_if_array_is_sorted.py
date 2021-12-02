def check_sorted(arr):
    
    length = len(arr)
    
    if length == 1:
        return True
    
        
    for i in range(1,length,1):
                
        if arr[i] < arr[i-1]:
            
            return False
        
    return True

arr = [1,-2,3]
print(check_sorted(arr))

# Time Complexity O(n)
# Space Complexity O(1)