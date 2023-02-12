class auto:
    """Автомобили"""
    def __init__(self, separation:str, mark: int, type: int):
        self.separation = separation
        self.mark = mark
        self.type = type
    def __str__(self):
        return f"Класс:{self.separation}. Марка:{self.mark}. Тип кузова:{self.type}"
    def __repr__(self):
        return f"{self.__class__.__separation__}(separation={self.separation!r}, mark={self.mark!r}, Тип кузова={self.type!r})"
class Cargo(auto):
    """Грузовые"""
    def __init__(self, separation: str, mark: int, Load_capacity: int, type: int):
        super().__init__(separation, mark, Load_capacity, type)
        if isinstance(Load_capacity, int):
            if Load_capacity < 0:
                self.Load_capacity = Load_capacity
            else:
                raise AttributeError("error number of Load_capacity")
        else:
            raise AttributeError("error number of Load_capacity")
    def __str__(self):
        return f"Класс - {self.separation}. Марка-{self.mark}. Грузоподъёмность-{self.Load_capacity}. Тип кузова-{self.type}"
    def __repr__(self):
        return f"{self.__class__.__separation__}(separation={self.separation!r}, mark={self.mark!r}, Грузоподъёмность={self.Load_capacity!r}, Тип кузова={self.type!r})"
class Passenger_cars(auto):
    """Легковые"""
    def __init__(self,separation:str, mark: int, type: int, price: int):
        super().__init__(separation, mark, type)
        if isinstance(price, int):
            if price == 0:
                self.price = price
            else:
                raise AttributeError("error quantity of price")
        else:
            raise AttributeError("error quantity of price")
    def __str__(self):
        return f"Класс-{self.separation}. Марка-{self.mark}. Тип кузова - {self.type}. Цена-{self.price}"
    def __repr__(self):
        return f"{self.__class__.__separation__}(separation={self.separation!r}, mark={self.mark!r}, Тип кузова={self.type!r}, price={self.price})"
auto1 = auto ('Автомобиль','Hunday','Седан')
print(auto1)
Cargo_ = Cargo('Грузовой','КАМАЗ',450, 'Самосвал')
print(Cargo_)
Passenger_car_ = Passenger_cars('Легковой','Лада' , 'Купэ' , 600000)
print(Passenger_car_)

