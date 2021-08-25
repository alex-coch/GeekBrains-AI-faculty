try:
    with open('1.txt') as our_file:
        average, amount = 0, 0
        for count in our_file:
            if int(count.split()[1]) < 20000:
                print(count.split()[0])
            average += int(count.split()[1])
            amount += 1
        print(f'The average wage is {round(average / amount, 2)}')
except IOError:
    print('File not found')
except ValueError:
    print(f'Wrong salary - {count.split()[1]}')
