# -*- coding: utf-8 -*-

from tkinter import *
import socket
import threading
import time
import datetime


# Fenêtre
window = Tk()
window.title("NetWay Management")
window.geometry(("1080x600"))
window.minsize(1080,600)
window.iconbitmap("./Pictures/netway_icon.ico")
window.config(background="#deedca")

# Titre
label_title = Label(window, text="Netway Management", font=("Calibri", 40), bg="#deedca", fg="white")
label_title.pack(expand=YES, side=TOP)

# Images
width = 300
height = 300
img = PhotoImage(file="./Pictures/netway_img.png")
canvas = Canvas(window, width=width, height=height, bg="#deedca", bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=img)
canvas.pack(expand=YES, side=BOTTOM)


# Afficher la fenêtre
window.mainloop()