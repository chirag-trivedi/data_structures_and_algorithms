def print_n_to_1(n):

    if n == 1:
        print(n)
        return

    print(n)

    print_n_to_1(n-1)



n = int(input())
print_n_to_1(n)