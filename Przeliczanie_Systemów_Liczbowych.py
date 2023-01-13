"""
    WIP

    By Hubsik
    19.10.2022

    TODO:
    TODO:
        Placeholder dla Entry_3 (docelowe Systemy Liczbowe) -----> Trzeba zdarzeniami
        Obliczenia
        Ustawienia
        Pasek Menu Dokończyć
        Dać możliwość żeby jako docelowe systemy liczbowe dać jakiś przedział

        Dodać U1, U2, ZM, Bias, przecinki

    FIXME:
        Naprawić przedziały docelowych systemów liczbowych
            można podać tylko jeden przedział, MUSI być on ostatni bo inaczej następny elementy uznaje za STR
"""

#! Importy
import tkinter as GUI
import tkinter.ttk as GUI_2
#from tktooltip import ToolTip as TOOLTIP #https://pypi.org/project/tkinter-tooltip/
from functools import partial as PARTIAL
import webbrowser as WEBBROWSER
import re as RE

#! Zmienne
Wersja = "2.13"
Ustawienia = {
    #! Opcje z Menu
    "Duże Litery": True,
    "Wyświetlaj Obliczenia": False, #TODO:
    "Historia": False,
    "Duplikaty Dozwolone": False,
    "Sortowanie Docelowych": True,
    "Okno Na Wierzchu": False,

    #! Domyślne Wartości
    "Systemy_Liczbowe": [2,8,10,16],

    #! Specjalne; Nie Zmieniać
    "Specjalne Systemy Liczbowe": ["zm", "ZM", "u1" , "U1", "u2", "U2"], #TODO: Dodać Inne Systemy O Podstawach Innych Niż <int>
}
Czy_Dopisano_Separator = False

#! Debug Tools
def WIP_1():
    print("-=== WIP ===-")

def WIP_2(Tekst):
    print(f"-=== WIP_2: {Tekst} ===-")

#! Funkcje
def Link_Do_Strony(Link):
    WEBBROWSER.open(Link)

def Aktualizacja_Ustawien(Co_Zmienic):
    #print(f"Ustawienie: {Co_Zmienic} --> {Ustawienia[Co_Zmienic]} {type(Ustawienia[Co_Zmienic])}")
    #! Ogólne
    if Ustawienia[Co_Zmienic]:
        Ustawienia[Co_Zmienic] = False
    else:
        Ustawienia[Co_Zmienic] = True

    #! Specyficzne Ustawienia
    if Co_Zmienic == "Historia":
        for x in Treeview.get_children():
            Treeview.delete(x)
        
        if Entry_1.get() != "" and Entry_2.get() != "" and Entry_3.get() != "":
            Przeliczanie_Systemow_Liczbowych()

    elif Co_Zmienic == "Okno Na Wierzchu":
        Main_Window.attributes("-topmost", Ustawienia["Okno Na Wierzchu"])

def Przeliczanie_Systemow_Liczbowych(Event = None):
    #! Zmienne
    Liczby = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    if Ustawienia["Duże Litery"]:
        for x in range(10, len(Liczby)):
            Liczby[x] = Liczby[x].upper()

    #! Pola Tekstowe
    Input = Entry_1.get()
    System = Entry_2.get()
    Docelowe_Systemy = Entry_3.get()

    # Usunięcie Spacji
    Input = Input.replace(" ", "")
    System = System.replace(" ", "")
    Docelowe_Systemy = Docelowe_Systemy.replace(" ", "")

    try:
        System = int(System)
    except:
        System = ""

    try:
        Docelowe_Systemy = Docelowe_Systemy.replace(" ", "")
        #Docelowe_Systemy += ","
        Docelowe_Systemy = Docelowe_Systemy.split(",")

        for x in range(len(Docelowe_Systemy)):
            if Docelowe_Systemy[x] in Ustawienia["Specjalne Systemy Liczbowe"]:
                continue
            elif RE.match("^\d{1,}-\d{1,}$", Docelowe_Systemy[x]): # Przedział; https://regex101.com/r/qcd1iw/1
                WIP = Docelowe_Systemy[x].split("-")
                for y in range(len(WIP)): # STR --> INT
                    WIP[y] = int(WIP[y])

                print(f"WIP: {WIP}\tRANGE: {list(range(min(WIP), max(WIP)+1))}") #FIXME: Przedział MUSI być ostatni, i można podać tylko jeden przedział; następny element po przedziale interpretuje jako str

                for z in list(range(min(WIP), max(WIP)+1)):
                    Docelowe_Systemy.append(z)
                print(f"WIP: {Docelowe_Systemy[x]}")
                Docelowe_Systemy.remove(Docelowe_Systemy[x])
            else:
                Docelowe_Systemy[x] = int(Docelowe_Systemy[x])

        print(f"Docelowe: {Docelowe_Systemy}")
    except:
        print(f"Docelowe: {Docelowe_Systemy}")
        Docelowe_Systemy = "" # Podano coś co nie da się zamienić na liczbę, patrz: tekst

    #! Funkcje
    def Walidacja():
        #! Wyświetlenie Potencjalnych Błędów
        Wyswietl_Blad("", False)

        Poprawne_Dane = True
        Brak_Systemu = False
        Poprawny_System = False
        Poprawne_Docelowe = True

        if Ustawienia["Duże Litery"]:
            Input_Kopia = Input.upper()
        else:
            Input_Kopia = Input.lower()

        if Docelowe_Systemy == "": #? Jeśli W Ogóle Nie Podano Docelowe Systemy Liczbowe Lub Jeśli Podano Tekst
            Poprawne_Dane = False
            Poprawne_Docelowe = False
            Wyswietl_Blad("Docelowe Systemy Liczbowe Zawierają Tekst")

        if Poprawne_Docelowe: #? Czy Podano Poprawne Docelowe Systemy Liczbowe
            Zle_Systemy = []
            for x in range(len(Docelowe_Systemy)):
                if Docelowe_Systemy[x] in Ustawienia["Specjalne Systemy Liczbowe"]:
                    continue
                else:
                    #print(f"x: {Docelowe_Systemy[x]}")
                    if not (Docelowe_Systemy[x] >= 2 and Docelowe_Systemy[x] <= 34):
                        Zle_Systemy.append(Docelowe_Systemy[x])
            if len(Zle_Systemy) != 0:
                Poprawne_Dane = False
                Wyswietl_Blad(f"Podane Docelowe Systemy Liczbowe Zawiera Błędy\n\t{Zle_Systemy}")

            #print(f"Złe Docelowe: {Zle_Systemy} {len(Zle_Systemy)}")
            pass
            
        if System == "":  #? W Ogóle Podany System Liczbowy
            Poprawne_Dane = False
            Brak_Systemu = True  #Żeby Nie wyświetlać dwa razy tego samego błędu
            Wyswietl_Blad("Nie Podano Podstawy Systemu Liczbowego")
        if not Brak_Systemu: #? Poprawna Podstawa Systemu Liczbowego (Sprawdzane Jeśli W Ogóle Podano Podstawę)
            if System >= 2 and System <= 34:
                Poprawny_System = True
            else:
                Poprawne_Dane = False
                Wyswietl_Blad("Zła Podstawa Systemu Liczbowego\n\tPodstawa Musi Być z Zakresu <2 , 34>")
        if Input_Kopia == "": #? Czy W ogóle Podana Liczba
            Poprawne_Dane = False
            Wyswietl_Blad("Nie Podano Liczby")
        if Poprawny_System: #? Czy Input Zawiera Złe Cyfry (np. Czy liczba 123 (2) zawiera tylko "0" i "1")
            Zle_Znaki = []

            
            if Ustawienia["Duże Litery"]: # Zmiana Rozmiaru Liter
                #Input = Input.upper()
                pass
            else:
                #Input = Input.lower()
                pass
            
            for x in range(len(Input)):
                if not Input_Kopia[x] in Liczby[0:System]:
                    Zle_Znaki.append([Input[x], x+1])
                    Poprawne_Dane = False

            if len(Zle_Znaki) != 0:
                #print(f"Podana Liczba Zawiera Złe Cyfry\n\t{Zle_Znaki}")
                Wyswietl_Blad(f"Podana Liczba Zawiera Złe Cyfry\n\t{Zle_Znaki}")

        #! Jeśli Wszystkie Dane Są Poprawne
        if Poprawne_Dane:
            return True
        else:
            return False

    def Przeliczanie_Na_Sys10(Input, System):
        """
            Działa W Systemach Od 2-{Długość Alfbetu + 8}
            Przyjmnuje jako Input liczby albo tekst (pamiętać że np. 1a3 to jest string)

            TODO:
                Zrobić Żeby Caps Działał??? Przetestować
        """
        if System == 10:
            return Input
        else:
            Wynik = 0

            for x in range(len(str(Input))):
                if Ustawienia["Duże Litery"]:
                    Wynik += Liczby.index((str(Input)[x].upper())) * (System ** (len(str(Input)) - x - 1))  #Pierwsze x to liczby od początku (lewej) drugie x liczby od końca (prawej)
                    #print(f"{Liczby.index(str(Input)[x].upper)} * {System ** (len(str(Input)) - x-1)}")
                else:
                    Wynik += Liczby.index((str(Input)[x].lower())) * (System ** (len(str(Input)) - x - 1))  #Pierwsze x to liczby od początku (lewej) drugie x liczby od końca (prawej)
                    #print(f"{Liczby.index(str(Input)[x].lower())} * {System ** (len(str(Input)) - x-1)}")

            #print(f"Wynik: {Wynik}")
            return Wynik

    def Przeliczanie_Na_Inne_Systemy(Liczba, System):
        Wynik = ""

        if System in Ustawienia["Specjalne Systemy Liczbowe"]:
            return ["==- WIP -==", System]
        else:
            while True:
                if Liczba <= 0:
                    Wynik = Wynik[::-1]
                    break
                else:
                    #print(f"{Liczba} / {System} = {int(Liczba) // System} r {int(Liczba) % System}")
                    Wynik += str(Liczby[(int(Liczba) % System)])
                    Liczba = int(Liczba) // System

            #print(f"{Liczba} (10) == {Wynik} ({System})")
            return [Wynik, System]

    def Wyswietl_Tekst(Tekst=[], Tryb="Wyczyść"):
        if Tryb == "Wyczyść":
            if not Ustawienia["Historia"]:
                for x in Treeview.get_children():
                    Treeview.delete(x)
        elif Tryb == "Dodaj":
            if not Ustawienia["Historia"]: # Usunięcie Poprzednich Wyników
                for x in Treeview.get_children():
                    #Treeview.delete(x)
                    pass
            Treeview.insert("", GUI.END,values=(Tekst[0], Tekst[1]))

    def Wyswietl_Blad(Tekst="", Dopisz=True):
        if Dopisz:
            Obecny_Komunikat = Label_5.cget("text")
            Label_5.config(text=f"{Obecny_Komunikat}\n{Tekst}")
        else:
            Label_5.config(text=f"{Tekst}")

    #! Walidacja Danych
    if Walidacja():
        #! Ustawienia
        if Ustawienia["Duplikaty Dozwolone"]:
            Duplikaty = []
            for x in range(len(Docelowe_Systemy)):
                if Docelowe_Systemy[x] not in Duplikaty:
                    Duplikaty.append(Docelowe_Systemy[x])
            Docelowe_Systemy = Duplikaty

        if Ustawienia["Sortowanie Docelowych"]:
            Docelowe_Systemy.sort()
        
        #! Policzenie Na System 10 TODO: Żeby tego nie robiło kiedy od razu się poda liczbę w sys10
        System = int(System)
        Liczba = int(Przeliczanie_Na_Sys10(Input, System))
        #print(f"{Input} ({System}) == {Liczba} (10)")

        #! Przeliczenie z Systemu 10 Na Pozostałe
        if not Ustawienia["Historia"]: # Dopisanie Separatora
            Wyswietl_Tekst(Tryb="Wyczyść")

        for x in range(len(Docelowe_Systemy)):
            Wyswietl_Tekst(Przeliczanie_Na_Inne_Systemy(Liczba, Docelowe_Systemy[x]), "Dodaj")
            pass

        if Ustawienia["Historia"]: # Dopisanie Separatora
            Treeview.insert("", GUI.END,values=("---", "---"))
    else:
        #print("ERROR: Walidacja")
        Wyswietl_Tekst(Tryb="Wyczyść")

#! Main
if __name__ == "__main__":
    #! Start
    Main_Window = GUI.Tk()
    Main_Window.title("Przeliczanie Systemów Liczbowych")
    Main_Window.geometry("450x250+75+75")
    Main_Window.minsize(400, 175)

    #! Frames
    Frame_Top = GUI.Frame(Main_Window)
    Frame_Left = GUI.Frame(Main_Window)
    Frame_Right = GUI.Frame(Main_Window)
    Frame_Bottom = GUI.Frame(Main_Window)

    #! Lewo
    Label_1 = GUI.Label(Frame_Top, text="Zamiana Systemów Liczbowych")
    Label_1.grid(row=0, column=0)

    Label_2 = GUI.Label(Frame_Left, text="Liczba")
    Label_2.grid(row=0, column=0)

    Label_3 = GUI.Label(Frame_Left, text="System Liczbowy")
    Label_3.grid(row=0, column=1)

    Label_4 = GUI.Label(Frame_Right, text="Inne Systemy")
    Label_4.grid(row=0, column=0, columnspan=2)

    Entry_1 = GUI.Entry(Frame_Left)
    Entry_1.grid(row=1, column=0, sticky=GUI.EW)

    Entry_2 = GUI.Entry(Frame_Left)
    Entry_2.grid(row=1, column=1, sticky=GUI.EW)

    Label_6 = GUI.Label(Frame_Left, text="Docelowe Systemy Liczbowe")
    Label_6.grid(row=2, column=0, columnspan=2)

    Entry_3 = GUI.Entry(Frame_Left)
    Entry_3.grid(row=3, column=0, columnspan=2, sticky=GUI.EW)

    Button_1 = GUI.Button(Frame_Left, command=Przeliczanie_Systemow_Liczbowych, text="Policz")
    Button_1.grid(row=4, column=0, columnspan=2)

    Label_5 = GUI.Label(Frame_Left, text="", fg="red")
    Label_5.grid(row=5, column=0, columnspan=2)

    Label_7 = GUI.Label(Frame_Bottom, text="By Hubsik", fg="#595959")
    Label_7.grid(row=0, column=0)

    Treeview = GUI_2.Treeview(Frame_Right, columns=("Liczba", "System"), show="headings", height=10)
    Treeview.grid(row=1, column=0, sticky=GUI.NSEW)
    Treeview.column("Liczba", width=100)
    Treeview.heading("Liczba", text="Liczba")
    Treeview.column("System", width=50, stretch=False)
    Treeview.heading("System", text="System")

    #! Scrollbar
    Scrollbar = GUI_2.Scrollbar(Frame_Right, command=Treeview.yview)
    Scrollbar.grid(row=1, column=1, sticky=GUI.NS)
    Treeview.configure(yscrollcommand = Scrollbar.set)

    #! Frames
    Frame_Top.grid(row=0, column=0, columnspan=2)
    Frame_Left.grid(row=1, column=0, sticky=GUI.NS)
    Frame_Right.grid(row=1, column=1, sticky=GUI.NSEW)
    Frame_Bottom.grid(row=2, column=0, sticky=GUI.EW, columnspan=2)

    Main_Window.rowconfigure(Frame_Top, weight=0)
    Main_Window.rowconfigure(Frame_Left, weight=1)
    Main_Window.rowconfigure(Frame_Right, weight=1) #
    Main_Window.columnconfigure(Frame_Right, weight=1)
    Main_Window.rowconfigure(Frame_Bottom, weight=0)

    Frame_Right.rowconfigure(1, weight=1)
    Frame_Right.columnconfigure(0, weight=1)
    Frame_Right.columnconfigure(1, weight=0)

    #! Domyślne Wartości
    Entry_1.insert(GUI.END, "123")
    Entry_2.insert(GUI.END, "16")
    Temp_Tekst = f"{Ustawienia['Systemy_Liczbowe']}"
    Temp_Tekst = Temp_Tekst[1:len(Temp_Tekst)-1]
    Entry_3.insert(GUI.END, f"{Temp_Tekst}")

    #! Menu
        #? Zmienne
    M_Duze_Litery = GUI.BooleanVar(); M_Duze_Litery.set(Ustawienia["Duże Litery"])
    M_Historia = GUI.BooleanVar(); M_Historia.set(Ustawienia["Historia"])
    M_Duplikaty = GUI.BooleanVar(); M_Duplikaty.set(Ustawienia["Duplikaty Dozwolone"])
    M_Sortowanie = GUI.BooleanVar(); M_Sortowanie.set(Ustawienia["Sortowanie Docelowych"])
    M_Obliczenia = GUI.BooleanVar(); M_Obliczenia.set(Ustawienia["Wyświetlaj Obliczenia"])
    M_Wierzch = GUI.BooleanVar(); M_Obliczenia.set(Ustawienia["Okno Na Wierzchu"])
        #? Main
    Menu_Main = GUI.Menu(Main_Window)
    Main_Window.config(menu=Menu_Main)
        #? 1 - Plik
    Menu_File = GUI.Menu(Menu_Main, tearoff=False)
    Menu_File.add_command(label="By Hubsik", state=GUI.DISABLED, activebackground="#f0f0f0")
    Menu_File.add_command(label=f"v {Wersja}", state=GUI.DISABLED, activebackground="#f0f0f0")
    Menu_File.add_separator()
    Menu_File.add_command(label="Exit", command=Main_Window.destroy)
        #? 2 - Settings
    Menu_Settings = GUI.Menu(Menu_Main, tearoff=False)
    Menu_Settings.add_checkbutton(label="Duże Litery", onvalue=1, offvalue=0, variable=M_Duze_Litery, command=PARTIAL(Aktualizacja_Ustawien, "Duże Litery"))
    Menu_Settings.add_checkbutton(label="WIP | Historia", onvalue=1, offvalue=0, variable=M_Historia, command=PARTIAL(Aktualizacja_Ustawien, "Historia"))
    Menu_Settings.add_checkbutton(label="Dozwolone Duplikaty", onvalue=1, offvalue=0, variable=M_Duplikaty, command=PARTIAL(Aktualizacja_Ustawien, "Duplikaty Dozwolone"))
    Menu_Settings.add_checkbutton(label="Sortowanie", onvalue=1, offvalue=0, variable=M_Sortowanie, command=PARTIAL(Aktualizacja_Ustawien, "Sortowanie Docelowych"))
    Menu_Settings.add_checkbutton(label="WIP | Obliczenia", onvalue=1, offvalue=0, variable=M_Obliczenia, command=PARTIAL(Aktualizacja_Ustawien, "Wyświetlaj Obliczenia"), state="disabled")
    Menu_Settings.add_checkbutton(label="Okno Na Wierzchu", onvalue=1, offvalue=0, variable=M_Wierzch, command=PARTIAL(Aktualizacja_Ustawien, "Okno Na Wierzchu"))
        #? 3 - Linki
    Menu_Linki = GUI.Menu(Main_Window, tearoff=False)
    Menu_Linki.add_command(label="Kalkmat.org (Obliczenia, ZM, U1, U2, Ułamki)", command=PARTIAL(WEBBROWSER.open, "https://www.kalkmat.pl"))
    Menu_Linki.add_command(label="Naukowiec.org", command=PARTIAL(WEBBROWSER.open, "https://www.naukowiec.org/konwerter.html"))
    Menu_Linki.add_command(label="RapidTables.com (+ Kalkulator)", command=PARTIAL(WEBBROWSER.open, "https://www.rapidtables.com/convert/number/base-converter.html"))
    Menu_Linki.add_command(label="Tools4noobs.com", command=PARTIAL(WEBBROWSER.open, "https://www.tools4noobs.com/online_tools/base_convert/"))
    Menu_Linki.add_command(label="exploringbinary.com", command=PARTIAL(WEBBROWSER.open, "https://www.exploringbinary.com/floating-point-converter/"))
        #? End
    Menu_Main.add_cascade(label="Plik?", menu=Menu_File, underline=0)
    Menu_Main.add_cascade(label="Ustawienia", menu=Menu_Settings, underline=0)
    Menu_Main.add_cascade(label="Linki", menu=Menu_Linki, underline=0)

    #! Binds
    Main_Window.bind("<Return>", Przeliczanie_Systemow_Liczbowych)

    #! Tooltips
    #TOOLTIP(Entry_1, msg=f"Liczba\nZezwala na spację.\nRozróżnia Wielkość Ewentualnych Liter", delay=0.75)
    #TOOLTIP(Entry_2, msg="Podstawa Systemu Liczbowego\nZezwala na spację.\n<2; 34>", delay=0.75)
    #TOOLTIP(Entry_3, msg="Docelowe Systemy Liczbowe\nZezwala na spację.\nZezwala na podanie przedziału (tylko przedziału), np: 2-16.\n<2; 34>\nLiczby Oddzielane Przecinkami", delay=0.75)

    #! End
    Main_Window.mainloop()