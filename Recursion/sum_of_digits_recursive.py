def sum_of_digits(n,val):

    if n % 10 == n:
        return n + val

    n_mod = n % 10
    n_div = n // 10

    val = val + n_mod

    return sum_of_digits(n_div,val)
    



val = 0
n = int(input())
print(sum_of_digits(n,val))

# Time Complexity O(n)
# Space Complexity O(n)