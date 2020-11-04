first = int(input('Какое расстояние бегун пробежал в первый день? '))
target = int(input('Дистанция, которую нужно достигнуть? '))
days = 1
while first <= target:
    first = first * 0.1 + first
    days += 1
print(f'На {days} день бегун достигнет цели')