# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('task5_1.txt', 'w+', encoding='utf-8') as f_obj:
    while True:
        text = input('Введите: ')
        if text == '':
            break
        f_obj.write(text + '\n')
#f_obj.close()

#print(f_obj.closed)
