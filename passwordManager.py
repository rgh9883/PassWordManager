
from PIL import Image
import customtkinter as ctk
import pyperclip
from cryptography.fernet import Fernet
import base64

#GenerateKey
'''def createKey():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
createKey()'''

#Functions
def loadKey():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key
key = loadKey()
fer = Fernet(key)

def addName():
    nameScreen = ctk.CTkInputDialog(text="Type in Where Password will be used", title="passName")
    name = nameScreen.get_input()
    if name is not None and name != "":
        addPassword(name)

def addPassword(namePass):
    addScreen = ctk.CTkInputDialog(text="Type in the Password", title="password")
    password = addScreen.get_input()
    with open('passwords.txt', 'a') as f:
        passw = fer.encrypt(password.encode())
        f.write(namePass + "-" + base64.b64encode(passw).decode() + "\n")
    options = getOptions()
    viewMenu.configure(values=options)
    textDisplay.configure(text="Password Added")

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
                passw = base64.b64decode(data[1].encode())
                print(passw)
                password = fer.decrypt(passw).decode()
                textDisplay.configure(text="Password Copied: " + password)
                pyperclip.copy(password)
                pyperclip.paste()
                
                



#MainApp
ctk.set_appearance_mode("dark")
key = loadKey()
fer = Fernet(key)

app = ctk.CTk()
app.geometry("500x250")
app.resizable(False, False)
app.title("passwordManagerMain")

#Adds Peter Griffin Background Picture
'''bg = Image.open('peter.png')
background = ctk.CTkImage(bg, size=(500,250))
bgLabel = ctk.CTkLabel(app, text="", image=background)
bgLabel.place(x=0,y=0)'''

#Header
title = ctk.CTkLabel(app, text="Password Manager", font=('default', 40))
title.pack(padx=10)

#PasswordNameSelector
viewOptions = getOptions()
viewMenu = ctk.CTkOptionMenu(app, values=viewOptions, dropdown_fg_color='#a2c4fa', text_color='black', dropdown_text_color='black')
viewMenu.set("Pick Password Name")
viewMenu.pack(pady=10)

#CreateFrame
f = ctk.CTkFrame(app)
f.pack()

addButton = ctk.CTkButton(f, text="Add Password", command=addName, text_color='black')
addButton.pack(side='left', padx=5)

viewButton = ctk.CTkButton(f, text="View Password", command=viewPass, text_color='black')
viewButton.pack(side='left', padx=5)

textDisplay = ctk.CTkLabel(app, text="", font=('arial', 20))
textDisplay.pack(pady=10)

app.mainloop()