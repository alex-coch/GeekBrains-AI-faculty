def in_out(str1):
    res = sum(map(int, str1.split()))
    print(res)
    return res


our_sum = 0
while True:
    our_str = input('Enter numbers using space (Q - exit) :')
    if our_str[0] == 'Q':
        break
    elif our_str[-1] == 'Q':
        our_sum += in_out(our_str[:-1])
        break
    else:
        our_sum += in_out(our_str)
print('Total :', our_sum)
