# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def my_func(name, surname, age, email, phone_number):
    print(f' Имя: {name}. Фамилия: {surname}. Возраст: {age}. Эл.почта: {email}. Телефон: {phone_number}.')


my_func(name=input('Введите имя: '),
        surname=input('Фамилия: '),
        age=input('Возраст: '),
        email=input('email: '),
        phone_number=input('Номер телефона: '))