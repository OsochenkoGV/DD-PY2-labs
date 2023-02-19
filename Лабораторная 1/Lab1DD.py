from typing import Union

class note:
    def __init__(self, squareth: Union[int, float], length: Union[int, float]):
        self.squareth = None
        self.lenght = None
        self.init_squareth(squareth)  #Площадь
        self.init_lenght(length) #Число страниц
    def init_squth(self, squ: (int, float)):
        if not isinstance(squ, (int, float)):
            raise TypeError('Значение должно быть числом')
        if squ < 0:
            raise ValueError('Значение должно быть больше нуля')
        self.squareth = squ
    def init_lenght(self, leng: (int, float)):
        if not isinstance(leng, (int, float)):
            raise TypeError('Значение должно быть числом')
        if leng < 0:
            raise ValueError('Значение должно быть больше нуля')
        self.length = leng
    def sqr_note(self):
        print(f"{self.length * self.squareth} - толщина")
    def count_note(self):
        print(f'{(self.squareth/self.length)} - число страниц на единицу площади')

class auto:
    def __init__(self, price: Union[int, float], weight: Union[int, float]): # Класс Автомобиль
        self.price = None
        self.weight = None
        self.init_price(price) #Цена
        self.init_weight(weight) #Вес
    def init_price(self, pr: (int, float)):
        if not isinstance(pr, (int, float)):
            raise TypeError('Значение должно быть числом')
        if pr < 0:
            raise ValueError('Значение должно быть больше нуля')
        self.price = pr
    def init_weight(self, wei: (int, float)):
        if not isinstance(wei, (int, float)):
            raise TypeError('Значение должно быть числом')
        if wei < 0:
            raise ValueError('Объем должен быть больше нуля')
        self.weight = wei
    def wei_to_pr(self):
        print(f"{self.weight / self.price} - отношение массы к цене")
    def boost(self,power):
        print(f"{power / self.weight} -ускорение автомобиля ")
# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
note1 = note(100,20)
note1.count_note()
note1.sqr_note()
auto1 = auto(5000,3000)
auto1.wei_to_pr()
auto1.boost(3)
