#Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [9, 6, 5, 3, 3, 2]
print(my_list)
us_num = int(input('Введите число рейтинга: '))
my_list.append(us_num)
my_list.sort(reverse=True)
print(my_list)




