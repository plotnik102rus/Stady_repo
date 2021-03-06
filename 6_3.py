#Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
#Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
#Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника
# (get_full_name)и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
#(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_w = income['wage']
        self._income_b = income['bonus']


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname} {self.position}'

    def get_total_income(self):
        return self._income_w + self._income_b

qwe = Position('Vik', 'Plotnikov', 'electrician', {'wage':10000, 'bonus': 5000})
print(qwe.get_full_name())
print(qwe.get_total_income())