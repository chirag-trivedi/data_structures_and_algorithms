def remove_dupes(s):

    length = len(s)

    if length == 0 or length == 1:
        return s

    if s[0] == s[1]:
        return remove_dupes(s[1:])
    else:
        return s[0] + remove_dupes(s[1:])



s = input()
print(remove_dupes(s))