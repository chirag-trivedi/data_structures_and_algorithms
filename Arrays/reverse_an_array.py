def reverse_array(arr):
    
    length = len(arr)
    
    if length == 1:
        return arr
    
    left = 0
    right = length - 1
    
    while left < right:
        arr[left] , arr[right] = arr[right] , arr[left]
        left += 1
        right -= 1
        
    return arr
    
arr = [-2,1,-1,0]

print(reverse_array(arr))

# Time Complexity O(n)
# Space Complexity O(1)
