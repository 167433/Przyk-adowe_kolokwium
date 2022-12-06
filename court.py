from datetime import date


class Court:
    __width: float
    __length: float
    __address: str
    __year_built: int

    def __init__(self, width: float = 68, length: float = 150, *, address: str, year_built: int) -> None:
        if (width < 45 or width > 90) or (length < 90 or length > 120):
            self.__width = 68
            self.__length = 150
        else:
            self.__width = width
            self.__length = length
        self.__address = address
        self.__year_built = year_built

    @property
    def width(self) -> float:
        return self.__width

    @width.getter
    def width(self) -> str:
        return f'{self.__width}'

    @width.setter
    def width(self, value: float) -> None:
        if value < 45 or value > 90:
            raise ValueError(" Wymiar boiska nie miesci się w przedziale z przepisow z 2008 - [45, 90] ")
        self.__width = value

    @property
    def length(self) -> float:
        return self.__length

    @length.getter
    def length(self) -> str:
        return f'{self.__length}'

    @length.setter
    def length(self, value: float) -> None:
        if value < 90 or value > 120:
            raise ValueError(" Wymiar boiska nie miesci się w przedziale z przepisow z 2008 - [90, 120] ")
        self.__length = value

    @property
    def address(self) -> str:
        return self.__address

    @address.getter
    def address(self) -> str:
        return f'{self.__address}'

    @address.setter
    def address(self, value: str) -> None:
        self.__address = value

    @property
    def year_built(self) -> int:
        return self.__year_built

    @year_built.getter
    def year_built(self) -> str:
        return f'{self.__year_built}'

    @year_built.setter
    def year_built(self, value: int) -> None:
        self.__year_built = value

    def area(self) -> float:
        return self.__width * self.__length

    @staticmethod
    def validate(court):
        if court.__year_built > date.today().year or court.__year_built < 0:
            court.__year_built = date.today().year

    def __str__(self) -> str:
        return f'Boisko wybudowane w roku {self.__year_built}, o długosci ' \
               f'{self.__length} metrow i szerokosci {self.__width} metrow.\n' \
               f'Pole powierzchni: {self.area()} mkw.\n' \
               f'Adres: {self.__address}.'

    def __eq__(self, other):
        if self.area() == other.area():
            return True
        else:
            return False

    def __ne__(self, other):
        if self.area() != other.area():
            return True
        else:
            return False
