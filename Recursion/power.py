def myPow(x: float, n: int):
        
        
    def helper(x,n):
            
        if n == 0:
            return 1
            
        return x * helper(x,n-1)


print(myPow(2,2))