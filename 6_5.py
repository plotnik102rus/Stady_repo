# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    title = 'канцелярская принадлежность'

    def draw(self):
        print('запуск отрисовки')


class Pen(Stationery):

    def draw(self):
        print('рисуем ручкой')


class Pencil(Stationery):

    def draw(self):
        print('рисуем карандашом')


class Handle(Stationery):

    def draw(self):
        print('Рисуем маркером')


a1 = Stationery()
a1.draw()
a2 = Pen()
a2.draw()
a3 = Pencil()
a3.draw()
a4 = Handle()
a4.draw()
