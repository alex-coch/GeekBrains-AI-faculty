# with open('3.txt', 'r', encoding='utf-8') as f:
#     employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
#     print(f'Average salary = {round(sum(employees_dict.values()) / len(employees_dict), 3)}\n'
#           f'Employees with salary less than 20k {[e[0] for e in employees_dict.items() if e[1] < 20000]}')


with open('3.txt', 'r', encoding='utf-8') as f:
    employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Average salary = {round(sum(employees_dict.values()) / len(employees_dict), 3)}\n'
          f'Employees with salary less than 20k {[e[0] for e in employees_dict.items() if e[1] < 20000]}')