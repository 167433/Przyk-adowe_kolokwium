from court import Court


class Stadium(Court):
    __name: str
    __common_name: str
    __capacity: int

    def __init__(self, width: float, length: float, address: str, year_built: int,
                 name: str, common_name: str = None, capacity: int = 0):
        super().__init__(width=width, length=length, address=address, year_built=year_built)
        self.__name = name
        self.__common_name = common_name
        if capacity < 0:
            self.__capacity = 0
        else:
            self.__capacity = capacity

    @property
    def name(self) -> str:
        return self.__name

    @name.getter
    def name(self) -> str:
        return f'{self.__name}'

    @name.setter
    def name(self, value: str) -> None:
        if type(value) != str:
            raise ValueError(" Wartosc jest zlego typu (nie jest napisem). ")
        self.__name = value

    @property
    def common_name(self) -> str:
        return self.__common_name

    @common_name.getter
    def common_name(self) -> str:
        return f'{self.__common_name}'

    @common_name.setter
    def common_name(self, value: str) -> None:
        if type(value) != str or value is not None:
            raise ValueError(" Wartosc jest zlego typu (nie jest napisem). ")
        self.__common_name = value

    @property
    def capacity(self) -> int:
        return self.capacity

    @capacity.getter
    def capacity(self) -> str:
        return f'{self.__capacity}'

    @capacity.setter
    def capacity(self, value: int) -> None:
        if type(value) != int or value < 0:
            raise ValueError(" Wartosc jest zlego typu (nie jest liczba calkowita dodatnia). ")
        self.__capacity = value

    def __eq__(self, other):
        if self.area() == other.area() and self.__capacity == other.__capacity:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.area() != other.area() or self.__capacity != other.__capacity:
            return True
        else:
            return False

    def __str__(self) -> str:
        string = f'Boisko wybudowane w roku {self.year_built}, o długosci ' \
                 f'{self.length} metrow i szerokosci {self.width} metrow.\n' \
                 f'Pole powierzchni: {self.area()} mkw.\n' \
                 f'Adres: {self.address}.\n' \
                 f'Nazwa: {self.name}\n.'
        if self.__common_name is not None:
            string += f'Nazwa zwyczajowa: {self.common_name}\n.'
        string += f'Pojemnosc stadionu: {self.capacity} osób.'

        return string
