gain = int(input('Введите выручку фирмы (руб): '))
cost = int(input('Введите издержки фирмы (руб): '))
if gain > cost:
    print(f'Вы работаете с прибылью, прибыль составляет:  {(gain / cost) * 100:.2f}''%')
elif gain < cost:
    print('Вы работаете в убыток')
elif gain == cost:
    print('Вы работаете в ноль')
slaves = int(input('Укажите количество сотрудников компании: '))
print('Прибыль фирмы в расчете на одного сотрудника (руб)', cost / slaves)