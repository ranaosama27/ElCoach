from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import os
import voiceAssistant

def register(register_screen,mainFrame):
    register_screen.grid(row=0,column=0)

    global username
    global password
    global age
    global gender
    global height
    global weight
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    age = int()
    gender = StringVar()
    choices = {'male','female'}
    gender.set('male')
    downframe= Frame(register_screen)
    downframe.pack(side="bottom", fill=BOTH)
    WIDTH, HEIGTH = 200, 200
    canvas = tk.Canvas(register_screen, width=WIDTH, height=HEIGTH)
    canvas.pack(side="top", fill=BOTH, expand=1, padx=370)
    img = ImageTk.PhotoImage(Image.open('images/profile.png').resize((WIDTH, HEIGTH), Image.ANTIALIAS))
    canvas.background = img  # Keep a reference in case this code is put in a function.
    bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)
    gender_menu = OptionMenu(downframe, gender, *choices)
    Label(downframe, text="Please enter details below").grid(row=0,column=0)
    # Label(register_screen, text="").grid(row=0,column=1)
    username_lable = Label(downframe, text="Username * ", height="4", width="30")
    username_lable.grid(row=0,column=0)
    username_entry = Entry(downframe, textvariable=username)
    username_entry.grid(row=0,column=1)
    password_lable = Label(downframe, text="Password * " , height="4", width="30")
    password_lable.grid(row=0,column=2)
    password_entry = Entry(downframe, textvariable=password, show='*')
    password_entry.grid(row=0,column=3)
    age_lable = Label(downframe, text="age", height="4", width="30")
    age_lable.grid(row=1,column=0)
    age_entry = Entry(downframe, textvariable=age)
    age_entry.grid(row=1,column=1)
    gender_label = Label(downframe, text="gender").grid(row = 1, column = 2)
    gender_menu.grid(row = 1, column =3)
    height_lable = Label(downframe, text="height", height="4", width="30")
    height_lable.grid(row=2,column=0)
    height_lable = Entry(downframe)
    height_lable.grid(row=2,column=1)
    weight_lable = Label(downframe, text="weight", height="4", width="30")
    weight_lable.grid(row=2,column=2 )
    weight_lable = Entry(downframe)
    weight_lable.grid(row=2,column=3)

    register_button = tk.Button(downframe, text="register",width=10, height=2, command = lambda:register_user(downframe))
    register_button.grid(row=3, column=1)
    register_button = Button(downframe, text="Cancel", width=10, height=2, command = lambda: [mainFrame.grid(row=0,column=0),register_screen.grid_forget()])
    register_button.grid(row=3 , column=2)


# # Implementing event on register button

def register_user(downframe):

    username_info = username.get()
    
    list_of_files = os.listdir()
    if username_info in list_of_files:
        Label(downframe, text="user exist").grid(row=5, column=0) #update
        voiceAssistant.voice("user exist")
        return 0
    password_info = password.get()
    # age_info = age.get()
    # height_info = height.get()
    # weight_info = weight.get()
    
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info + "\n")
    # file.write(age_info + "\n")
    # file.write(height_info + "\n")
    # file.write(weight_info + "\n")
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    #Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).grid(row=0,column=0)

