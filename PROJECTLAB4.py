class Auto:
    """Родительский класс Автомобилей"""

    def __init__(self, name: str, price: int, body_type: str):
        self.name = name
        self.price = price
        self.body_type = body_type

    def __str__(self):
        return f"Название:{self.name}. Цена:{self.price}. Тип кузова:{self.body_type}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, price={self.price!r}, body_type={self.body_type!r})"

    def characteristic(self):
        print(f'Марка - {self.name}/ Цена - {self.price}/ Тип кузова - {self.body_type}')

class Cargo(Auto):
    """Дочерний класс Грузовых автомобилей"""

    def __init__(self, name: str, price: int, body_type: str, load_capacity: int):
        super().__init__(name, price, body_type)
        if isinstance(load_capacity, int):
            if load_capacity > 0:
                self.load_capacity = load_capacity
            else:
                raise AttributeError("Грузоподъёмность должна быть больше нуля")

    def __str__(self):
        return f"Название - {self.name}. Цена-{self.price}. Тип кузова-{self.body_type}. " \
               f"Грузоподъёмность{self.load_capacity}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, price={self.price!r}, body_type:{self.body_type!r}" \
               f", load capacity:{self.load_capacity!r})"

    def characteristic(self):
        print(f'Марка - {self.name}/ Цена - {self.price}/ Тип кузова: {self.body_type}/ '
              f'Грузоподъёмность: {self.load_capacity}')

class Passenger(Auto):
    """Дочерний класс легковых автомобилей"""

    def __init__(self, name: str, price: int, body_type: str, engine_capacity: int):
        super().__init__(name, price, body_type)
        if isinstance(engine_capacity, int):
            if engine_capacity > 0:
                self.engine_capacity = engine_capacity
            else:
                raise AttributeError("Объём двигателя неотрицателен")

    def __str__(self):
        return f"Название - {self.name}. Цена-{self.price}. Тип кузова-{self.body_type}. " \
               f"Объём двигателя-{self.engine_capacity}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, price={self.price!r}, body_type:{self.body_type!r}" \
               f", engine capacity={self.engine_capacity!r})"

    def characteristic(self):
        print(f'Марка - {self.name}/ Цена - {self.price}/ Тип кузова: {self.body_type}/ '
              f'Объём двигателя: {self.engine_capacity}')

auto1 = Auto('KIA', 1200000, 'Седан')
auto1.characteristic()
auto2 = Cargo('КамАЗ-5511 ', 520000, 'Самосвал', 10000)
auto2.characteristic()
auto3 = Passenger('Renault Logan', 345000, 'Купе', 1149)
auto3.characteristic()
