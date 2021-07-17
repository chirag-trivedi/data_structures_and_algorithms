def replace_s(s,char,replaced_char):

    length = len(s)

    if length == 0:
        return

    smallStr = s[1:]
    smallStrOutput = replace_s(smallStr,char,replaced_char)

    if s[0] == char:
        return replaced_char + str(smallStrOutput or '')
    else:
        return s[0] + str(smallStrOutput  or '')



s = input()
char = input()
replaced_char = input()
print(replace_s(s,char,replaced_char))
