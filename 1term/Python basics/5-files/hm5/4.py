try:
    with open('4.txt') as our_file:
        with open('4out.txt', 'w') as out_file:
            average, amount = 0, 0
            rus_arr = ('Один', 'Два', 'Три', 'Четыре')
            for count in our_file:
                our_arr = count.replace('\n', '').split(' — ')
                out_file.write(f'{rus_arr[int(our_arr[1]) - 1]} - {our_arr[1]}\n')
except IOError:
    print('File not found')
except ValueError:
    print(f'Wrong number - {our_arr[1]}')
