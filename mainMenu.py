from tkinter import *
from PIL import Image, ImageTk
import tkinter
import PIL.Image, PIL.ImageTk
import cv2
import os
# import index as ins


def mainMenu(self,modeFrame,exerciseFrame,sideFrame,avatarFrame,mainMenueFrame):
    modeFrame.pack(side="top", fill=BOTH, expand= False , pady=40 )
    exerciseFrame.pack(side="bottom", fill=BOTH, expand= 1,padx=10)
    
    self.hidden = 0
    self.activity = StringVar()
    self.activity= ''
    self.mode = StringVar()
    self.mode = ''

    self.performancePhoto = tkinter.PhotoImage(file='images/performance.png')
    self.accuracyPhoto = tkinter.PhotoImage(file='images/accuracy.png')

    performance = tkinter.Button(modeFrame, image=self.performancePhoto, borderwidth=0,command=lambda: [hideMode(self,"2",modeFrame)])
    accracy = tkinter.Button(modeFrame, image=self.accuracyPhoto, borderwidth=0, command=lambda: [hideMode(self,"1",modeFrame)])
    performance.grid(row=0, column=0, sticky=W,  padx=290)
    accracy.grid(row=0, column=0, sticky=W,  padx=490)

    labelPerformance = tkinter.Label(modeFrame ,text=' high perfomance mode',font=("Comic Sans MS", "11"))
    labelaccuracy = tkinter.Label(modeFrame ,text=' high accuracy mode',font=("Comic Sans MS", "11"))
    labelPerformance.grid(row=1, column=0, sticky=W, padx=260)
    labelaccuracy.grid(row=1, column=0, sticky=W, padx=490 )



    #exercises buttons
    self.arm_lifting = tkinter.PhotoImage(file='images/arm_lifting.png')
    arm_lifting_button = Button(exerciseFrame,image=self.arm_lifting ,command=lambda: [hideExercise(self,"arm lifting",exerciseFrame,avatarFrame)], borderwidth=0)
    arm_lifting_button.grid(row=0,column=0, padx=50 , pady=35)
    arm_lifting_label = tkinter.Label(exerciseFrame, text='Arm lifting',font=("Comic Sans MS", "11"))
    arm_lifting_label.place( x=75, y=170 )

    self.shoulder_abduction = tkinter.PhotoImage(file='images/shoulder_abduction.png')
    shoulder_abduction_button = Button(exerciseFrame, image=self.shoulder_abduction, command=lambda: [hideExercise(self,"shoulder abduction",exerciseFrame,sideFrame)],  borderwidth=0)
    shoulder_abduction_button.grid(row=0, column=1, padx=35)
    shoulder_abduction_label = tkinter.Label(exerciseFrame, text='shoulder abduction', font=("Comic Sans MS", "11"))
    shoulder_abduction_label.place(x=240, y=170)

    self.leg_extention = tkinter.PhotoImage(file='images/leg_extention.png')
    leg_extention_button = Button(exerciseFrame, image=self.leg_extention,  command=lambda: [hideExercise(self,"leg_lifting_extension",exerciseFrame,sideFrame)], borderwidth=0)
    leg_extention_button.grid(row=0, column=2, padx=35)
    leg_extention_label = tkinter.Label(exerciseFrame, text='leg extention', font=("Comic Sans MS", "11"))
    leg_extention_label.place(x=470, y=170)

    self.triceps = tkinter.PhotoImage(file='images/triceps.png')
    triceps_button = Button(exerciseFrame, image=self.triceps,command=lambda: [hideExercise(self,"static_tricep_extension",exerciseFrame,sideFrame)], borderwidth=0)
    triceps_button.grid(row=0, column=3, padx=35)
    triceps_label = tkinter.Label(exerciseFrame, text='triceps', font=("Comic Sans MS", "11"))
    triceps_label.place(x=700, y=170)

    self.swing_arm = tkinter.PhotoImage(file='images/swing_arm.png')
    swing_arm_button = Button(exerciseFrame, image=self.swing_arm,command=lambda: [hideExercise(self,"swing_arm",exerciseFrame,sideFrame)], borderwidth=0)
    swing_arm_button.grid(row=1, column=0, padx=35, pady=35)
    swing_arm_label = tkinter.Label(exerciseFrame, text='swing arm', font=("Comic Sans MS", "11"))
    swing_arm_label.place(x=75, y=400)

    self.circle_arm = tkinter.PhotoImage(file='images/circle_arm.png')
    circle_arm_button = Button(exerciseFrame, image=self.circle_arm, command=lambda: [hideExercise(self,"circle_arm",exerciseFrame,sideFrame)], borderwidth=0)
    circle_arm_button.grid(row=1, column=1, padx=35)
    circle_arm_label = tkinter.Label(exerciseFrame, text='circle arm', font=("Comic Sans MS", "11"))
    circle_arm_label.place(x=260, y=400)

    self.seated_leg_lifting = tkinter.PhotoImage(file='images/leg_lifting.png')
    seated_leg_lifting_button = Button(exerciseFrame, image=self.seated_leg_lifting,  command=lambda: [hideExercise(self,"leg_lifting_extension",exerciseFrame,sideFrame)], borderwidth=0)
    seated_leg_lifting_button.grid(row=1, column=2, padx=35)
    seated_leg_lifting_label = tkinter.Label(exerciseFrame, text='leg lifting', font=("Comic Sans MS", "11"))
    seated_leg_lifting_label.place(x=490, y=400)

    self.seated_hamstring = tkinter.PhotoImage(file='images/seated_harmstring.png')
    seated_hamstring_button = Button(exerciseFrame, image=self.seated_hamstring, command=lambda: [hideExercise(self,"seated_hamstring",exerciseFrame,sideFrame)], borderwidth=0)
    seated_hamstring_button.grid(row=1, column=3, padx=40)
    seated_hamstring_label = tkinter.Label(exerciseFrame, text='seated hamstring', font=("Comic Sans MS", "11"))
    seated_hamstring_label.place(x=700, y=400)

    #side
    self.leftPhoto = tkinter.PhotoImage(file='images/left.png')
    self.RightPhoto = tkinter.PhotoImage(file='images/right.png')

    left = tkinter.Button(sideFrame, image=self.leftPhoto, borderwidth=0,command=lambda: [hideExercise(self,"_left",mainMenueFrame,avatarFrame)])
    right = tkinter.Button(sideFrame, image=self.RightPhoto, borderwidth=0, command=lambda: [hideExercise(self,"_right",sideFrame,avatarFrame)])
    left.grid(row=0, column=0, sticky=W,  padx=290)
    right.grid(row=0, column=0, sticky=W,  padx=490)

    labelLeft = tkinter.Label(sideFrame ,text='left',font=("Comic Sans MS", "11"))
    labelRight = tkinter.Label(sideFrame ,text='right',font=("Comic Sans MS", "11"))
    labelLeft.grid(row=1, column=0, sticky=W, padx=260)
    labelRight.grid(row=1, column=0, sticky=W, padx=490 )

    print(self.activity)

def activityReturn(self):
    return self.activity

def modeReturn(self):
    return self.mode

def hideMode(self,name,hide):
    hide.pack_forget()
    self.mode=name
    print(self.mode)
    modeReturn(self)

def hideExercise(self,name,hide,show):
    hide.pack_forget()
    if show == 'avatarFrame':
        show.pack(side="right", fill=BOTH, expand=1)
        avatar(self,'avatar/arm-liftinge.mp4')
    else:
       show.pack(side="top", fill=BOTH, expand= False , pady=40 )
    
    self.activity += name
    print(self.activity)
    activityReturn(self)
