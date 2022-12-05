import random

"""
    22.11.2022

        lista składana
    lista = [for i in range(5)]
    lista = [random.randint(1,10) for i in range(x)]

    Kod z chatu
    1)
        for i in range(7,84,7):
            print(i, end=" ")
        print()
        for i in range(20,-1,-2):
            print(i,end=" ")
    2)
        import random
        lista = []
        x = int(input("podaj dlugosc listy: " ))
        for i in range(x):
            x2 = random.randint(1,10)
            lista.append(x2)
        print(lista)
    3)
    s = int(input("Podaj liczbe: "))
    if s in lista:
          print('Liczba z zestawu 1')
    elif s in lista2:
          print('Liczba z zestawu 2')
    else:
          print('Nie ma takiej liczby w obu zestawach')
    4)
        liczba=int(input("sprawdz sowja liczbe"))
        if liczba in zestaw_1 and liczba in zestaw_2:
            print("liczba jest w obu zestawach ")
    5)

"""

def Zadanie_Dodatkowe_3():
    x = 6
    y = 6
    Tablica = []

    Czy_Wpisac_Jeden = True

    # Tablica 2d
    for a in range(x):
        Tablica.append([])

        for b in range(y):
            Tablica[a].append(0)

    # Wypełnianie Tablicy
    for a in range(x):
        # Wiersz parzysty
        if y % 2 == 0 and a % 2 != 0:
            Czy_Wpisac_Jeden = False

        # Wypełnianie
        for b in range(y):
            if Czy_Wpisac_Jeden:
                Tablica[a][b] = 1
                Czy_Wpisac_Jeden = False
            else:
                Tablica[a][b] = 0
                Czy_Wpisac_Jeden = True

        # Wiersz parzysty
        if y % 2 == 0 and a % 2 != 0:
            Czy_Wpisac_Jeden = True

    # Wyświetlenie Tablicy
    for a in range(x):
        for b in range(y):
            print(Tablica[a][b], end=" ")
        print()

def Zadnie_3():
    zwierzeta = ["Kot", "Pies", "Lew", "Coś Innego"]
    pass

def Zadanie_4():
    zestaw_1 = []
    x = int(input("Podaj Długość Listy: "))

    for y in range(x+1):
        zestaw_1.push(random.randint(1, 10))

    print()

if __name__ == "__main__":
    Zadnie_3
    #Zadanie_Dodatkowe_3()
