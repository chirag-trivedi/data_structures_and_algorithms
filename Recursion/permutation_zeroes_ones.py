'''
generate all variations of zeroes and ones of some length
N =3
000
001
010
011
100
101
110
111


'''

def permute(n,prefix=''):

    if n == 0:
        return

    if n == 1:
        prefix += '0'
        print(prefix)
        prefix = prefix[0:len(prefix)-1]
        prefix += '1'
        print(prefix)


    permute(n-1,prefix+'0')
    permute(n-1,prefix+'1')


n = int(input())
permute(n)


# time complexity O(2^n)
# space complexity O(n)