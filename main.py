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
window.iconbitmap("./Pictures/netway.ico")
window.config(background="#deedca")


label_title = Label(window, text="Netway Management", font=("Courrier", 40), bg="#deedca", fg="white")
label_title.pack(expand=YES)



window.mainloop()