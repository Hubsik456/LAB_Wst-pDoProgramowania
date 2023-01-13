"""
    Some Clock I Made

    By Hubsik
    04.05.2022
"""

#! Imports
import tkinter as GUI
import datetime as DATETIME
import os as OS
import re as REGULAR_EXPRESSION

#! Variables
Settings = {
        "Foreground": "white",
        "Background": "black",

        "Window_On_Top": True,
        "Resizable": False,

        "No Alarms Message": "No Alarms Set",
    }
Days = ["Niedziela", "Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota"]
Months = ["Grudzień", "Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Październik", "Grudzień"]
Allowed_Colors = [ #Source: https://htmlcolorcodes.com/color-names/
    # Red
    "indianred", "lightcoral", "salmon", "darksalmon", "lightsalmon", "crimson", "red", "firebrick", "darkred",
    # Pink
    "pink", "lightpink", "hotpink", "deeppink", "mediumvioletred", "palevioletred",
    # Orange
    "lightsalmon", "coral", "tomato", "orangered", "darkorange", "orange",
    # Yellow
    "gold", "yellow", "lightyellow", "lemonchiffon", "lightgoldenrodyellow", "papayawhip", "moccasin", "peachpuff", "palegoldenrod", "khaki", "darkkhaki",
    # Purple
    "lavender", "thistle", "plum", "violet", "orchid", "fuchsia", "magenta", "mediumorchid", "mediumpurple", "rebeccapurple", "blueviolet", "darkviolet", "darkorchid", "darkmagenta", "purple", "indigo", "slateblue", "darkslateblue", "mediumslateblue",
    # Green
    "greenyellow", "chartreuse", "lawngreen", "lime", "limegreen", "palegreen", "lightgreen", "mediumspringgreen", "springgreen", "mediumseagreen", "seagreen", "forestgreen", "green", "darkgreen", "yellowgreen", "olivedrab", "olive", "darkolivegreen", "mediumaquamarine", "darkseagreen", "lightseagreen", "darkcyan", "teal",
    # Blue
    "aqua", "cyan", "lightcyan", "paleturquoise", "aquamarine", "turquoise", "mediumturquoise", "darkturquoise", "cadetblue", "steelblue", "lightsteelblue", "powderblue", "lightblue", "skyblue", "lightskyblue", "deepskyblue", "dodgerblue", "cornflowerblue", "royalblue", "blue", "mediumblue", "darkblue", "navy", "midnightblue",
    # Brown
    "cornsilk", "blanchedalmond", "bisque", "navajowhite", "wheat", "burlywood", "tan", "rosybrown", "sandybrown", "goldenrod", "darkgoldenrod", "peru", "chocolate", "saddlebrown", "sienna", "brown", "maroon",
    # White
    "white", "snow", "honeydew", "mintcream", "azure", "aliceblue", "ghostwhite", "whitesmoke", "seashell", "beige", "oldlace", "floralwhite", "ivory", "antiquewhite", "linen", "lavenderblush", "mistyrose",
    # Gray
    "gainsboro", "lightgray", "silver", "darkgray", "gray", "dimgray", "lightslategray", "slategray", "darkslategray", "black"]


#! Functions
def Load_Settings():
    """
        Loading Data From Text File (if Exists) And Updating Settings
    """
    #! If File Exists
    if (OS.path.exists("Clock_Config.txt")):
        File = open("Clock_Config.txt", "r")
    
        #! Loading File To Array
        temp = File.read().splitlines()
        if (len(temp) <= 3):
            #! Default Settings
            #Settings["Foreground"] = Settings["Default_Foreground"]
            #Settings["Background"] = Settings["Default_Background"]
            return

        #! Validate Loaded Data
        Regex = "^#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$"
        temp2 = REGULAR_EXPRESSION.compile(Regex)

        if (REGULAR_EXPRESSION.search(temp2, temp[0])): #! Foreground
            Settings["Foreground"] = temp[0]
        elif (temp[0].lower() in Allowed_Colors):
            Settings["Foreground"] = temp[0]
        else:
            Settings["Foreground"] = Settings["Default_Foreground"]

        if (REGULAR_EXPRESSION.search(temp2, temp[1])): #! Background
            Settings["Background"] = temp[1]
        elif (temp[1].lower() in Allowed_Colors):
            Settings["Background"] = temp[1]
        else:
            Settings["Background"] = Settings["Default_Background"]

        #! Window On Top
        if (temp[2] == "True"):
            Settings["Window_On_Top"] = True
        else:
            Settings["Window_On_Top"] = False

        #! Resizable Window
        if (temp[3] == "True"):
            Settings["Resizable"] = True
        else:
            Settings["Resizable"] = False

        #! End
        File.close()

def Open_Settings_Menu():
    """
        Processing Opening New Window With Settings
    """
    #! New Window Settings
    Window_Settings = GUI.Toplevel(Window)
    Window_Settings.title("Clock Settings")
    Window_Settings.resizable(Settings["Resizable"], Settings["Resizable"])
    # Window_Settings.geometry("200x250")

    #! Functions
    def Save_Settings():
        """
            Save Settings To Text File
            Requires Restarting APP To Take Effect
        """
        #! Create File
        File = open("Clock_Config.txt", "w")

        #! Save Data To File
        File.write(Entry_FG.get() + "\n")
        File.write(Entry_BG.get() + "\n")

        File.write(str(Checkbox_OnTop_Value.get()) + "\n")
        File.write(str(Checkbox_Resizable_Value.get()) + "\n")

        #! End
        Label.config(text="Settings Will Change On Restarting App")
        File.close()

    #! Defining GUI Elements
    Label = GUI.Label(Window_Settings, text="Settings:")
    Label.grid(row=0, column=0, columnspan=2)

    Label_FG = GUI.Label(Window_Settings, text="Foreground: ")
    Label_BG = GUI.Label(Window_Settings, text="Background: ")
    Label_OnTop = GUI.Label(Window_Settings, text="Window On Top: ")
    Label_Resizable = GUI.Label(Window_Settings, text="Resizable Window: ")

    Entry_FG = GUI.Entry(Window_Settings)
    Entry_BG = GUI.Entry(Window_Settings)

    Label = GUI.Label(Window_Settings, text="Enter Colors As HTML Color Names OR HEX Value")

    Button_Save = GUI.Button(Window_Settings, text="Save", command=Save_Settings)

    Checkbox_OnTop_Value = GUI.BooleanVar()
    Checkbox_Resizable_Value = GUI.BooleanVar()
    Checkbox_OnTop = GUI.Checkbutton(Window_Settings, onvalue=True, offvalue=False, variable=Checkbox_OnTop_Value)
    Checkbox_Resizable = GUI.Checkbutton(Window_Settings, onvalue=True, offvalue=False, variable=Checkbox_Resizable_Value)

    #! Default Values For Entry/Checkbox/Whatever
    Entry_FG.insert(0, Settings["Foreground"])
    Entry_BG.insert(0, Settings["Background"])
    if (Settings["Window_On_Top"]):
        Checkbox_OnTop.select()
    if (Settings["Resizable"]):
        Checkbox_Resizable.select()


    #! Placing GUI Elements
    Label.grid(row=0, column=0, columnspan=2)

    Label_FG.grid(row=1, column=0)
    Entry_FG.grid(row=1, column=1)

    Label_BG.grid(row=2, column=0)
    Entry_BG.grid(row=2, column=1)

    Label_OnTop.grid(row=3, column=0)
    Checkbox_OnTop.grid(row=3, column=1)

    Label_Resizable.grid(row=4, column=0)
    Checkbox_Resizable.grid(row=4, column=1)

    Button_Save.grid(row=5, column=0, columnspan=2)

    Label.grid(row=6, column=0, columnspan=2)

def Update_Clock():
    """"
        Get time/date and edit label
    """
    #! Update Time / Weekday / Month / Year
    Clock = DATETIME.datetime.now()
    Clock_Combined = Clock.strftime("%H:%M:%S   ")  + Days[int(Clock.strftime("%w"))] + "\n" + Clock.strftime("%d ") + Months[int(Clock.strftime("%m"))] + Clock.strftime(" %Y")

    Label_1.config(text=Clock_Combined)

    #! End
    Window.after(100, Update_Clock)

#! Main
Load_Settings()

Window = GUI.Tk()
Window.title("Clock")
#Window.geometry("200x35")
#Window.geometry("200x60")
Window.attributes('-topmost', Settings["Window_On_Top"])
Window.resizable(Settings["Resizable"], Settings["Resizable"])
Window.configure(bg=Settings["Background"])

Alarms = []

Label_1 = GUI.Label(text="", fg=Settings["Foreground"], bg=Settings["Background"])
Label_1.grid(row=0, column=0)

Button_1 = GUI.Button(Window, text="   ...   ", command=Open_Settings_Menu, fg=Settings["Foreground"], bg=Settings["Background"], border=0)
Button_1.grid(row=0, column=1, sticky='nesw')

Label_2 = GUI.Label(text="", fg=Settings["Foreground"], bg=Settings["Background"])

Update_Clock()
Window.mainloop()