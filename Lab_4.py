import random as RANDOM

def L4_Z1():
    Lista_Zakupow = ["Jabłko", "Chleb", "Ser", "Masło"]

    print(f"Pierwszy: {Lista_Zakupow[0]}")
    print(f"Drugi: {Lista_Zakupow[1]}")
    Lista_Zakupow[2] = "Mleko"
    print(f"Przedostatni: {Lista_Zakupow[-2]}")
    print(f"Ostatni: {Lista_Zakupow[-1]}")

def L4_Z2():
    Zestaw_1 = []
    Zestaw_2 = []

    #* Podpunkt 1
    Dlugosc_Listy = int(input("Podaj Długość Listy #1: "))
    for x in range(Dlugosc_Listy):
        Zestaw_1.append(RANDOM.randint(1, 10))
    print(f"Zestaw #1: {Zestaw_1}")

    #* Podpunkt 2
    Dlugosc_Listy = int(input("Podaj Długość Listy #2: "))
    for x in range(Dlugosc_Listy):
        Zestaw_2.append(RANDOM.randint(5, 15))
    print(f"Zestaw #2: {Zestaw_2}")

    #* Podpunkt 3
    Liczba = int(input("Podaj Liczbę: "))
    if Liczba in Zestaw_1 and Liczba in Zestaw_2:
        print(f"Liczba {Liczba} występuje w obu listach")
    elif Liczba in Zestaw_1:
        print(f"Liczba {Liczba} występuje w zestawie #1")
    elif Liczba in Zestaw_2:
        print(f"Liczba {Liczba} występuje w zestawie #2")
    else:
        print(f"Liczba {Liczba} nie występuje w obu zestawach")
    
    #* Podpunkt 4
    Zestaw_1_2 = Zestaw_1 + Zestaw_2
    Zestaw_1_2.sort()
    print(f"Zestaw #3: {Zestaw_1_2}")

def L4_Z3():
    Zwierzeta = ["Kot", "Pies", "Ptak", "Krowa", "Ryba", "Lew"]
    Zwierzeta.sort()
    print(f"Zwierzęta: {Zwierzeta}")
    print(f"{Zwierzeta[0]} {Zwierzeta[-3]} {Zwierzeta[-2]} {Zwierzeta[-1]}")
    print(f"Ilość Zwierząt: {len(Zwierzeta)}")
    pass

def L4_Z4():
    Imiona = ["Kasia", "Tomek", "Jan", "Ola", "Jerzy", "Marek", "Piotr", "Zuzia", "Bartek", "Jacek"]
    print(f"0) Imiona: {Imiona}")

    #* Podpunkt 1
    Imiona[3] = "Janusz"
    print(f"1) Imiona: {Imiona}")

    #* Podpunkt 2
    Imiona.insert(4, "Inny Janusz")
    print(f"2) Imiona: {Imiona}")

    #* Podpunkt 3
    Imiona.pop(6)
    print(f"3) Imiona: {Imiona}")

    #* Podpunkt 4
    print(f"4) Imiona: {Imiona} (Brak Zmian)")

    #* Podpunkt 5
    Imiona.insert(0, input("Podaj Imię #1: "))
    Imiona.insert(1, input("Podaj Imię #2: "))
    Imiona.insert(2, input("Podaj Imię #3: "))
    print(f"5) Imiona: {Imiona}")

    #* Podpunkt 6
    Imiona.remove(input("Podaj Imię Do Usunięcia: "))
    print(f"6) Imiona: {Imiona}")

    #* Podpunkt 7
    Imiona[-1] = "Jakieś Inne Imie"
    print(f"7) Imiona: {Imiona}")

    #* Podpunkt 8
    print(f"{Imiona[0:3]} {Imiona[-3:]}")
    print(f"8) Imiona: {Imiona}")

    #* Podpunkt 9
    Podane_Imie = input("Podaj Imię Do Sprawdzenia: ")
    if Podane_Imie in Imiona:
        print(f"Imię {Podane_Imie} znajduje się w liście")
    else:
        print(f"Imię {Podane_Imie} nie znajduje się w liście")
    print(f"9) Imiona: {Imiona}")

    #* Podpunkt 10
    Imiona.sort()
    print(f"10) Imiona: {Imiona}")

    #* Podpunkt 11
    Imiona.sort(reverse=True)
    print(f"11) Imiona: {Imiona}")

    #* Podpunkt 12
    for x in range(round(len(Imiona) / 2), len(Imiona)):
        Imiona.pop()
    print(f"12) Imiona: {Imiona}\n\tIlość Imion: {len(Imiona)}")

def L4_Z5():
    Punkty = [] # Nie dawać tablic w jednej linijce bo nie działa, referencje???
    Punkty_Ponizej = []
    Punkty_Powyzej = []
    Max = Srednia = Ilosc_Ponizej = Ilosc_Powyzej = 0
    Min = 999 # Ewentualnie Pierwszy element listy
    for x in range(15):
        Punkty.append(RANDOM.randint(0, 50))
    print(f"{Punkty}")

    #* Podpunkt 1
    for x in range(len(Punkty)):
        if Min > Punkty[x]: # Nowe Min
            Min = Punkty[x]

        if Max < Punkty[x]: # Nowe Max
            Max = Punkty[x]
    print(f"Min: {Min}\nMax: {Max}")

    #* Podpunkt 2
    Konkretny_Punkt = int(input("Podaj Punkt Do Sprawdzenia: "))
    if Konkretny_Punkt in Punkty:
        print(f"Ilość pkt {Konkretny_Punkt} występuje w liście")
    else:
        print(f"Ilość pkt {Konkretny_Punkt} nie występuje w liście")

    #* Podpunkt 3
    for x in range(len(Punkty)):
        Srednia += Punkty[x]
    Srednia = Srednia / len(Punkty)
    print(f"Średnia Punktów Wynosi: {Srednia}")

    #* Podpunkt 4 i 5
    for x in range(len(Punkty)):
        if Punkty[x] < Srednia:
            Ilosc_Ponizej += 1
            Punkty_Ponizej.append(Punkty[x])
        if Punkty[x] > Srednia:
            Ilosc_Powyzej += 1
            Punkty_Powyzej.append(Punkty[x])
    print(f"Ilośc Pkt Powyżej Średniej: {Ilosc_Powyzej}\n\tTe Punkty: {Punkty_Powyzej}")
    print(f"Ilośc Pkt Poniżej Średniej: {Ilosc_Ponizej}\n\tTe Punkty: {Punkty_Ponizej}")

def L4_Z6():
    #TODO: Dokończyć
    pass

def L4_Z7():
    #TODO: Dokończyć
    pass

def L4_Z8():
    #TODO: Dokończyć
    pass
