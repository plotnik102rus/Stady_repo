number = int(input('Введите любое целое положительное число: '))
unsw = number%10
number = number//10
while number > 0:
    if number%10 > unsw:
        unsw = number%10
    number = number//10
print('Наибольшая цифра Вашего числа: ', unsw)
