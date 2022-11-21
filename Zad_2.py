# Funkcje
def Zadanie_pdf1_1():
    Bok_1 = int(input("Podaj a: "))
    Bok_2 = int(input("Podaj b: "))

    Pole = Bok_1 * Bok_2
    Obwod = Bok_1 + Bok_1 + Bok_2 + Bok_2

    print(f"Pole: {Pole}\nObwod: {Obwod}")

def Zadanie_pdf2_1():
    Wiek = int(input("Podaj Wiek: "))

    if Wiek < 4:
        print("Wstęp Bezpłatny")
    elif Wiek >= 4 and Wiek < 18:
        print("10zł")
    else:
        print("20zł")

def Zadanie_pdf2_2():
    Znak = input("Podaj Znak: ")

    if Znak.isupper():
       print(f"{Znak} - Duża Litera")
    else:
       print(f"{Znak} - Mała Litera")

def Zadanie_pdf2_3():
    print("Jaka Operacja:\n1) +\n2) -\n3) *\n4) /\n5) %")
    Operacja = int(input("Podaj Operacje: "))
    Arg_1 = int(input("Podaj Argument #1: "))
    Arg_2 = int(input("Podaj Argument #2: "))

    if Operacja == 1:
        print(f"{Arg_1} {Arg_2} = {Arg_1 + Arg_2}")
    elif Operacja == 2:
        print(f"{Arg_1} - {Arg_2} = {Arg_1 - Arg_2}")
    elif Operacja == 3:
        print(f"{Arg_1} * {Arg_2} = {Arg_1 * Arg_2}")
    elif Operacja == 4:
        if Arg_2 != 0:
            print(f"{Arg_1} / {Arg_2} = {Arg_1 / Arg_2}")
        else:
            print("DZIELENIE PRZEZ ZERO")
    elif Operacja == 5:
        if Arg_2:
            print(f"{Arg_1} ^ {Arg_2} = {Arg_1 ** Arg_2}")
        else:
            print("DZIELENIE PRZEZ ZERO")
    else:
        print("Zła Operacja")

def Zadanie_pdf2_4():
    Znak = input("Podaj Znak: ")

    if Znak.isupper():
        print(f"{Znak.lower()}")
    else:
        print(f"{Znak.upper()}")

def Zadanie_Dodatkowe_1():
    Liczba = int(input("Podaj Liczbę: "))
    pass

def WIP_1():
    Wiek = int(input("Podaj Wiek: "))

    if Wiek < 4:
        Cena = 0
    # elif Wiek >= 4 and Wiek <= 18: # Można sprawdzać tylko ten drugi warunek
    # Zadanie Dodatkowe Na Maila wysłać, tak w miarę przed północą
    elif Wiek <= 18:
        Cena = 10
    else:
        Cena = 20

    print(f"Cena Biletu: {Cena}zł")

    pass
def Zadanie_Dodatkowe_2():
    Parametry = []
    Temp = 1

    while True:
        Input = input(f"Podaj Parametr #{Temp}:")
        if Input.isdigit():
            Temp += 1
            Parametry.append(Input)
        else:
            print(f"Koniec")
            break

    print(f"{Parametry}")

"""
    skończone na kalkulatorze
    kart na następnych zajęciach
    Zadania Dodatkowe
        Wysłać mail, z linkiem do githuba
        zrobić jakieś nowe repozytorium, tylko z tym
"""

# Main
if __name__ == "__main__":
    pass
    Zadanie_Dodatkowe_2()
    #print("Hello World")
    #Zadanie_pdf2_1()


