

def left_rotate_by_d(arr,d):
    length = len(arr)
    
    if d == length:
        return arr
    
    if d > length:
        d = d - length
        
        
    def reverse_it(arr,start,end):
        while start < end:
            arr[start],arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    reverse_it(arr,0,d-1)
    reverse_it(arr,d,length-1)
    reverse_it(arr,0,length-1)
       
    return arr
        
    

arr = [1,2,3,4,5]
d = int(input())

print(left_rotate_by_d(arr,d))