try:
    with open('1.txt') as our_file:
        lines, words = 0, 0
        for count in our_file:
            words += len(count.split())
            lines += 1
        print(f'Lines - {lines}, words - {words}')
except IOError:
    print('File not found')
