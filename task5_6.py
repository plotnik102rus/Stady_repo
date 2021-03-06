#Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

my_dict = dict()
with open('task5_6.txt') as f_obj:
    lines_1 = f_obj.readlines()
    for line in lines_1:
        broken_line = line.split()
        subject = broken_line[0]
        sum_less = sum([int(x[:x.find('(')]) for x in broken_line[1:] if '(' in x])
        my_dict[subject[:-1]] = sum_less
print(my_dict)