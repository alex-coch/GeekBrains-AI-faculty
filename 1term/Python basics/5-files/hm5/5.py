with open('5.txt', 'w') as our_file:
    our_str = input('Enter your numbers via space: ')
    our_file.write(our_str)
    try:
        print(sum(map(int, our_str.split())))
    except ValueError:
        print('Wrong number')
