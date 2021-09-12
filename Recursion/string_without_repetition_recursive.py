def pshelper(slate,arr):
    if len(arr) == 0:
        print(slate)

    else:

        for i in range(0,len(arr),1):
            pshelper(slate+arr[i],arr[:i]+arr[i+1:])



def printpermutations(arr):
    pshelper('',arr)

arr = ['a','b','c']
printpermutations(arr)

# Time Comp. O(n * n!)
# Space Comp. O(n)