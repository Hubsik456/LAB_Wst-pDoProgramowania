"""
    I dont like Windows Sticky Notes so I made my own (which will be even worse, somehow)

    Hubsik

    ??? TODO:
        Przerobić całość na grid a nie że raz pack a raz grid
        Obsługa metadanych .txt
        Dodać Jakiś Kosz czy coś
        Walidacja ustawień z pliku .dzb
        Zamknięcie wszystkich okienek na raz
        Do licznika notatek w rogu, dodać ilość niezapisanych jeszcze notatek
        W settings dodać jakąś dodatkowy klucz z tablicą 2d [nazwa_opcji, poprawny_typ_zmiennej] ??? ---> Wywalić Guess_Var_Type(), albo chociaż przeczytać coś o .isdigit() i podobnych
        Dopracować komunikat o tym że aplikacja jest już otwarta (Jakaś instrukcja jeśli jest to false positive)
    ??? FIXME:
        Dowiedzieć się jak dodawać inne pliki w pyinstaller
            Żeby działało .exe usunąć wszystko co wymaga jakiś zewnętrznych plików (np. tktooltip czy grafiki)
            Ikony na pasku (i żeby w .exe działały)
        "Reload Settings" nie zmienia kolorów w treeview; Zmienić jakoś check_settings(load) żeby od razu ustawiało ustawienia typu resize, on top, kolorki, ilość notatek wyświetlanych (???)
        Jeśli użyje się Settings[np "123"] to pierwszy raz wywali program, drugi się nie uruchomii bo przy poprzednim razie nie poprawiło pliku DzbanPad_InUse.dzb
        Menu/Save nie usuwa *
        Menu/Delete nie usuwa X
"""

#! Imports
import functools as FUNCTOOLS
import tkinter as GUI
from tkinter import ttk as GUI_2
from tkinter import messagebox as MESSAGEBOX
from tkinter import scrolledtext as SCROLLEDTEXT
#from tktooltip import ToolTip as TOOLTIPS #https://pypi.org/project/tkinter-tooltip/
import os as OS
import subprocess as SUBPROCESS
from sys import exit as EXIT
from tkinter.filedialog import asksaveasfilename as ASKSAVEASFILENAME

#! Variables
    # About
DzbanPad_Version = "2.0"
Date_Creation = "10.05.2022" # d-m-y
Date_LastUpdate = "30.11.2022"  # d-m-y
    # Int
Amount_Of_All_Notes = 0
Amount_Of_Notes_Opened = 0
    # Arrays
List_Of_Opened_Notes = []
Supported_File_Formats = []
All_Styles = [
        #! Legend
        #["Color Scheme Name",      "TextBox Color",    "TextBox Background",   "TextBox Pointer",      "UI Foreground",    "UI Background"]
        # ---                       ---                 ---                     ---                     ---                 ---
        #* Light & Dark
        ["White",                   "Black",            "White",                "Black",                "Black",            "#f0f0f0"],
        ["Black",                   "White",            "#1a1a1a",              "White",                "White",            "Black"],
        ["Gray",                    "White",            "#404040",              "Black",                "White",            "#595959"],

        #* Colorful
        ["Yellow",                  "Black",            "#fff7d1",              "Black",                "Black",            "#fff2ab"],
        ["Blue",                    "Black",            "#e2f1ff",              "Black",                "Black",            "#cde9ff"],
        ["Green",                   "Black",            "#e4f9e0",              "Black",                "Black",            "#cbf1c4"],
        ["Red",                     "Black",            "#ffcccc",              "Black",                "Black",            "#ff9999"],
        ["Pink",                    "Black",            "#ffe4f1",              "Black",                "Black",            "#ffcce5"],
        ["Purple",                  "Black",            "#f2e6ff",              "Black",                "Black",            "#e7cfff"],
    ]
All_Fonts = ["Calibri", "Times New Roman", "Consolas", "Comic Sans MS"]
All_FontSizes = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    # Dicts
Settings = {
    #! Default Settings
    #* Essential Settings
    "Main_UseCustomPath": False,
    "Main_FilePath": "N/A",

    #* Main Window Settings
    "Show_File_Extensions": True,
    "Main_Window_On_Top": False,
    "Main_Window_Resizable_X": True,
    "Main_Window_Resizable_Y": True,
    "Main_Window_Show_Version_On_Title_Bar": True,
    "Main_Window_Highlight_Color": "#42c4f0",
    "Main_Window_Even_Row_Color": "#f0f0f0",
    "Main_Window_Odd_Row_Color": "#e6e6e6",
    "Main_Window_Show_Amount_Of_Notes": True, #TODO: Zrobić żeby wyświetlało (albo nie) stopkę

    #* Note Window Settings
    "Note_Window_On_Top": False,
    "Note_Window_Resizable_X": False,
    "Note_Window_Resizable_Y": True,
    "Note_Window_Default_Theme": "Yellow",
    "Note_Window_Font_Face": "Calibri",
    "Note_Window_Font_Size": 11,

    #* File Types
    "FileType_txt": True,
    "FileType_csv": False,
    "FileType_html": False,
    "FileType_css": False,
    "FileType_js": False,
    "FileType_bat": False,
    "FileType_py": False,
    "FileType_cpp": False,

    #* General
    "General_Show_If_Is_In_Use": False,
}
Settings_Copy = {}
Current_Path = OS.getcwd()

#! TODO:
def WIP(Text = ""):
    print(f"--- WIP: '{Text}' ---")

def WIP_2():
    print("--- WIP_2 ---")

#! TODO: Some Tools
def DEBUG_ListOfOpenedNotes():
    print("---\nOpened RN:")
    print(List_Of_Opened_Notes)
    print("\n---")

#! Functions
def Confirm_Closing_Main_Window(Force_Exit = False):
    """
        Asking For Confirmation About Closing Main Window (If There Are Any Notes Left Opened)
    """
    if Force_Exit:
        Check_If_App_Is_Already_Opened("End")
        Main_Window.destroy()
        return
    
    if (Amount_Of_Notes_Opened != 0):
        #* Message To Display
        if (Amount_Of_Notes_Opened == 1):
            Text = f"This action will also close all currently opened notes without saving.\nThere is 1 opened note right now."
        else:
            Text = f"This action will also close all currently opened notes without saving.\nThere are {Amount_Of_Notes_Opened} opened notes right now."

        #* Opening Message Window
        Message_Window_Result = MESSAGEBOX.askquestion("Are You Sure?", Text)

        if (Message_Window_Result == "yes"):
            Check_If_App_Is_Already_Opened("End")
            Main_Window.destroy()
    else:
        Check_If_App_Is_Already_Opened("End")
        Main_Window.destroy()

def Add_New_Note():
    """
        Opening Menu To Create New .txt File
    """
    Filepath = ASKSAVEASFILENAME(defaultextension="txt", filetypes=[("Text Files", "*.txt")])

    if not Filepath:
        return
    with open(Filepath, "w") as New_Note:
        New_Note.write("")

    Check_For_Notes_v2()

def Custom_Message_Box(Which_Menu_To_Open): #TODO: Finish This Function
    """
        Create Custom Message Message Box Window 
    """
    #* Defining Window
    Message_Box = GUI.Toplevel(Main_Window)
    Message_Box.title(f"{Which_Menu_To_Open} - Dzbanpad")

    #* Which Menu To Open
    #? Credits
    if (Which_Menu_To_Open == "Credits"):
        Text = f"Dzpanpad v{DzbanPad_Version}\nMade By Hubsik\n{Date_Creation} - {Date_LastUpdate}"

        Label = GUI.Label(Message_Box, text=Text)
        Label.pack()

    #? Settings
    elif (Which_Menu_To_Open == "Settings"):
        Text = f"Settings - WIP"

        Label_1 = GUI.Label(Message_Box, text=Text)
        Label_1.grid(row=0, column=0, columnspan=2)

        Row = 1
        All_Labels = []
        All_Entries = []

        for Key, Value in Settings.items():
            #* Key
            Temp_Label = Key.replace("_", " ")
            GUI.Label(Message_Box, text=f"{Temp_Label}: ").grid(row=Row, column=0)

            All_Labels.append(Temp_Label)

            #* Value
            Temp_Entry = GUI.Entry(Message_Box)
            Temp_Entry.grid(row=Row, column=1)
            Temp_Entry.insert(GUI.END, Value)

            All_Entries.append(Temp_Entry)

            #* End
            Row += 1
        
        def WIP_Save():
            Temp = len(All_Entries)
            Some_Text = f"# Config File For DzbanPad v{DzbanPad_Version}\n"
            for x in range(Temp):
                Temp_2 = All_Labels[x].replace(" ", "_")

                if (All_Entries[x].get() == "1"):
                    Temp_3 = True
                elif (All_Entries[x].get() == "0"):
                    Temp_3 = False
                else:
                    Temp_3 = All_Entries[x].get()


                Some_Text += f"{Temp_2}= {Temp_3}\n"

            Check_Settings("Save", Some_Text)

        Button_1 = GUI.Button(Message_Box, text="Save", command=WIP_Save)
        Button_1.grid(row=Row+1, column=1)

        Button_2 = GUI.Button(Message_Box, text="Cancel", command=WIP)
        Button_2.grid(row=Row+1, column=0)

    #? Wrong Parameter
    else: # DEL ME
        Label = GUI.Label(Message_Box, text=f"There Is No Menu: '{Which_Menu_To_Open}'")
        Label.pack()

def Check_Settings(Mode = "Load", Text = ""):
    """
        Look For Settings In Config File
        Modes Description:
            Load ---> Load Settings from Config File
            Save ---> TODO:
            GUI  ---> Open GUI Menu To Modify Settings TODO: USELESS????

    """
    #! Load ---> Getting Settings From File
    if (Mode == "Load"):
        if (OS.path.exists("DzbanPad_Config.dzb")):
            #! Opening Settings
            File = open("DzbanPad_Config.dzb", "r")

            for x in File:
                #! Check For Comments
                if (x.startswith("# ")):
                    continue

                #! Remove \n
                if x.endswith("\n"): 
                    x = x[:-1]
                Text_Line = x.split("= ")

                #! Dont Update Custom File Path TODO:
                if x == "Main_FilePath":
                    continue
                
                Settings[Text_Line[0]] = Guess_Var_Type(Text_Line[1])

            #! Add Correct File Types To Array Of Supported File Extension
            if (Settings["FileType_txt"]):
                Supported_File_Formats.append(".txt")
            if (Settings["FileType_csv"]):
                Supported_File_Formats.append(".csv")
            if (Settings["FileType_html"]):
                Supported_File_Formats.append(".html")
            if (Settings["FileType_css"]):
                Supported_File_Formats.append(".css")
            if (Settings["FileType_js"]):
                Supported_File_Formats.append(".js")
            if (Settings["FileType_bat"]):
                Supported_File_Formats.append(".bat")
            if (Settings["FileType_py"]):
                Supported_File_Formats.append(".py")
            if (Settings["FileType_cpp"]):
                Supported_File_Formats.append(".cpp")

        else:
            Check_Settings("Default")

    #! Save ---> Saving Settings To File
    elif (Mode == "Save"):
        File = open("DzbanPad_Config.dzb", "w")
        File.write(Text)
        File.close()

        Check_Settings("Load")
    
    #! GUI ---> WIP TODO: Move Custom Box Settings Here???
    elif (Mode == "GUI"):
        print("WIP - Mode: GUI")
        pass
    
    #! Default ---> Force Default Settings
    elif (Mode == "Default"):
        #! Creating Config File With Default Values
        File = open("DzbanPad_Config.dzb", "w")
        #File.write(f"# Config File For DzbanPad v{DzbanPad_Version}\n# Default Settings\n")
        File.write(f"# Config File For DzbanPad v{DzbanPad_Version}\n")

        for Key, Value in Settings_Copy.items():
            File.write(f"{Key}= {Value}\n")

        File.close()

        #! Opening Those Settings
        Check_Settings("Load")
    
    #! Wrong Mode
    else:
        print(f"ERROR: There Is No '{Mode}' Mode")

def Guess_Var_Type(Input):
    """
        Try To Assign Proper Variable Type To Input
        Checks In Following Order: BOOLEAN --> INT --> STR

        There is no way this could backfire in any way.
    """
    if (Input == "True"):
        return True
    elif (Input == "False"):
        return False
    else:
        # Int
        try:
            Input = int(Input)
            return int(Input)
        except:
            pass
        
        # Str
        try:
            Input = str(Input)
            return str(Input)
        except:
            pass

def Open_Note_In_New_Window(File_Name, File_Path):
    """
        Processes Opening .txt File In New Window And Adding Buttons To Open Those .txt Files
        (TODO: Figure Out Better Way To Add Those Notes)
        
        Zrobić tak żeby tutaj były tylko dodawane "command" a w Check_For_Notes() dodaje przycisku (bez command)

        Open .txt File In New Window
    """
    #! Variables
    global Amount_Of_Notes_Opened
    Amount_Of_Notes_Opened += 1

    Font_Face = Settings["Note_Window_Font_Face"]
    Font_Size = Settings["Note_Window_Font_Size"]

    #! Even More Functions
    def MetaData_Note(File): # TODO:
        if OS.path.exists(File):
            Text_To_Display = f"File Name: {File}\nSize: {OS.path.getsize(File)}\nLast Modified: {OS.path.getmtime(File)}\nCreated: {OS.path.getctime(File)}"
            MESSAGEBOX.showinfo(f"{File} Meta Data", Text_To_Display)
        else:
            MESSAGEBOX.showerror("Error", "File Is Already Removed!\nSomehow file got deleted between opening note and pressing \"Meta Data\" button.")
            Window_Note.destroy()
            #Check_For_Notes()
            Check_For_Notes_v2()
    def Delete_Note(File):
        Message_Window_Result = MESSAGEBOX.askquestion("Are You Sure", f"Do You Want To Delete File {File}")

        if Message_Window_Result == "yes":
            if OS.path.exists(File):
                OS.remove(File)
                #Check_For_Notes()
            else:
                MESSAGEBOX.showerror("Error", "File Is Already Removed!\nSomehow file got deleted between opening note and pressing \"Delete Note\" button.")
                #Check_For_Notes()
            global Amount_Of_Notes_Opened
            Amount_Of_Notes_Opened -= 1
            Window_Note.destroy()
            Check_For_Notes_v2()
    def Save_Note(File, Event = ""):
        print(f"File: {File}")

        #* Updating Close Event
        global TextBox_Content

        #* Saving Changes To File
        File_1 = open(File, "w")
        File_1.write(TextBox.get("1.0", GUI.END))
        File_1.close()

        #* Reading Text From File To Update Exit Event
        File_2 = open(File, "r")
        wip2 = File_2.read()
        File_Content = wip2
        File_2.close()

        #* Getting Value Of TextBox
        TextBox_Content = TextBox.get("1.0", GUI.END)
        
        #* Updating Exit Event
        Window_Note.protocol("WM_DELETE_WINDOW", FUNCTOOLS.partial(Ask_To_Save_Before_Exit, File))

        #* Updating Note Window After Saving
        global Original_TXT_Content
        Original_TXT_Content = wip2
        """
        New_Window_Title = File.name + " - Dzbanpad"
        Window_Note.title(New_Window_Title)
        global Was_Note_Edited
        Was_Note_Edited = False
        """
    def Ask_To_Save_Before_Exit(File):
        #FIXME:
        #* Updating Variables To Check If There Were Any Changes
            # Checking File
        WIP_Path = Current_Path + "\\" + File
        #File_2 = open(File, "r")
        File_2 = open(WIP_Path, "r")
        wip2 = File_2.read()
        File_Content = wip2
        File_2.close()
            # Checking TextBox
        Content_Of_TXT_File = File_Content
        Content_Of_Text_Widget = TextBox.get("1.0", GUI.END)

        #* Changing Global Variables - DEL ME (Reduce_Amount_Of_Notes_Opened() does the same thing)
        #global Amount_Of_Notes_Opened
        #Amount_Of_Notes_Opened -= 1

        #* Checking If There Aren't Any Changes To Be Saved
        if (Content_Of_TXT_File == Content_Of_Text_Widget):
            Window_Note.destroy()

        #* If There Are Any Changes To Be Saved
        else:
            Message_Window_Result = MESSAGEBOX.askquestion("Confirm Changes", f"Do You Want To Save Changes To File {File}?")

            if Message_Window_Result == "yes":
                #Save_Note(File, "")
                Save_Note(WIP_Path, "")
                Window_Note.destroy()
            else:
                Window_Note.destroy()

        #* Remove Name Of Opened File From Array
        Reduce_Amount_Of_Notes_Opened(File)
    def Update_Temp_Changes_Variable(Event = ""):
        #* Updating Note Window After Editing
        global Original_TXT_Content
        if (Original_TXT_Content != TextBox.get("1.0", GUI.END)): # Not Edited
            Window_Note.title(f"*{File_Name} - DzbanPad")
        else: # Edited
            Window_Note.title(f"{File_Name} - DzbanPad")

        #* For Cornfirming Closing Note Window
        Window_Note.protocol("WM_DELETE_WINDOW", FUNCTOOLS.partial(Ask_To_Save_Before_Exit, File_Name))
    def Reduce_Amount_Of_Notes_Opened(File_Name_2):
        """
            Used when user click on "X" or closes Note Window in Any Way
        """
        global Amount_Of_Notes_Opened
        Amount_Of_Notes_Opened -= 1
        Window_Note.destroy()
        List_Of_Opened_Notes.remove(File_Name_2)
        Check_For_Notes_v2()
        Update_Notes_Counter()
    def Themes(Selected_Style):
        #* Changing Style
        for x in range(len(All_Styles)):
            if Selected_Style == All_Styles[x][0]:
                #* Variables
                TextBox_Foreground = All_Styles[x][1]
                TextBox_Background = All_Styles[x][2]
                TexBox_Pointer = All_Styles[x][3]
                #UI_Foreground = All_Styles[x][4]
                UI_Background = All_Styles[x][5]

                #* Apply Selected Style
                TextBox.config(fg=TextBox_Foreground, bg=TextBox_Background, insertbackground=TexBox_Pointer)
                Window_Note.config(bg=UI_Background)
                #TODO: Zbędne elementy gui notatki
                #Label.config(fg=UI_Foreground, bg=UI_Background) 
                #Button_1.config(fg=UI_Foreground, bg=UI_Background)
                #Button_2.config(fg=UI_Foreground, bg=UI_Background)
                #Button_3.config(fg=UI_Foreground, bg=UI_Background)
                break
    def Fonts(Selected_Font):
        TextBox.config(font=(Selected_Font, Font_Size))
    def Font_Sizes(Selected_FontSize):
        TextBox.config(font=(Font_Face, Selected_FontSize))

    #! Checking If File Exists (If File Didnt mysteriously dissapear after listing all .txt files) FIXME: delete 4 lines below later
    #WIP_FILE = File_Path+"\\"+File_Name
    WIP_FILE = File_Path
    #print(f"File_Name: {File_Name}")
    #print(f"WIP_FILE: {WIP_FILE}")
    #if (OS.path.isfile(WIP_FILE) == False):
    if (OS.path.isfile(WIP_FILE) == False):
        
        #MESSAGEBOX.showerror("Error", f"File {File_Name} Cannot Be Opened!\nNo Such File.")
        MESSAGEBOX.showerror("Error", f"File '{File_Path}' Cannot Be Opened!\nNo Such File.\nFile '{File_Name}' Cannot Be Opened!\nNo Such File.")
        Check_For_Notes_v2()
        return

    #! Reading File
    #File = open(File_Name, "r")
    File = open(File_Path, "r")
    File_Content = File.read()
    File.close()
    global Original_TXT_Content
    Original_TXT_Content = File_Content

    #! GUI Elements
    Window_Note = GUI.Toplevel(Main_Window)
    Window_Note.title(f"{File_Name} - DzbanPad")
    Window_Note.geometry("580x450+50+50")
    Window_Note.minsize(400, 200)
    #Window_Note.iconbitmap("Images/NoteBook.ico")
    Window_Note.resizable(Settings["Note_Window_Resizable_X"], Settings["Note_Window_Resizable_Y"])
    Window_Note.attributes("-topmost", Settings["Note_Window_On_Top"])

    TextBox = SCROLLEDTEXT.ScrolledText(Window_Note, undo=True)
    TextBox.config(font=(Settings["Note_Window_Font_Face"], Font_Size), borderwidth=0)

    TextBox.grid(row=0, column=0, sticky="NSEW")
    TextBox.insert(GUI.END, File_Content)

    Window_Note.rowconfigure(0, weight=1)
    Window_Note.columnconfigure(0, weight=1)
    
    #! Menu
        #* Setting Up Note Bar
    Note_Menu_Bar = GUI.Menu(Window_Note)
        #* File
    Note_File_Menu = GUI.Menu(Note_Menu_Bar, tearoff=0)
    #Note_File_Menu.add_command(label="Save", command=FUNCTOOLS.partial(Save_Note, File_Name))
    Note_File_Menu.add_command(label="Save", command=FUNCTOOLS.partial(Save_Note, File_Path))
    Note_File_Menu.add_separator()
    #Note_File_Menu.add_command(label="Delete", command=FUNCTOOLS.partial(Delete_Note, File_Name))
    Note_File_Menu.add_command(label="Delete", command=FUNCTOOLS.partial(Delete_Note, File_Path))
    Note_File_Menu.add_separator()
    Note_File_Menu.add_command(label="Open In File Exlorer", command=FUNCTOOLS.partial(SUBPROCESS.Popen, fr'explorer /select,"{File_Path}"'))
    Note_File_Menu.add_command(label="Meta Data", command=FUNCTOOLS.partial(MetaData_Note, File_Name))
    Note_File_Menu.add_command(label="Meta Data", command=FUNCTOOLS.partial(MetaData_Note, File_Path))
    Note_File_Menu.add_separator()
    Note_File_Menu.add_command(label="Exit", command=FUNCTOOLS.partial(Reduce_Amount_Of_Notes_Opened, File_Name))
    #Note_File_Menu.add_command(label="Exit", command=FUNCTOOLS.partial(Reduce_Amount_Of_Notes_Opened, File_Path))
        #* Style
    Note_Style_Menu = GUI.Menu(Note_Menu_Bar, tearoff=0)
            #* Color Themes
    Note_Themes_Style_Menu = GUI.Menu(Note_Style_Menu, tearoff=0)
    for x in range(len(All_Styles)):
        Note_Themes_Style_Menu.add_command(label=All_Styles[x][0], command=FUNCTOOLS.partial(Themes, All_Styles[x][0]))
            #* Fonts
    Note_Fonts_Style_Menu = GUI.Menu(Note_Style_Menu, tearoff=0)
    for x in range(len(All_Fonts)):
        Note_Fonts_Style_Menu.add_command(label=All_Fonts[x], command=FUNCTOOLS.partial(Fonts, All_Fonts[x]))
            #* Font Sizes
    Note_FontSizes_Style_Menu = GUI.Menu(Note_Style_Menu, tearoff=0)
    for x in range(len(All_FontSizes)):
        Note_FontSizes_Style_Menu.add_command(label=All_FontSizes[x], command=FUNCTOOLS.partial(Font_Sizes, All_FontSizes[x]))
        
        #* Adding To Note Bar
    Note_Menu_Bar.add_cascade(label="File", menu=Note_File_Menu)
    Note_Menu_Bar.add_cascade(label="Styles", menu=Note_Style_Menu)
    Note_Style_Menu.add_cascade(label="Themes", menu=Note_Themes_Style_Menu)
    Note_Style_Menu.add_cascade(label="Fonts", menu=Note_Fonts_Style_Menu)
    Note_Style_Menu.add_cascade(label="Font Sizes", menu=Note_FontSizes_Style_Menu)
    Window_Note.config(menu=Note_Menu_Bar)

    #! Adding Events
        #* Closing
    Window_Note.protocol("WM_DELETE_WINDOW", FUNCTOOLS.partial(Reduce_Amount_Of_Notes_Opened, File_Name))
    #Window_Note.protocol("WM_DELETE_WINDOW", FUNCTOOLS.partial(Reduce_Amount_Of_Notes_Opened, File_Path))
        #* Editing
    TextBox.bind("<KeyRelease>", Update_Temp_Changes_Variable)
        #* Ctrl + S
    #Window_Note.bind_all("<Control-Key-s>", FUNCTOOLS.partial(Save_Note, File_Name))
    Window_Note.bind_all("<Control-Key-s>", FUNCTOOLS.partial(Save_Note, File_Path))

    #! Apply Settings
    Themes(Settings["Note_Window_Default_Theme"])

def Check_For_Notes_v2():
    #* Delete Everything From Tree
    for i in Tree.get_children():
        Tree.delete(i)
    
    #* Check For Amount Of Files
    File_Counter = 0
    #for File in OS.listdir():
    for File in OS.listdir(Current_Path): #FIXME:
        if (File[File.rfind("."):] in Supported_File_Formats):
            File_Counter += 1

    #* Add Files To Tree
    if (File_Counter >= 1):
        global Amount_Of_All_Notes

        Label_2.pack_forget()

        #if Settings["Main_UseCustomPath"]: #FIXME:
        #    Path = Settings["Main_FilePath"]
        #else:
        #    Path = OS.getcwd()
        Path = Current_Path

        Counter = 0
        Amount_Of_All_Notes = 0
        #* Loop Through Files In Directory
        #for File in OS.listdir():
        for File in OS.listdir(Current_Path): #FIXME:
            #* Continue If File Extension Is Supported
            if (File[File.rfind("."):] in Supported_File_Formats):
                #* Update Amount Of All Notes
                Amount_Of_All_Notes += 1
                
                #* Getting Extension Of The File
                Extension = File[File.rfind("."):]

                #* Add Row To Tree
                if (Settings["Show_File_Extensions"]):
                    Text_1 = File
                else:
                    Text_1 = File.replace(Extension, "")

                if (File in List_Of_Opened_Notes):
                    Text_2 = "X"
                else:
                    Text_2 = ""

                #* Zebra Stripes v4
                if (Counter % 2 == 0):
                    Tree.insert("", GUI.END, values=(f"{Text_1}", f"{Text_2}", f"{Extension}", f"{Path}\{File}"), tags="Even") #v4
                else:
                    Tree.insert("", GUI.END, values=(f"{Text_1}", f"{Text_2}", f"{Extension}", f"{Path}\{File}"), tags="Odd") #v4
                
                #print(f"___Path: {Path}\n___File: {File}")
                #* Add File Path To Array
                #File_path = f"{Path}\{File}"
                #File_List.append(File_path)

                Counter += 1

    else:
        Label_2.pack()

def Tree_Event(Event):
    #TODO: Add proper comments
    
    for x in Tree.selection():
        wip_1 = Tree.item(x)
        y = wip_1["values"]

        wip_2 = y[3] # File Name
        wip_3 = y[3] # File Path
        wip_2 = wip_2[wip_2.rfind("\\")+1:]

        if (wip_2 in List_Of_Opened_Notes): # Trying To Open One Note In Multiple Windows
            print(f"ERROR: {y[0]} Is Already Opened")
            pass
        else:
            Open_Note_In_New_Window(wip_2, wip_3)
            List_Of_Opened_Notes.append(wip_2)
            Update_Notes_Counter()

    #! Reload All Notes
    Check_For_Notes_v2() # This Will Also Remove Focus From Clicked Item In Tree
    pass

def Tree_Highlight(Event):
    #TODO: Add proper comments
    
    Treeview = Event.widget
    Treeview_Item = Treeview.identify_row(Event.y)
    Treeview.tk.call(Treeview, "tag", "remove", "Highlight")
    Treeview.tk.call(Treeview, "tag", "add", "Highlight", Treeview_Item)

def Update_Notes_Counter():
    Label_5.config(text=f"{Amount_Of_Notes_Opened} / {Amount_Of_All_Notes}")

def Check_If_App_Is_Already_Opened(Mode):
    #! Opening App And Checking For File
    if Mode == "Start":
        if (OS.path.exists("DzbanPad_InUse.dzb")):
            File = open("DzbanPad_InUse.dzb", "r")
            File_Content = File.readline()

            if File_Content == "True":
                #! Showing Message If App Is Already Opened
                if Settings["General_Show_If_Is_In_Use"]:
                    Error_Window = GUI.Tk()
                    Error_Window.title("DzbanPad")
                    Error_Window.geometry("250x75+100+100")
                    Label_E = GUI.Label(Error_Window, text="DzbanPad is already in use.")
                    Label_E.pack()
                    Error_Window.mainloop()

                return True
            else:
                File.close()
                File = open("DzbanPad_InUse.dzb", "w")
                File.write("True")
                File.close()

                return False
        else:
            File = open("DzbanPad_InUse.dzb", "w")
            File.write("True")
            File.close()
            return False
    #! Closing App And Changing File Content
    elif Mode == "End":
        File = open("DzbanPad_InUse.dzb", "w")
        File.write("False")
        File.close()

    return False

#! Main
if __name__ == "__main__":
    #print(f"Path: {Settings['Main_UseCustomPath']}")
    #print(f"Path: {Settings['Main_FilePath']}")
    #print(f"Current_Path: {Current_Path}")

    #* Settings
    Settings_Copy = dict(Settings) # Load Copy Of The Settings In Case There Is Need To Restore Default
    Check_Settings("Load")

    #* Check If Custom Path Is Valid
    if Settings["Main_UseCustomPath"] and OS.path.exists(Settings["Main_FilePath"]):
        #print("1")
        Current_Path = Settings["Main_FilePath"]
    else:
        #print("2")
        #TODO: Add messagebox and stop program here
        pass


    #* Checking If App Is Already Opened
    if Check_If_App_Is_Already_Opened("Start"):
        EXIT()

    #* Start
    Main_Window = GUI.Tk()
    Main_Window.title(f"DzbanPad")
    #Main_Window.geometry("450x280")
    #Main_Window.geometry("426x253")
    Main_Window.geometry("650x500+100+100")
    Main_Window.minsize(350, 300)
    Main_Window.protocol("WM_DELETE_WINDOW", Confirm_Closing_Main_Window)
    #Main_Window.iconbitmap("Images/NoteBook.ico")
    Main_Window.resizable(Settings["Main_Window_Resizable_X"], Settings["Main_Window_Resizable_Y"])
    Main_Window.attributes("-topmost", Settings["Main_Window_On_Top"])

    if (Settings["Main_Window_Show_Version_On_Title_Bar"]):
        Main_Window.title(f"DzbanPad v{DzbanPad_Version}")

    #* Frames
    Frame_Title = GUI.Frame(Main_Window)
    Frame_NoteList = GUI.Frame(Main_Window)
    Frame_Footer = GUI.Frame(Main_Window)

    #* Menu Bar
        #? Setting Up Main Bar
    Menu_Bar = GUI.Menu(Main_Window)
        #? File
    File_Menu = GUI.Menu(Menu_Bar, tearoff=0)
    File_Menu.add_command(label="New", command=Add_New_Note)
    File_Menu.add_command(label="Reload Notes", command=Check_For_Notes_v2)
    File_Menu.add_separator()
    File_Menu.add_command(label="Exit", command=Confirm_Closing_Main_Window)
    File_Menu.add_command(label="Force Exit", command=FUNCTOOLS.partial(Confirm_Closing_Main_Window, True))
    File_Menu.add_separator()
    #File_Menu.add_command(label="WIP|...", command=)
    File_Menu.add_command(label="WIP| List Of Opened Notes", command=DEBUG_ListOfOpenedNotes)
        #? Config
    Config_Menu = GUI.Menu(Menu_Bar, tearoff=0)
    Config_Menu.add_command(label="WIP| Edit Settings", command=FUNCTOOLS.partial(Custom_Message_Box, "Settings"))
    Config_Menu.add_command(label="Reload Settings", command=FUNCTOOLS.partial(Check_Settings, "Load"))
    Config_Menu.add_command(label="Restore Default Settings", command=FUNCTOOLS.partial(Check_Settings, "Default"))
    Config_Menu.add_separator()
    Config_Menu.add_checkbutton(label="WIP| Stay On Top", command=WIP, onvalue=True, offvalue=False)
        #? Help
    Help_Menu = GUI.Menu(Menu_Bar, tearoff=0)
    Help_Menu.add_command(label="WIP| Credits", command=FUNCTOOLS.partial(Custom_Message_Box, "Credits"))
        #? Adding To Main Bar
    Menu_Bar.add_cascade(label="File", menu=File_Menu)
    Menu_Bar.add_cascade(label="Config", menu=Config_Menu)
    Menu_Bar.add_cascade(label="Credits", menu=Help_Menu)

    #* Placing GUI Elements
        #? Frames
    Frame_Title.pack(side="top", fill="both")
    Frame_NoteList.pack(side="top", fill="both", expand=True)
    Frame_Footer.pack(side="top", fill="both")

        #? GUI Elements
    Label_1 = GUI.Label(Frame_Title, text="All Notes:")
    Label_1.pack()

    Label_2 = GUI.Label(Frame_Title, text="No Notes Found!", fg="red")
    Label_2.pack()
    
    Tree_Columns = ("File Name", "In Use", "Ext", "Path")
    Tree = GUI_2.Treeview(Frame_NoteList, columns=Tree_Columns, show="headings", style="W.TLabel") # Height psuje Frame_Footer
    Tree.tag_configure("Highlight", background=Settings["Main_Window_Highlight_Color"])
    Tree.tag_configure("Even", background=Settings["Main_Window_Even_Row_Color"])
    Tree.tag_configure("Odd", background=Settings["Main_Window_Odd_Row_Color"])
    
            #? Columns
    Tree.heading("File Name", text="File Name");    Tree.column("File Name", minwidth=65, width=200)
    Tree.heading("In Use", text="In Use");          Tree.column("In Use", minwidth=43, width=43, stretch=False)
    Tree.heading("Ext", text="Ext");                Tree.column("Ext", minwidth=43, width=43, stretch=False)
    Tree.heading("Path", text="Path");              Tree.column("Path", minwidth=100, width=350)

    Tree.grid(row=0, column=0, sticky="ewns")

    Tree.bind("<<TreeviewSelect>>", Tree_Event)
    Tree.bind("<Motion>", Tree_Highlight)
    #* Functions
    Check_For_Notes_v2()

        #? Scrollbar
    Scrollbar_1 = GUI_2.Scrollbar(Frame_NoteList, orient=GUI.VERTICAL, command=Tree.yview)
    Tree.configure(yscroll=Scrollbar_1.set)
    Scrollbar_1.grid(row=0, column=1, sticky="ns")

    Frame_NoteList.columnconfigure(0, weight=1)
    Frame_NoteList.columnconfigure(1, weight=0)
    Frame_NoteList.rowconfigure(0, weight=1)

    #* Footer
    if Settings["Main_Window_Show_Amount_Of_Notes"]:
        Label_5 = GUI.Label(Frame_Footer,text=f"{Amount_Of_Notes_Opened} / {Amount_Of_All_Notes}")
        Label_5.pack(anchor="e")

    #* Tooltips TODO:
    #TOOLTIPS(Label_5, msg="Opened Notes / All Notes", delay=0.5, follow=True)

    #* End
    Main_Window.config(menu=Menu_Bar)
    Main_Window.mainloop()

# The End
