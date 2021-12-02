def second_largest(arr):
    
    length = len(arr)
    
    if length == 1:
        return -1
    
    max_val = float("-inf")
    second_max_val = float("-inf")
    
    for i in range(0,length,1):
        if arr[i] > max_val:
            second_max_val = max_val
            max_val = arr[i]
        elif arr[i] > second_max_val and arr[i] < max_val:
            second_max_val = arr[i]
    
    if max_val == second_max_val:
        return -1        
    return second_max_val

arr = [10,10,10,20,20,20]
print(second_largest(arr))

# Time Complexity O(n)
# Space Complexity O(1)