def subsethelper(slate,s):

    if len(s) == 0:
        print(slate)
    else:
        subsethelper(slate,s[1:])
        subsethelper(slate+s[0],s[1:])



def printsubsets(s):
    subsethelper("",s)

s = input()
printsubsets(s)