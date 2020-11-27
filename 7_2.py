# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Close(ABC):
    def __init__(self, v_h):
        self.v_h = v_h

    @abstractmethod
    def textile(self):
        pass


class Coat(Close):

    @property
    def textile(self):
        return round((self.v_h / 6.5 + 0.5), 2)


class Suit(Close):

    @property
    def textile(self):
        return round(self.v_h * 2 + 0.3, 2)


coat = Coat(20)
suit = Suit(10)
print('На пальтишко: ', coat.textile)
print('На пиджачок: ', suit.textile)