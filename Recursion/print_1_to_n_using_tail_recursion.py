def print_1_to_n(n,i):

    if n == 0:
        return

    print(n - (n - i))
    print_1_to_n(n-1,i+1)
    


n = int(input())
i = 1
print(print_1_to_n(n,i))