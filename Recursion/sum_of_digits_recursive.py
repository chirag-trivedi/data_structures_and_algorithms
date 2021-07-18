def sum_of_digits(n):

    div_n = n // 10
    rem_n = n % 10

    if div_n < 10:
        return div_n + rem_n
    else:
        return rem_n + sum_of_digits(div_n)




n = int(input())
print(sum_of_digits(n))