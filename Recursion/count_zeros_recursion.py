def count_zeros(n):

    div_n = n // 10
    rem_n = n % 10

    if div_n < 10:
        if rem_n == 0:
            return 1
        else:
            return 0

    else:
        if rem_n == 0 :
            return 1 + count_zeros(div_n)
        else:
            return count_zeros(div_n)



n = int(input())
print(count_zeros(n))