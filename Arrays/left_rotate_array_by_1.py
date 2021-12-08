def left_rotate_by_1(arr):
    
    length = len(arr)
    
    if length == 1:
        return arr
    
    i = 0
    
    while i < length-1:
        arr[i] , arr[i+1] = arr[i+1] , arr[i]
        i += 1
        
    return arr
    

arr = [1,2, 3]
print(left_rotate_by_1(arr))

# Time Complexity O(n)
# Space Complexity O(1)