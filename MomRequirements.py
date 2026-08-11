from customtkinter import *

app = CTk()
app.geometry("500x400")

set_appearance_mode("light")
set_default_color_theme("Greengage.json")

checkbox = CTkCheckBox(master=app, text="Option", checkbox_height=20,checkbox_width=20)
checkbox.place(relx = 0.5, rely = 0.2, anchor="center")

combobox = CTkComboBox(master=app, values=["options 1","options 2"])
combobox.place(relx = 0.5, rely = 0.3, anchor="center")

frame = CTkScrollableFrame(master=app,orientation="vertical")
frame.pack(expand = True)
frame.place(relx = 0.5, rely = 0.4, anchor="n")

label = CTkLabel(master=frame,text = "some text", font=("Arial",20))
label.place(relx = 0.5, rely = 0.4, anchor="center")


def click_handler():
    print(checkbox.get())

btn = CTkButton(master=frame, text="Save", command=click_handler,corner_radius=32)
# anchor = must be n, ne, e, se, s, sw, w, nw, or center
btn.place(relx=0.5,rely=0.5,anchor="center")



app.mainloop()