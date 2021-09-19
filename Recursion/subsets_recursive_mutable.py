

def subsets(arr):

    res = []


    def helper(arr,i,slate):
        if len(arr) == i:
            res.append(slate[:])
            return
            

        else:

            
            helper(arr,i+1,slate)

            slate.append(arr[i])
            helper(arr,i+1,slate)
            slate.pop()

    helper(arr,0,[])
    return res



arr = [1,2,3]

print(subsets(arr))