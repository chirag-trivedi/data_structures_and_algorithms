def remove_dupes(arr):
    length = len(arr)
    
    if length == 1:
        return arr
    
    slow = 0
    fast = 1
    
    while fast < length:
        if arr[slow] != arr[fast]:
            slow = fast
            fast += 1
            
        elif arr[slow] == arr[fast]:
            del arr[fast]
            length -= 1
            print(arr)
            
    
    return arr
    
arr = [1,1,1,1,1,1]
remove_dupes(arr)