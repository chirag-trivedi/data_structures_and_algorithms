

def subsets(arr):
    res = []

    def helper(arr,i,slate):

        if i == len(slate):
            res.append(slate[:])
            return

        else:
            s = set()

            for pick in range(i,len(arr),1):
                if arr[pick] not in s:
                    s.add(arr[pick])
                    helper(arr,i+1,slate)

                    slate.append(arr[pick])
                    helper(arr,i+1,slate)
                    slate.pop()

    helper(arr,0,[])

    return res


arr = [1,2,2]
print(subsets(arr))