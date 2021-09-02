class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

num1 = input('Input the first number: ')
num2 = input('Input the second number: ')
try:
    num1 = int(num1)
    num2 = int(num2)
    if num2 == 0:
        raise OwnError('The second number can\'t be zero')
except ValueError:
    print("You entered not a number")
except OwnError as err:
    print(err)
else:
    print(f'Everything is okay - {num1 / num2}')