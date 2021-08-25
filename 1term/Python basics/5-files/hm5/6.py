try:
    with open('6.txt') as our_file:
        our_arr = {}
        for our_str in our_file:
            hours = our_str[our_str.find(':')+1:].replace('—', '').replace(')', '(').replace(' ', '').split('(')
            our_arr[our_str[:our_str.find(':')]] = sum(int(i) for i in hours if i.isdigit())
        print(our_arr)
except IOError as err:
    print('File not found.', err)
except ValueError as err:
    print('Error of convertion.', err)
