# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('task5_3.txt.', encoding='utf-8') as f_obj:
    incomes = []
    lines = f_obj.readlines()
    for line in lines:
        name, income = line.split(' ')
        incomes.append(int(income))
        if int(income) < 20000:
            print(line, end='')
    print('\nСредний доход:', sum(incomes) / len(incomes))
