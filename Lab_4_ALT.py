def L4_Z5_InnaWersja():
    """
    Zadanie 5. Utwórz listę punkty będącą listą punktów zdobytych z pewnego egzaminu przez grupę 15 studentów.
    Punkty niech będą liczbami rzeczywistymi z przedziału [0; 50]. Następnie
    • Wyświetl informację o największej i najmniejszej ilości zdobytych punktów
    • Wyświetl indeks pierwszego wystąpienia punktów podanych przez użytkownika. Jeżeli taka liczba
    punktów nie występuje na liście, wyświetl odpowiedni komunikat
    • Oblicz średnią punktów liczbę punktów z egzaminu
    • Oblicz, ile osób zdobyło punkty powyżej, a ile poniżej średniej
    • Wyświetl punkty poniżej średniej
    • Wyświetl punkty powyżej średniej

    lista składana doczytać co to jest
    """

    import random
    """
    Punkty = []
    for x in range(15):
        Punkty.append(round(random.uniform(0, 50), 2))
    """
    Punkty = [round(random.uniform(0, 50), 2) for x in range(15)]

    print(Punkty)

    Min = min(Punkty)
    Max = max(Punkty)
    print(f"Min: {Min}")
    print(f"Min: {Max}")

    Sprawdzana_Wartosc = float(input("Podaj wartość do sprawdznenia: "))
    if Sprawdzana_Wartosc in Punkty:
        print(f"Wartość {Sprawdzana_Wartosc} ma index {Punkty.index(Sprawdzana_Wartosc)}")
    else:
        print(f"Wartość {Sprawdzana_Wartosc} nie występuje w liscie")
        
    "To jest połowa zadania, robić potem gotowymi funkcjami sum()"

def L4_Z5_InniejszaWersja():
    import random as rand
    punkty = [round(rand.uniform(0, 50), 2) for x in range(15)]
    print(punkty)
    Min = min(punkty)
    Max = max(punkty)
    print(f'Min: {Min}')
    print(f'Max: {Max}')
    sp = float(input("Podaj wartość do sprawdzania: "))
    if sp in punkty:
        print(f'Wartość {sp} ma index {punkty.index(sp)}')
    else:
        print(f'Wartość {sp} nie wystempuje w liscie')
    suma = sum(punkty)
    ilosc = len(punkty)
    s_war = suma / ilosc
    print(f'Sriednia wartość punkyów {round(s_war, 2)}')
    mn = []
    we = []
    mn = [x for x in punkty if x<s_war] #TODO: Przykłady listy złożonej
    we = [x for x in punkty if x>s_war]
    #for x in punkty:
    #    if x < s_war:
    #        mn.append(x)
    #    else:
    #        we.append(x)
    print(mn, len(mn))
    print(we, len(we))

def L4_Z6():
    x = list(range(1, 11))
    print(x)
    print(x[-3:])
    x[:0] = x[-3:]
    x[-3:] = [] # Usunięcie

    #y = x
    #y = x[:] # Kopiowanie za pomocą wycinka
    y = list(x)

    print("Przed")
    print(x)
    print(y)

    y[0] = 99
    print("Po")
    print(y)
    print(y)
    #TODO: Dokończyć
    pass

def L4_ZD1():
    """
    Zrobić to pętlą???
    """
    Lista_1 = [1, 45, 3, 4, 5, 6]
    Lista_2 = [7, 7, 2, 4, 99, 6]
    Lista_3 = Lista_1 + Lista_2
    print(f"Lista_1: {Lista_1}")
    print(f"Lista_2: {Lista_2}")
    print(f"Lista_3: {Lista_3}")
    Lista_3.sort()
    print(f"Lista_3 Posortowana: {Lista_3}")

def L4_ZD2():
    Lista = []
    Rozmiar_Tablicy = 10

    for x in range(Rozmiar_Tablicy):
        Lista.append([])

    print(Lista)

    for x in range(len(Lista)):
        print(f"x: {x}")
        #for y in range(1):
        Lista[x].append(int(input("Podaj Liczbę: ")))
        #Lista[x].append(Liczba)
        Lista[x].append(Lista[x][0]**2)
            #print(Lista[x][y], end=" ")
        #print("")

    for x in range(len(Lista)):
        print(f"{Lista[x][0]}^2\t= {Lista[x][1]}")