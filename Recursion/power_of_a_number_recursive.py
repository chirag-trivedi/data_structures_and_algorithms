def power(n,k):

    if k == 0:
        return 1

    smallOutput = power(n,k-1)

    return n * smallOutput

print(power(3,3))