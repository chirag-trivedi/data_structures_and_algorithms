def fib(n,b1,b2):

    if n == 0:
        return b1

    else:
        return fib(n-1,b2,b1+b2)

    
print(fib(10,0,1))