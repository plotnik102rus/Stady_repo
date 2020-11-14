#Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(x, y, z):
    num_1 = min(x, y, z)
    num_sum = (x+y+z) - num_1
    return num_sum


print(my_func(100, -1, -6))