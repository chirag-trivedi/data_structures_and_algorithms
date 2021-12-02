def sum_of_n(n):
    if n == 1:
        return n
    
    return n*(n+1)/2



n = int(input())
print(sum_of_n(n))