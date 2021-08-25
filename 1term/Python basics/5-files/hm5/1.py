with open('1.txt', 'w') as our_file:
    while True:
        our_str = input('Enter your string (blank string - exit): ')
        if our_str == '':
            break
        else:
            our_file.write(our_str + '\n')
