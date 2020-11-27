# Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.

class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return 'Сумма клеток: ' + str(self.quantity + other.quantity)

    def __sub__(self, other):
        return 'Вычитание: ' + self.quantity - other.quantity if self.quantity + other.quantity > 0 \
            else 'разность количества ячеек двух клеток меньше нуля'

    def __mul__(self, other):
        return 'Число ячеек общей клетки: ' + str(self.quantity * other.quantity)

    def __truediv__(self, other):
        return 'Деление: ' + str(round(self.quantity / other.quantity))

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.quantity // rows)]) + '\n' + '*' * (self.quantity % rows)


cell_1 = Cell(50)
cell_2 = Cell(40)
print(cell_1)
print(cell_1 + cell_2)
print(cell_1 / cell_2)
print(cell_2.make_order(5))
