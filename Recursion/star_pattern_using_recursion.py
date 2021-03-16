# N=2
# *
# **
# *

# N=3
# *
# **
# ***
# **
# *


def star(N):
    if N == 1:
        return '*'

    smallOutput = star(N-1)

    print(smallOutput)

    return '*' + str(smallOutput)

def star_decrease(N):
    if N == 0:
        return

    print(N*'*')
    smallOutput = star_decrease(N-1)

    

N = int(input())
print(star(N))
star_decrease(N-1)

# time complexity O(N)
# space complexity O(N)