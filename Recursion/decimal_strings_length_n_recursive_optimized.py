def dshelper(slate,n):
    if n == 0:
        print(slate)

    else:
        for i in range(0,10,1):
            dshelper(slate+str(i),n-1)

def dec_strings(n):

    dshelper("",n)



n = int(input())

dec_strings(n)