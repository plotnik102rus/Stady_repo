#Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
month_list = [{1, 2, 12}, 'зима', {3, 4, 5}, 'весна', {6, 7, 8}, 'лето', {9, 10, 11}, 'осень']
data = int(input('Введите номер месяца: '))
for i in range(len(month_list)):
    if (type(month_list[i]) == set) and (data in month_list[i]):
        print(f'Ваш месяц относится к времени года:  {month_list[i +1]}')
        break

month_list = [(1, 2, 12), (3, 4, 5), (6, 7, 8), (9, 10, 11)]
month_dict = {month_list[0]: 'зима',   month_list[1]: 'весна',  month_list[2]: 'лето', month_list[3]: 'осень'}
data = int(input('Введите номер месяца: '))
for i in range(len(month_dict)):
    if data in month_list[i]:
        print(f'Ваш месяц относится к времени года:  {month_dict[month_list[i]]}')




