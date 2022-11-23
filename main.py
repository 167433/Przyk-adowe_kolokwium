import datetime

class Court:
    __width: float = 68
    __lenght: float = 150
    __addres: str
    __year_bulit: int

    def __init__(self, width:float = 68, lenght:float = 150,* ,addres:str, year_bulit:int):

        if width>=45 and width<=90:
            self.__width = width
        else:
            self.__width = 68

        if lenght >= 90 and lenght <= 120:
            self.__lenght = lenght
        else:
            self.__lenght = 150

        self.__addres = addres
        self.__year_bulit = year_bulit

    def __str__(self):
        return f'Boisko wybudowane w roku {self.__year_bulit},' \
               f' o długości {self.__lenght} ' \
               f'metrów i szerokości {self.__width} metrów.\n' \
               f' Pole powierzchni: {self.area()} mkw.\n' \
               f' Adres: {self.__addres}\n”'

    def __eq__(self, other):
        if self.area() == other.area():
            return True
        return False

    def __ne__(self, other):
        if self.area() != other.area():
            return True
        return False


    def area(self):
        return self.__lenght*self.__width

    @staticmethod
    def validate(self):
        rok = datetime.date.today().year
        rok = int(rok)
        if int(self.__year_bulit) > rok or int(self.__year_bulit) < 0:
            self.__year_bulit = rok
        return self.__year_bulit


    @property
    def width_prop(self):
        return self.__width

    @width_prop.setter
    def width_prop(self, value):
        if (value >= 90) and (value <= 120):
            self.__width = value

    @width_prop.getter
    def width_prop(self):
        return f' {self.__width}'

    @property
    def lenght_prop(self):
        return self.__lenght

    @lenght_prop.setter
    def lenght_prop(self, value):
        if (value >= 90) and (value <= 120):
            self.__lenght = value

    @lenght_prop.getter
    def lenght_prop(self):
        return f'{self.__lenght}'

    @property
    def adres_prop(self):
        return self.__addres

    @adres_prop.setter
    def adres_prop(self, value):
        self.__addres = value

    @adres_prop.getter
    def adres_prop(self):
        return f'{self.__addres}'

    @property
    def year_bulit(self):
        return self.__year_bulit

    @year_bulit.setter
    def year_bulit(self, value):
        self.__year_bulit = value

    @year_bulit.getter
    def year_bulit(self):
        return f' {self.__year_bulit}'

kort = Court(width= 70, lenght= 110, addres="Adres", year_bulit=2005)
print(kort.area())
print(kort.validate(kort))


class Stadium(Court):
    name: str
    common_name: str
    capacity: int = 0

    def __init__(self, width:float, lenght: float,addres: str, year_bulit: int, name: str,common_name: str=None,* ,capacity: int):
        super().__init__(width=width, lenght=lenght, addres=addres, year_bulit=year_bulit)
        self.name = name
        self.common_name = common_name
        self.capacity = capacity

    def __str__(self):
        napis = ''
        string=[f'Boisko wybudowane w roku {self.year_bulit},o długości {self.width_prop} metrów i szerokości {self.lenght_prop} metrów.',
               f'Pole powierzchni: {self.area()} mkw.\n',
               f'Adres: {self.adres_prop}\n',
               f'Nazwa: {self.name}\n',
               f'Nazwa zwyczajowa: {self.common_name}\n',
               f'Pojemność stadionu: {self.capacity}']

        if self.common_name is None:
            string.pop(4)
            for linia in string:
                napis = napis+linia
            return napis

        for linia in string:
            napis = napis + linia
        return napis

    @property
    def name_prop(self):
        return self.name

    @name_prop.getter
    def name_prop(self):
        return f'{self.name}'

    @name_prop.setter
    def name_prop(self,value):
        if isinstance(value,str):
            self.name = value
        else:
            print("ŹLE TO MA BYĆ STRING!!!")

    @property
    def common_name_prop(self):
        return self.common_name

    @common_name_prop.getter
    def common_name_prop(self):
        return f'{self.common_name}'

    @common_name_prop.setter
    def common_name_prop(self,value):
        if isinstance(value,str):
            self.common_name = value
        else:
            print("Zły typ danych")

    @property
    def capacity_prop(self):
        return self.capacity

    @capacity_prop.getter
    def capacity_prop(self):
        return f'{self.capacity}'

    @capacity_prop.setter
    def capacity_prop(self,value):
        if isinstance(value,int) and value >= 0:
            self.capacity = value
        else:
            print("Nieprawidłowe dane")

stadion = Stadium(width=90,lenght=90,addres="Adres",year_bulit=2000,name="Nazwa",capacity=1005)
print(stadion)

