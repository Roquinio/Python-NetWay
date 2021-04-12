# -*- coding: utf-8 -*-

from tkinter import *
import socket
import threading
import time
import datetime
import hashlib

def getWindow():

    # Fenêtre
    window = Tk()
    window.title("NetWay Management")
    window.geometry(("1080x600"))
    window.minsize(1080,600)
    window.iconbitmap("./Pictures/netway_icon.ico")
    window.config(background="#cce6aa")

    # frameLog
    frameLog = Frame(window, bg="#cce6aa")

    # Titre
    label_title = Label(frameLog, text="Netway Management", font=("Calibri", 40), bg="#cce6aa", fg="white")
    label_title.pack(expand=YES, side=TOP)

    # Images
    width = 300
    height = 300
    img = PhotoImage(file="./Pictures/netway_img.png")
    canvas = Canvas(frameLog, width=width, height=height, bg="#cce6aa", bd=0, highlightthickness=0)
    canvas.create_image(width/2, height/2, image=img)
    canvas.pack(expand=YES, side=BOTTOM)

    # Champs login
    login_entry = Entry(frameLog, font=("Calibri", 25), bg="white", fg="#9bb07f")
    login_entry.insert(0, "Login")
    login_entry.pack()
    
    # Champs Mot de passe
    passwd_entry = Entry(frameLog, font=("Calibri", 25), bg="white", fg="#9bb07f")
    passwd_entry.insert(0, "Mot de passe")
    passwd_entry.config(show="*")
    passwd_entry.pack()

    def logSession(login_entry, passwd_entry):
    
        login_value = login_entry.get()
        passwd_value = passwd_entry.get()

    # Bouton Connexion
    log_button = Button(frameLog, text="Se connecter", font=("Calibri", 25), bg="white", fg="#9bb07f", command = logSession(login_entry, passwd_entry))
    log_button.pack(pady=25, fill=X)


    # Ajout de la frameLog
    frameLog.pack(expand=YES)

    # Afficher la fenêtre
    window.mainloop()

  
    

getWindow()




    