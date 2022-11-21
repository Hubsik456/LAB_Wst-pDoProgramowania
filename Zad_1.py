def Test():
    print("Hello World", end="-\n")

    # Podstawy
    x = 10
    print(f"x: {x}")
    print(f"x: {type(x)}")

    # RNG
    """
        help(random.radnomint)
        Dać do konsoli, ale trzeba to najpierw zaimportować
    """
    import random as RANDOM
    Los = RANDOM.randint(-1, 9)
    print(f"x: {Los}")

    # Input
    #y = int(input("Podaj y: "))
    #print(f"y: {y}")
    pass

def Zadanie_01():
    Zmienna = 2 + 1
    print(Zmienna, type(Zmienna))

    Zmienna = 1 + 4.5
    print(Zmienna, type(Zmienna))

    Zmienna_2 = 3 / 2
    print(Zmienna_2, type(Zmienna_2))

    Zmienna_3 = 4 / 2
    #Zmienna_4 = int(4 / 2)
    print(Zmienna_3, type(Zmienna_3))
    #print(Zmienna_4, type(Zmienna_4))

    Zmienna_3 = 3 // 2
    print(Zmienna_3, type(Zmienna_3)) # w dół

    Zmienna_3 = -3 // 2
    print(Zmienna_3, type(Zmienna_3))

    Zmienna_3 = 11 % 2
    print(Zmienna_3, type(Zmienna_3))

    Zmienna_3 = 2 ** 10
    print(Zmienna_3, type(Zmienna_3))

    Zmienna_3 = 8 ** (1/3)
    print(Zmienna_3, type(Zmienna_3))

def Zadanie_02():
    """
    Zmienne są wskaźnikami/referencjami
    """
    print(int(3.0))
    print(float(3))
    print(float("3"))
    print(str(12.4))
    print(bool(0))

def Zadanie_1():
    Bok_1 = int(input("Podaj Bok #1: "))
    Bok_2 = int(input("Podaj Bok #2: "))
    Obwod = Bok_1 + Bok_1 + Bok_2 + Bok_2
    Pole = Bok_1 * Bok_2
    print("Obwod:", Obwod, "Pole:", Pole)

def Zadanie_1_1():
    Bok_1 = int(input("Podaj Bok #1: "))
    Bok_2 = int(input("Podaj Bok #2: "))
    Obwod = Bok_1 + Bok_1 + Bok_2 + Bok_2
    Pole = Bok_1 * Bok_2
    print(f"Obwod: {Obwod}\nPole: {Pole}")

def Zadanie_2():
    Droga = int(input("Podaj Drogę: "))
    Srednie_Spalenie = int(input("Podaj Średnie Spalenie (na 100km): "))
    Przewidywane = Droga / 100 * Srednie_Spalenie
    Cena_Paliwa_Cala = Przewidywane * 6.5
    print(f"Przewidywane Spalenie: {Przewidywane}\nKoszt Paliwa: {Cena_Paliwa_Cala}")

Zadanie_2()