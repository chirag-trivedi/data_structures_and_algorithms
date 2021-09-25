def palindrome_check(s,start,end,checkOutput):
    if start > end:
        return checkOutput


    checkOutput = checkOutput and (s[0].lower() == s[-1].lower())

    return palindrome_check(s,start+1,end-1,checkOutput)


s = input()
start = 0
end = len(s) - 1
checkOutput = True
print(palindrome_check(s,start,end,checkOutput))

# Time Complexity O(n)
# Space Complexity O(n)