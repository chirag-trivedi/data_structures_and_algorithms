



def permutations(arr):

    res = []

    def helper(arr,i,slate):
    
        if len(arr) == i:
            res.append(slate[:])
            return

        else:

            for pick in range(i,len(arr),1):

                arr[pick] , arr[i] = arr[i], arr[pick]
                slate.append(arr[i])
                helper(arr,i+1,slate)
                slate.pop()
                arr[pick] , arr[i] = arr[i], arr[pick]

    helper(arr,0,[])

    return res

arr = [1,2,3]
print(permutations(arr))