
import tkinter as tk
import customtkinter as ctk

def addName():
    nameScreen = ctk.CTkInputDialog(text="Type in Where Password will be used", title="passName")
    name = nameScreen.get_input()
    if name is not None and name != "":
        addPassword(name)

def addPassword(namePass):
    addScreen = ctk.CTkInputDialog(text="Type in the Password", title="password")
    print(namePass, addScreen.get_input())

#MainApp Settings
ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("500x500")
app.title("passwordManagerMain")

title = ctk.CTkLabel(app, text="PassWord Manager", font=('Bold', 20))
title.pack(padx=10,pady=10)

addButton = ctk.CTkButton(app, text="Add Password", command=addName)
addButton.pack()


app.mainloop()