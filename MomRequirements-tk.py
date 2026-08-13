from customtkinter import *

def reverse_by_spaces(text: str) -> str:
    return " ".join(text.split(" ")[::-1])

class mandatoryFrame(CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

        self.title = CTkLabel(self,text=reverse_by_spaces("קורסי חובה"))
        self.title.grid(row=0,column=0,padx=10, pady=(10, 0),columnspan=2)

        self.boxNdLabel(reverse_by_spaces("מושגי יסוד בחקר סכסוכים"),1)

        self.boxNdLabel(reverse_by_spaces("מבנה חברתי של ישראל"),2)

        self.boxNdLabel(reverse_by_spaces("סוגיות בקונפליקטים קבוצתיים וארגוניים"),3)

        self.boxNdLabel(reverse_by_spaces("משא ומתן ככלי לניהול וישוב סכסוכים"),4)

    def boxNdLabel(self,text,row):
        self.lbl = CTkLabel(self,text=text)
        self.lbl.grid(row=row, column=0, padx=(10,0), pady=(10, 0),sticky="e")

        self.ckbox = CTkCheckBox(self,text="",width=10)
        self.ckbox.grid(row=row, column=1, padx=(10,0), pady=(10, 0),sticky="e")

class seminarFrame(CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)


        self.title = CTkLabel(self,text=reverse_by_spaces("סמינר"))
        self.title.grid(row=0,column=0,padx=10, pady=(10, 0),sticky="new",columnspan=2)

        radio_var = IntVar(value=1)

        self.radioNdLabel(reverse_by_spaces("לא ביצע"),1,radio_var)

        self.radioNdLabel(reverse_by_spaces("התמודדות מתבגרים במצבי קונפליקט"),2,radio_var)

        self.radioNdLabel(reverse_by_spaces("קונפליקטים במרחב המשפחתי"),3,radio_var)


    def radioNdLabel(self,text,row,radio_var):
        self.lbl = CTkLabel(self,text=text)
        self.lbl.grid(row=row, column=0, padx=(10,0), pady=(10, 0),sticky="e")
        self.seminarOption = CTkRadioButton(self,text="",variable= radio_var, value=row,width=10)
        self.seminarOption.grid(row=row,column=1,padx=10, pady=(10, 0),sticky="e")

class electivesFrame(CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        self.rowCounter = 3
        self.COLUMNS = ["Electives", "Credits"]

        self.grid_columnconfigure((0,1),weight=1)
        

        self.title = CTkLabel(self,text=reverse_by_spaces("קורסי בחירה"))
        self.title.grid(row=0,column=0,padx=10, pady=(10, 0),columnspan=2)

        self.addRowButton = CTkButton(self,text=reverse_by_spaces("הוסיפי שורה"),command=self.addRow)
        self.addRowButton.grid(row=1,column=0,padx=10, pady=(5, 0),columnspan=2)

        self.credHeader = CTkLabel(self,text=reverse_by_spaces("מספר נקז"))
        self.credHeader.grid(row=2,column=0,padx=(10,0), pady=(5,0),sticky="nsew")

        self.nameHeader = CTkLabel(self,text=reverse_by_spaces("שם הקורס"))
        self.nameHeader.grid(row=2,column=1,padx=(0,10), pady=(5, 0),sticky="nsew")

        self.addRow()


    def addRow(self):
        self.name_var = StringVar()
        self.name_var.trace_add("write", self.on_var_change)

        self.entryName = CTkEntry(self, placeholder_text="",textvariable=self.name_var)
        self.entryName.grid(row=self.rowCounter, column=1,padx=(10,0), pady=(5, 0))
        self.entryCredits = CTkEntry(self, placeholder_text="")
        self.entryCredits.grid(row=self.rowCounter, column=0,padx=(0,10), pady=(5, 0))
        self.rowCounter += 1

    def on_var_change(self, *args):
        current = self.name_var.get()
        # e.g. force uppercase as they type
        self.name_var.set(reverse_by_spaces(current))



class App(CTk):
    def __init__(self):
        super().__init__()

        self.title("Mom's App")
        self.geometry("600x500")
        set_appearance_mode("light")
        set_default_color_theme("blue")

        self.grid_columnconfigure((0,1),weight=1)
        self.grid_rowconfigure(0,weight=5)
        self.grid_rowconfigure(1,weight=5)
        self.grid_rowconfigure(2,weight=1)

        self.seminarFrame = seminarFrame(self)
        self.seminarFrame.grid(row=0,column = 0,padx=10, pady=(10, 0),sticky="nswe")

        self.mandatoryFrame = mandatoryFrame(self)
        self.mandatoryFrame.grid(row=0,column=1,padx=10, pady=(10, 0),sticky="nswe")

        self.electivesFrame = electivesFrame(self)
        self.electivesFrame.grid(row=1,column=0,padx=10,pady=(10,0),sticky="nsew")

        self.button = CTkButton(self,text = reverse_by_spaces("שמירת קובץ"),command=self.save_button)
        self.button.grid(row=2,column=0,padx=10,pady=10,sticky="nsew",columnspan=2)

    def save_button(self):
        print("saved")


app = App()
app.mainloop()

