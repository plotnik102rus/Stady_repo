# #Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# # который должен принимать данные (список списков) для формирования матрицы.
# # Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# #Примеры матриц вы найдете в методичке.
# #Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# #Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# # Результатом сложения должна быть новая матрица.
# #Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# # с первым элементом первой строки второй матрицы и т.д.
#
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([' '.join([str(numb) for numb in line]) for line in self.matrix])

    def __add__(self, other):
        answer = ''
        if len(self.matrix) == len(other.matrix):
            for line_1, line_2 in zip(self.matrix, other.matrix):
                if len(line_1) != len(line_2):
                    return 'Problems with shape'

                summed_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ' '.join([str(i) for i in summed_line]) + '\n'
        else:
            return 'Problems with shape'
        return answer



matrix_1 = Matrix([[1, 2, 4], [3, 4, 4], [5, 6, 3], [7, 8, 9]])
matrix_2 = Matrix([[2, 3, 5], [4, 5, 5], [6, 7, 1], [10, 2, 11]])
print(matrix_1 + matrix_2)

