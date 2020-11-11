sec = int(input('Введите время в секундах: '))
minutes = round(sec / 60)
hours = round(sec / 3600)


result = (f' {hours} часов = {minutes} минут = {sec} секунд.')
print(result)
