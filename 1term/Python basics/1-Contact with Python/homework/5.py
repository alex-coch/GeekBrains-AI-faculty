# task 5
proceeds = int(input('Input proceeds: '))
expenses = int(input('Input expenses: '))
profit = proceeds - expenses
if profit <= 0:
    print('Losses', profit)
else:
    print('Profit -', profit)
    print(f"Profitability - {profit / proceeds:.3f}")
    amount = int(input('Input amount of employees: '))
    print(f'Profit per an employee: {profit / amount}')