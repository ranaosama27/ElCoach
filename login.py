import tkinter
from tkinter import *

from PIL import Image, ImageTk
import tkinter as tk
import os
import voiceAssistant

def login(login_screen,mainMenuFrame):

    global username_verify
    global password_verify
    global username_login_entry
    global password_login_entry
    username_verify = StringVar()
    password_verify = StringVar()
    canvas = Canvas(login_screen)
    canvas.pack(side=RIGHT, fill=BOTH, expand=True)
    rightframe = tkinter.Frame(canvas)
    leftframe = tk.Frame(canvas)

    leftframe.pack(side="left", fill=tkinter.BOTH, expand=1, padx=10, pady=80)
    #rightframe['bg'] = "black"
    rightframe.pack(side="right", fill=tkinter.BOTH, expand=1, padx=30 , pady=200)

    logo = tk.PhotoImage(file='images/elcoach-1.png')
    logo_shape = tk.Button(leftframe, image=logo, borderwidth=0)
    logo_shape.grid(row=0, column=0)
    # fitness = tk.PhotoImage(file='images/fitness.png')
    # fitness_shape = tk.Button(leftframe, image=fitness, borderwidth=0)
    # fitness_shape.grid(row=1, column=0)



    Label(rightframe, text="").grid(row=1, column=0)

    face = tk.PhotoImage(file='images/person-male.png')
    face_shape = tk.Button(rightframe, image=face, borderwidth=0 )
    face_shape.grid(row=1, column=1)

    Label(rightframe, text="Username * " , fg='#01365e').grid(row=2, column=0)
    username_login_entry = Entry(rightframe, textvariable=username_verify)
    username_login_entry.grid(row=2, column=1)

    Label(rightframe, text="").grid(row=3, column=0)

    Label(rightframe, text="Password * " , fg='#01365e').grid(row=4, column=0)
    
    
    password_login_entry = Entry(rightframe, textvariable=password_verify, show='*')
    password_login_entry.grid(row=4, column=1)

    Label(rightframe, text="").grid(row=6, column=0)

    Label(rightframe, text="").grid(row=5, column=1)

    login = tk.PhotoImage(file='images/login_icon.png')
    login_button= Button(rightframe, image= login, borderwidth=0,command=lambda: login_verify(mainMenuFrame, login_screen, rightframe)).grid(row=7, column=0)  #update
    
    login_button.grid(row=0, column=0, padx=100)

     # Implementing event on login button


def login_verify(next, hide, rightframe):#update
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            next.pack(side="right", fill=BOTH, expand=1)
            hide.pack_forget()
            print('done')
            voiceAssistant.voice("you have been logined successful")
        else:
            Label(rightframe, text="Incorrect Password").grid(row=5, column=0) #update
            voiceAssistant.voice("Incorrect Password")

    else:
        Label(rightframe, text="User not found").grid(row=5, column=0)#update
        voiceAssistant.voice("User not found")

        