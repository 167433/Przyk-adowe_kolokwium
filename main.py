import datetime


class Court:
    _width: float = 68
    _lenght: float = 150
    _addres: str
    _year_bulit: int

    def __init__(self, width, lenght, addres, year_bulit):
        if (width >= 45) and (width <= 90):
            self._width = width

        if (lenght >= 90) and (lenght <= 120):
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
        return self._year_bulit
    
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

    def __eq__(self, other):
        if self.area() == other.area() and self.capacity == other.capacity:
            return True
        return False

    def __ne__(self, other):
        if self.area() == other.area() and self.capacity == other.capacity:
            return False
        return True

    def __str__(self):
        if self.common_name == None:
            return f'Boisko wybudowane w roku {self.year_bulit}, o długości {self._lenght}' \
                   f' metrów i szerokości {self._width} metrów.\n' \
                   f'Pole powierzchni: {self.area()} mkw.\n' \
                   f'Adres: {self._addres}\n' \
                   f'Nazwa: {self.name}\n' \
                   f'Pojemność stadionu: {self.capacity} osób.'

        return f'Boisko wybudowane w roku {self.year_bulit}, o długości {self._lenght}' \
            f' metrów i szerokości {self._width} metrów.\n'\
            f'Pole powierzchni: {self.area()} mkw.\n'\
            f'Adres: {self._addres}\n'\
            f'Nazwa: {self.name}\n'\
            f'Nazwa zwyczajowa: {self.common_name}.\n'\
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
    3 (2pt) Zaimplementuj właściwości (propercje) setter i getter dla każdego atrybutu. 
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

stadion = Stadium(90,120,"ADRES",2000,"Nazwa",1005)
print(f' {stadion._width} {stadion._lenght} ')
stadion2 = Stadium(90,120,"Adres",2005,"Nazwa",1005)
print(f' {stadion2._width} {stadion2._lenght} ')
print(stadion._addres)
print(stadion)
print("---")
if stadion == stadion2:
    print("Tak")
else:
    print("Nie")

print(stadion.validate(stadion))
