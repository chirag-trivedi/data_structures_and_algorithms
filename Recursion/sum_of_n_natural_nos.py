def summation(n,i):
    if n == 0:
        return i
    

    i = i + n

    return summation(n-1,i)


n = int(input())
i = 0

print(summation(n,i))

# Time Complexity O(n)
# Space Complexity O(n)