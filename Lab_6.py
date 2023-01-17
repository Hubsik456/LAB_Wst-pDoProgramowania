def Wejsciowka():
    Lista = []
    for x in range(6):
        Liczba = int(input(f"Podaj Liczbę #{x + 1}: "))

        if -20 <= Liczba <= 20:
            Lista.append(Liczba)

    print(f"Liczy z przedziału [-20, 20]: {Lista}")

def Zadanie_1(Imie = "Janusz", Wiek = 42):
    """
    Imie: Podane Imie
    Wiek: Podane Nazwisko
    Funkcja wyświetla podane dane na ekranie.
    """
    print(f"Imię: {Imie}\tWiek: {Wiek}")

def Zadanie_2(Liczba_1, Liczba_2):
    return Liczba_1+Liczba_2, Liczba_1-Liczba_2
    pass

def Zadanie_3():
    # Pominięte, za trudne
    pass

def Zadanie_4():
    # Pominięte, za trudne
    pass

# Zadanie 5 jest w "main"

def Zadanie_6(a, b = 0, c = 0):
    #a = int(input("Podaj a: "))
    #b = int(input("Podaj b: "))
    #c = int(input("Podaj c: "))

    #print(f"Wyrażenie: {a}x^2 + {b}x + {c}")

    Delta = b**2 - (4 * a * c)
    #print(f"Delta: {Delta}")

    Wynik = []

    if Delta > 0:
        Wynik.append((b*(-1) - math.sqrt(Delta)) / (2*a)) # lub -b
        Wynik.append((b*(-1) + math.sqrt(Delta)) / (2*a))
    elif Delta == 0:
        Wynik.append((b*(-1)) / (2*a))
    else:
        Wynik.append("Brak Rozwiązań.")

    return Wynik

def Zadanie_7(Input):
    return Input[::-1]

def Zadanie_8(Input):
    Slownik = {
        "Duze": 0,
        "Male": 0
    }

    for x in Input:
        if x in Slownik: # Jeśli litera się powtarza
            Slownik[x] = Slownik[x] + 1
        else:
            Slownik[x] = 0

        if x.isupper():
            Slownik["Duze"] += 1
        if x.islower():
            Slownik["Male"] += 1


    return Slownik

def Zadanie_10():
    Liczba = random.randint(1, 100)
    while True:
        Input = int(input("Podaj Liczbę z przedziału [1, 100]: "))
        if Input == Liczba:
            print("Podano Wylosowaną Liczbę.")
            break
        else:
            print("") # niedokończone
            pass
    pass

if __name__ == "__main__":
    import math
    import random
    #Zadanie_1("Janusz", 123); print(Zadanie_1.__doc__)

    #print(Zadanie_2(10, 20))
    #Wynik_Z2 = Zadanie_2(15, 24)
    #print(f"Dodawanie: {Wynik_Z2[0]}\tOdejmowanie: {Wynik_Z2[1]}")
    # lub
    #print(f"Dodawanie: {Zadanie_2(15, 24)[0]}\tOdejmowanie: {Zadanie_2(15,24)[1]}")

    # Zadanie 5
    def Dodawanie(Liczba_1, Liczba_2):
        return Liczba_1+Liczba_2
    def Odejmowanie(Liczba_1, Liczba_2):
        return Liczba_1-Liczba_2
    def Mnozenie(Liczba_1, Liczba_2):
        return Liczba_1*Liczba_2
    def Dzielenie(Liczba_1, Liczba_2):
        if Liczba_2 == 0:
            return "DZIELENIE PRZEZ 0!" # Lub None
        return Liczba_1/Liczba_2


    Slownik = {
        "+": Dodawanie,
        "-": Dodawanie,
        "*": Dodawanie,
        "/": Dodawanie,
    }

    if False:
        print(Slownik["+"](10, 20))
        print(Slownik["-"](10, 20))
        print(Slownik["*"](10, 20))
        print(Slownik["/"](10, 20))
        print(Slownik["/"](10, 0))

    Z6 = Zadanie_6(20, 1, 2)
    #print(Z6)

    Z6 = Zadanie_6(-1, -11, 12)
    #print(Z6)

    Z6 = Zadanie_6(1, 5, 6)
    #print(Z6)

    Z6 = Zadanie_6(1)
    #print(Z6)

    #print(Zadanie_7("123"))

    Z8 = Zadanie_8("abcAbde")
    print(f"Ilość Małych: {Z8['Male']}\nIlość Dużych: {Z8['Duze']}")
    print(Z8)

