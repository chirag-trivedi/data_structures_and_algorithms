

# 47. Permutations II

def permutations(arr):

    res = []

    

    def helper(arr,i,slate):
    
        if len(arr) == i:
            res.append(slate[:])
            return

        else:
            s = set()
            for pick in range(i,len(arr),1):
                if arr[pick] not in s:
                    s.add(arr[pick])
                    arr[pick] , arr[i] = arr[i], arr[pick]
                    slate.append(arr[i])
                    helper(arr,i+1,slate)
                    slate.pop()
                    arr[pick] , arr[i] = arr[i], arr[pick]
                    

    helper(arr,0,[])

    return res

arr = [1,1,2]
print(permutations(arr))

# Space Complex Aux Space O(n) 
# Time Complex O(n!*n)