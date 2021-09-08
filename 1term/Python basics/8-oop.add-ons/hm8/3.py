class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


arr = []
while True:
    num1 = input('Input your number (Enter - exit): ')
    if num1 == '':
        break
    else:
        try:
            if num1.isdigit():
                arr.append(num1)
            else:
                raise OwnError('You entered not a number')
        except OwnError as err:
            print(err)
print(f'Everything is okay - {arr}')
