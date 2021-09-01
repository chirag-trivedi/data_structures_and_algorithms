def number(s):

    if len(s) == 0:
      return 1


    smallOutput = number(s[1:])

    return 2 * smallOutput

print(number('xyz'))

# Time Complexity O(n)
# Space Complexity O(n)