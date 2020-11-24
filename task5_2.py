#2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('task5_2.txt.', 'r', encoding='utf-8') as f_obj:
    lines_1 = (f_obj.readlines())
    print(f'Файл содержит: {len(lines_1)}строк.')
    for str_num, lines in enumerate(lines_1, start=1):
        lines_2 = len(lines.split(' '))
        print(f' Cтрока {str_num}  содержит - {lines_2} слов')

    #print(len(lines_1))