def int_func(str1):
    return str1.capitalize()


our_str = input('Enter your string: ').split()
print(' '.join([int_func(i) for i in our_str]))

