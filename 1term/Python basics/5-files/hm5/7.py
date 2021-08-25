import json


try:
    with open('7.txt') as our_file:
        profit = {}
        average = 0
        for i in [our_str.split() for our_str in our_file]:
            profit[i[0]] = int(i[2]) - int(i[3])
            if int(i[2]) >= int(i[3]):
                print(f'The profit of {i[0]} is {int(i[2]) - int(i[3])}')
                average += int(i[2]) - int(i[3])
        average = round(average / len(profit), 2)
        print(f'The average profit of the companies is {average}')
        profit = list(profit)
        profit.append({'average_profit': average})
        with open('7out.txt', 'w') as out_file:
            json.dump(profit, out_file)
except IOError as err:
    print('File not found.', err)
except ValueError as err:
    print('Error of convertion.', err)
