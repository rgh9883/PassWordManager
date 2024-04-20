
import tkinter as tk
import customtkinter as ctk
import pyperclip

#Functions
def addName():
    nameScreen = ctk.CTkInputDialog(text="Type in Where Password will be used", title="passName")
    name = nameScreen.get_input()
    if name is not None and name != "":
        addPassword(name)

def addPassword(namePass):
    addScreen = ctk.CTkInputDialog(text="Type in the Password", title="password")
    password = addScreen.get_input()
    with open('passwords.txt', 'a') as f:
        f.write(namePass + "-" + password + "\n")
    options = getOptions()
    viewMenu.configure(values=options)

def getOptions():
    options = []
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip().split("-")
            options.append(data[0])
    return options

def viewPass():
    name = viewMenu.get()
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip().split("-")
            if data[0] == name:
                textDisplay.configure(text=data[1])
                pyperclip.copy(data[1])
                pyperclip.paste()
                
                



#MainApp
ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("500x500")
app.title("passwordManagerMain")

title = ctk.CTkLabel(app, text="PassWord Manager", font=('Bold', 20))
title.pack(padx=10,pady=10)

addButton = ctk.CTkButton(app, text="Add Password", command=addName, text_color='black')
addButton.pack()

viewButton = ctk.CTkButton(app, text="View Password", command=viewPass, text_color='black')
viewButton.pack()

viewOptions = getOptions()
viewMenu = ctk.CTkOptionMenu(app, values=viewOptions, dropdown_fg_color='#a2c4fa', text_color='black', dropdown_text_color='black')
viewMenu.pack()

textDisplay = ctk.CTkLabel(app, text="")
textDisplay.pack()


app.mainloop()