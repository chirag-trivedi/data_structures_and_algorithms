def fact(n,i):
    
    if n == 0:
        
        return i

    i = i * n
    
    return fact(n-1,i)



n = int(input())

i = 1
print(fact(n,i))

#Time complex O(n)
#Space Complex O(n)

