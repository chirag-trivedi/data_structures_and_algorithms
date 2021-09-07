def bshelper(slate,n):
    if n == 0:
        print(slate)

    else:

        bshelper(slate+"0",n-1)
        bshelper(slate+"1",n-1)



def binarystrings(n):
    bshelper("",n)

n = int(input())

binarystrings(n)