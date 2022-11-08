"""
    08.11.2022

    float range:
        numpy -> arange() -> https://pynative.com/python-range-for-float-numbers/
"""

# Funkcje
def Zadanie_1():
    x = int(input("Podaj x: "))
    y = int(input("Podaj y: "))

    if x > y:
        print("x > y")
        x, y = y, x # To Jest Krotka

    print(f"#1: {x}")
    print(f"#2: {y}")

    for z in range(x, y+1):
        print(z, end=" ")

def Zadanie_2():
    x = -4
    #for y in range():
    while x <= 4:
        #print(f"x: {x}", end=" ")

        Wynik = (2 * x) ** 2 - 5 * x - 8
        #print(f"Wynik: {Wynik}")

        print(f"f({x}) = {Wynik}")

        #print(f"{Wynik}\t", end=" ")

        x += 0.5

def Zadanie_3():
    while True:
        Input = input("Podaj Liczbę Całkowitą: ")
        if not Input.isdigit():
            break

def Zadanie_4():
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

def Zadanie_5():
    n = int(input("Podaj n: "))
    x = 0
    Srednia = 0

    #for x in range(n):
    while x < n:
        Srednia += int(input(f"Student #{x+1} Podaj Ilosc Pkt: "))
        x += 1

    Srednia = Srednia / n

    print(f"Średnia Ilość Pkt: {Srednia}")

def Zadanie_Dodatkowe_2():
    """
    Dokończyć
    """
    Liczba_1 = input("Podaj #1: ")
    Liczba_2 = input("Podaj #2: ")
    Wynik = []

    # Sprawdzanie Dlugosci Liczb
    if len(Liczba_1) > len(Liczba_2):
        for x in range(len(Liczba_2), len(Liczba_1)):
            Liczba_2 = "0" + Liczba_2
    elif len(Liczba_1) < len(Liczba_2):
        for x in range(len(Liczba_1), len(Liczba_2)):
            Liczba_1 = "0" + Liczba_1

    # Przygotowanie Listy z Wynikiem
    for x in range(len(Liczba_1) + 1):
        Wynik.append(0)

    print(f"#1: {Liczba_1}")
    print(f"#2: {Liczba_2}")
    print(f"Wynik: {Wynik}")

    # Iteracja przez str od końca
    for x in range(0, len(Liczba_1)):
        Operacja = int(Liczba_1[len(Liczba_1) - 1 - x]) + int(Liczba_2[len(Liczba_1) - 1 - x])

        print(Liczba_1[len(Liczba_1) - 1 - x], end=" ")
        print(Liczba_2[len(Liczba_2) - 1 - x], end=" ")
        print(Operacja, end=" ")

        print(Operacja % 10, end=" ")
        Wynik[len(Wynik) - 1 - x] += Operacja % 10

        print(f"x={x}", end=" ")

        # Overflow
        if Operacja >= 10:
        #if Wynik[len(Wynik) - 1 - x] >= 10:
            print("Overflow", end=" ")

            #if Operacja == 10:
                #print("v2", end=" ")
                #Wynik[len(Wynik) - 1 - x] = 0

            #Wynik[len(Wynik) - 2 - x] += 1
            #Liczba_1[len(Liczba_1) - 2 - x] = str(int(Liczba_1[len(Liczba_1) - 2 - x]) + 1)
            Wynik[len(Wynik) - 2 - x] += 1

        # Sprawdzanie Czy Jest Wynik Obecny = 10
        if Wynik[len(Liczba_1) - 1 - x] == 10:
            print("=10=", end=" ")
            Wynik[len(Liczba_1) - 1 - x] = 0
            Wynik[len(Liczba_1) - 2 - x] += 1


        print("")

    print(Wynik)

if __name__ == "__main__":
    #Zadanie_1()
    #Zadanie_2()
    #Zadanie_3()
    #Zadanie_4()
    Zadanie_5()
    #Zadanie_Dodatkowe_2()
    pass