def lastIndex(arr,x):
    length = len(arr)

    if length == 0 :
        return -1


    smallArr = arr[1:]
    smallArrOutput = lastIndex(smallArr,x)

    if smallArrOutput != -1:
        return smallArrOutput + 1
    else:
        if arr[0] == x:
            return 0
        else:
            return -1


n=int(input())
arr=[int(ele) for ele in input().split()]
x=int(input())
ans=lastIndex(arr,x)
print(ans)