def helper(arr,si,ei,x):

    if si > ei:
        return -1

    mid = (si + ei)//2

    if arr[mid] == x:
        return mid

    elif arr[mid] < x:
        return helper(arr,mid+1,ei,x)
    elif arr[mid] > x:
        return helper(arr,si,mid-1,x)
    

def bin_search(arr,x):
    length = len(arr)
    if length == 0:
        return -1
    si = 0
    ei = length - 1
    return helper(arr,si,ei,x)

arr = [int(i) for i in input().split(" ")]
x = int(input())
print(bin_search(arr,x))