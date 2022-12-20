"""
    Data: WIP 
    TODO: Przekopiowane z innego pliku, przerobić potem
"""
def L3_Z1():
    x = int(input("Podaj x: "))
    y = int(input("Podaj y: "))

    if x > y:
        print("x > y")
        x, y = y, x # To Jest Krotka

    print(f"#1: {x}")
    print(f"#2: {y}")

    for z in range(x, y+1):
        print(z, end=" ")

def L3_Z2():
    x = -4
    while x <= 4:
        Wynik = (2 * x) ** 2 - 5 * x - 8
        print(f"f({x}) = {Wynik}")
        x += 0.5

def L3_Z3():
    while True:
        Input = input("Podaj Liczbę Całkowitą: ")
        if not Input.isdigit():
            break

def L3_Z4():
    x = int(input("Podaj x: "))
    y = int(input("Podaj y: "))

    if x > y:
        print("x > y")
        x, y = y, x  # To Jest Krotka

    print(f"#1: {x}")
    print(f"#2: {y}")

    for z in range(x, y + 1):
        if z % 2 == 0:
            print(z, end=" ")
        else:
            continue

def L3_Z5():
    n = int(input("Podaj n: "))
    x = 0
    Srednia = 0

    while x < n:
        Srednia += int(input(f"Student #{x+1} Podaj Ilosc Pkt: "))
        x += 1

    Srednia = Srednia / n

    print(f"Średnia Ilość Pkt: {Srednia}")

def L3_Z6():
    n = int(input("Podaj n: "))
    x = 0
    Srednia = 0

    while True:
        if not x < n:
            break

        Ilosc_Pkt = int(input(f"Student #{x+1} Podaj Ilosc Pkt: "))
        x += 1
        if not 0 < Ilosc_Pkt < 100:
            continue
        Srednia += Ilosc_Pkt

        

    Srednia = Srednia / n

    print(f"Średnia Ilość Pkt: {Srednia}")

    #TODO: Dokończyć
    pass

def L3_Z7():
    print("Pętla: 1")
    for x in range(1, 101):
        print(f"{x}", end=" ")

    print("\nPętla: 2")
    for x in range(100, -1, -1):
        print(f"{x}", end=" ")

    print("\nPętla: 3")
    for x in range(7, 78, 7):
        print(f"{x}", end=" ")

    print("\nPętla: 4")
    for x in range(20, -1, -2):
        print(f"{x}", end=" ")

def L3_Z8():
    Ilosc = int(input("Podaj Ilość gwiazdek: "))

    for x in range(Ilosc):
        print("*" * Ilosc)

def L3_Z9():
    Ilosc = int(input("Podaj Ilość gwiazdek: "))

    for x in range(Ilosc):
        print("*" * (x+1))

    #TODO: Dokończyć Zrobić Wersję Trudniejszą

def L3_ZD1():
    #TODO: Dokończyć
    pass

def L3_ZD2():
    #TODO: Dokończyć
    pass