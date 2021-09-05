def binary_strings(n):
    if n == 0:
        return []

    if n == 1:
        return ["0","1"]

    smallOutput = binary_strings(n-1)

    result = []

    for s in smallOutput:
        result.append(s+"0")
        result.append(s+"1")


    return result

print(binary_strings(3))
