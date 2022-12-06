from court import Court
from stadium import Stadium

def main():
    # Sprawdzenie Court
    court_1: Court = Court(address="Sloneczna 10, 10-100 Olsztyn", year_built=1999)
    print(court_1)
    court_2: Court = Court(500, 500, address="Sloneczna 10, 10-100 Olsztyn", year_built=1999)
    print(court_2)
    court_3: Court = Court(50, 100, address="Sloneczna 10, 10-100 Olsztyn", year_built=1999)
    print(court_3)
    print(court_1.length)
    court_1.year_built = 1990
    print(court_1)
    print(court_1.area())
    court_1.year_built = 2030
    print(court_1)
    Court.validate(court_1)
    print(court_1)

    # Sprawdzenie Stadium
    stadium_1: Stadium = Stadium(width=50, length=100,address="Sloneczna 10, 10-100 Olsztyn", year_built=1999, name="Sloneczny stadion",
                                 common_name="Sloneczko", capacity=10000)
    print(stadium_1)
    stadium_2: Stadium = Stadium(width=50, length=100, address="Sloneczna 10, 10-100 Olsztyn", year_built=1999,
                                 name="Sloneczny stadion", capacity=10000)
    print(stadium_2)
    stadium_1.year_built = 2030
    print(stadium_1)
    Stadium.validate(stadium_1)
    print(stadium_1)
    if stadium_1 == stadium_2:
        print("Stadion 1 i 2 są takie same.")
    else:
        print("Stadion 1 i 2 są różne.")
    stadium_1.width = 50
    stadium_1.length = 100
    if stadium_1 == stadium_2:
        print("Stadion 1 i 2 są takie same.")
    else:
        print("Stadion 1 i 2 są różne.")
    if stadium_1 != stadium_2:
        print("Stadion 1 i 2 są różne.")
    else:
        print("Stadion 1 i 2 są takie same.")
    stadium_1.capacity = 500
    if stadium_1 == stadium_2:
        print("Stadion 1 i 2 są takie same.")
    else:
        print("Stadion 1 i 2 są różne.")


if __name__ == "__main__":
    main()