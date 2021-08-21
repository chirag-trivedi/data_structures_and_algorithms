def fib(n):
    table = [-1 for i in range(3)]

    table[0] = 0
    table[1] = 1
    mod_n = n % 3

    for i in range(2,n+1,1):
        mod_i = i % 3
        
        if mod_i == 0:
            temp = table[mod_i+1] + table[mod_i+2]
            table[0] = temp
        elif mod_i == 1:
            temp = table[mod_i-1] + table[mod_i+1]
            table[1] = temp
        elif mod_i == 2:
            temp = table[mod_i-2] + table[mod_i-1]
            table[2] = temp
    
    return table[mod_n]

print(fib(10))