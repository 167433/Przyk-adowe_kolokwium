import datetime


class Court:
    _width: float = 68
    _lenght: float = 150
    _addres: str
    _year_bulit: int

    def __init__(self, width, lenght, addres, year_bulit):
        if (width >= 90) and (width <= 120):
            self._width = width

        if (lenght >= 45) and (lenght <= 90):
            self._lenght = lenght

        self._addres = addres
        self._year_bulit = year_bulit

    def area(self):
        return self._lenght * self._width


    def __str__(self):
        return f'Boisko wybudowane w roku {self._year_bulit},' \
               f' o długości {self._lenght}' \
               f' metrów i szerokości {self._width} metrów \n' \
               f'Pole powierzchni {self.area()} \n' \
               f'Adres: {self._addres}'

    def __eq__(self, other):
        if self.area() == other.area():
            return True
        return False

    def __ne__(self, other):
        if self.area() != other.area:
            return True
        return False

    @property
    def width_prop(self):
        return self._width

    @width_prop.setter
    def width_prop(self,value):
        if (value >= 90) and (value <= 120):
            self._width = value

    @width_prop.getter
    def width_prop(self):
        return f' {self._width}'

    @property
    def lenght_prop(self):
        return self._lenght

    @lenght_prop.setter
    def lenght_prop(self, value):
        if (value >= 90) and (value <= 120):
            self._lenght = value

    @lenght_prop.getter
    def lenght_prop(self):
        return f'{self._lenght}'

    @property
    def adres_prop(self):
        return self._addres

    @adres_prop.setter
    def adres_prop(self,value):
        self._addres = value

    @adres_prop.getter
    def adres_prop(self):
        return f'{self._addres}'

    @property
    def year_bulit(self):
        return self._year_bulit

    @year_bulit.setter
    def year_bulit(self,value):
        self._year_bulit = value

    @year_bulit.getter
    def year_bulit(self):
        return f' {self._year_bulit}'

    @staticmethod
    def validate(self):
        rok = datetime.date.today().year
        rok = int(rok)
        if int(self._year_bulit) > rok or int(self._year_bulit) < 0:
            self._year_bulit = rok

class Stadium(Court):
    name: str
    common_name: str
    capacity: int = 0

    def __init__(self,width: int, lenght: int, addres: str,
                 year_bulit: int, name: str, capacity: int, common_name: str = None):
        super().__init__(width, lenght, addres, year_bulit)
        self.name = name
        self.common_name = common_name
        self.capacity = capacity

    '''
    Czemu nie działa printowanie
    '''
    def __str__(self):
        if self.common_name == None:
            return f'Boisko wybudowane w roku {super().year_bulit}, o długości {super()._lenght}' \
                    f' metrów i szerokości {super()._width} metrów.\n'\
                    f'Pole powierzchni: {super().area()} mkw.\n'\
                    f'Adres: {super()._addres}\n'\
                    f'Nazwa: {self.name}\n'\
                    f'Pojemność stadionu: {self.capacity} osób.'

        return f'Boisko wybudowane w roku {self.year_bulit}, o długości {super()._lenght}' \
            f' metrów i szerokości {super()._width} metrów.\n'\
            f'Pole powierzchni: {super().area()} mkw.\n'\
            f'Adres: {super()._addres}\n'\
            f'Nazwa: {self.name}\n'\
            f'Nazwa zwyczajowa: {self.common_name}.'\
            f'Pojemność stadionu: {self.capacity} osób.'

    @property
    def name_prop(self):
        return self.name

    @name_prop.getter
    def name_prop(self):
        zablokuj = False
        if self.name is not str:
            zablokuj = True
            return self.name
    """
    (2pt) Zaimplementuj właściwości (propercje) setter i getter dla każdego atrybutu. 
    Jeśli dla getterów podane wartości argumentów nie spełniają założeń, 
    wartość atrybutu nie powinna się zmieniać i powinien zostać wypisany odpowiedni komunikat.
    
     Jeśli dla getterów ---- HUH ---- wartość atrybutu nie powinna się zmieniać --- NANI ---
    """


kort = Court(90, 150, "Tak", '2005')
kort2 = Court(100,150,"Nie","2000")
print(kort.year_bulit)
kort._year_bulit = '-2000'
kort.validate(kort)
print(kort.year_bulit)
print(datetime.date.today().year)
print(kort)
if kort == kort2:
    print("równe")
else:
    print("Nie równe")

if kort != kort2:
    print("Nie równe")
else:
    print("Równe")
print("---")
print(kort._addres)
print("---")

stadion = Stadium(100,120,"ADRES",2000,"Nazwa",1005,"Daje")
print(stadion._addres)
print(stadion)
# import datetime


# class Court:
#     width: float = 68
#     length: float = 150
#     address: str
#     year_built: int
#
#     def __init__(self, width: float, length: float, address: str, year_built: int) -> None:
#         if year_built < 2008:
#             if width >= 90 and width <= 120 and length >= 45 and length <= 90:
#                 self.length = length
#                 self.width = width
#                 self.__length = length
#                 self.__width = width
#         if year_built >= 2008:
#             self.__width = width
#             self.__length = length
#         self.address = address
#         self.year_built = year_built
#         self.__address = address
#         self.__year_built = year_built
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, value):
#         self.__width = value
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#     @property
#     def address(self):
#         return self.__address
#
#     @address.setter
#     def address(self, value):
#         self.__address = value
#
#     @property
#     def _year_built(self) -> int:
#         return self.__year_built
#
#     @_year_built.setter
#     def year_built(self, value):
#         self.__year_built = value
#
#     @staticmethod
#     def validate(cls):
#         if cls.year_built < 0:
#             cls.year_built = datetime.datetime.now().year
#         if cls.year_built > datetime.datetime.now().year:
#             cls.year_built = datetime.datetime.now().year
#
#     def area(self) -> float:
#         return self.width * self.length
#
#     def __get__(self, instance, owner):
#         return self.year_built
#
#     def __str__(self):
#         return f"Boisko wybudowane w roku {self.year_built}, o długości {self.length} metrów i szerokości " \
#                f"{self.width} metrów.\nPole powierzchni: {Court.area(self)} mkw.\nAdres: {self.address}"
#
#     def __eq__(self, other: 'Court'):
#         if Court.area(self) == other.area():
#             return True
#         else:
#             return False
#
#     def __ne__(self, other):
#         if Court.area(self) != other.area():
#             return True
#         else:
#             return False


# class Stadium(Court):
#     name: str
#     common_name: str = None
#     capacity: int
#
#     def __init__(self, width: float, length: float, address: str, year_built: int, name: str
#                  , capacity: int, common_name: str = None) -> None:
#         super().__init__(width, length, address, year_built)
#         self.name = name
#         self.common_name = common_name
#         if int(capacity) >= 0:
#             self.capacity = capacity
#
#     def __str__(self):
#         if self.common_name is None:
#             return f"{Court.__str__(self)}Nazwa: {self.name}\n" \
#                    f"Pojemność stadionu: {self.capacity}"
#         return f"{Court.__str__(self)}Nazwa: {self.name}\nNazwa zwyczajowa:" \
#                f" {self.common_name}\nPojemność stadionu: {self.capacity}"
#
#
# court_1 = Court(100, 50, "10, 10-100 Olsztyn", 1999)
# print(court_1)
# court_2 = Court(100, 50, "10, 10-100 Olsztyn", 1999)
# print(court_2)
# court_3 = Court(100, 50, "10, 10-100 Olsztyn", 1999)
# print(court_3)
# print(court_1.length)
# court_1.year_built = 1990
# print(court_1.year_built)
# court_1.year_built = 2030
# print(court_1.year_built)
# court_1.validate(court_1)
# print(court_1.year_built)