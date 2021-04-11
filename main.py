# -*- coding: utf-8 -*-

from tkinter import *
import socket
import threading
import time
import datetime

def getWindow():

    # Fenêtre
    window = Tk()
    window.title("NetWay Management")
    window.geometry(("1080x600"))
    window.minsize(1080,600)
    window.iconbitmap("./Pictures/netway_icon.ico")
    window.config(background="#cce6aa")

    # Frame

    frame= Frame(window, bg="#cce6aa")

    # Titre
    label_title = Label(frame, text="Netway Management", font=("Calibri", 40), bg="#cce6aa", fg="white")
    label_title.pack(expand=YES, side=TOP)

    # Images
    width = 300
    height = 300
    img = PhotoImage(file="./Pictures/netway_img.png")
    canvas = Canvas(frame, width=width, height=height, bg="#cce6aa", bd=0, highlightthickness=0)
    canvas.create_image(width/2, height/2, image=img)
    canvas.pack(expand=YES, side=BOTTOM)

    # Bouton Connexion
    
    log_button = Button(frame, text="Se connecter", font=("Calibri", 25), bg="white", fg="#9bb07f")
    log_button.pack(pady=25, fill=X)



    # Ajout de la frame
    frame.pack(expand=YES)

    # Afficher la fenêtre
    window.mainloop()

getWindow()


def logSession():
    