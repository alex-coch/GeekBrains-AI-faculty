string = input('Input string: ').lower()
sum_substring = set(string[i:j].__hash__() for i in range(len(string)) for j in range(len(string), i, -1))
print(f'{len(sum_substring) -1} substring(s) in the string "{string}"')