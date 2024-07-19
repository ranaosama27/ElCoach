import tkinter
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import os
class Main_Screen:
    def __init__(self, main):
        self.main = main
        self.feedback()

    def feedback(self):
       resultFrame =tkinter.Frame()
       resultFrame.pack(fill=BOTH)

       self.circle_outline = tkinter.PhotoImage(file='images/score.jpeg')
       outline_button = tkinter.Button(resultFrame, image=self.circle_outline, borderwidth=0)
       outline_button.grid(row=0, column=0, padx=250, pady=50)

       your_score_label = tkinter.Label(resultFrame, text='90%' ,fg="black" , font='Helvetica 40 bold')
       your_score_label.grid(pady=20)

       feedback_label = tkinter.Label(resultFrame, text='good job , well done you have been strong we are so proud of you', fg="black", font=("Helvetica", 16))
       feedback_label.grid()



main = tkinter.Tk()
main.geometry("900x800")
app = Main_Screen(main)
main.mainloop()