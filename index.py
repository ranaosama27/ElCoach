from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import os
from tkinter import *
from PIL import Image, ImageTk
import tkinter
import PIL.Image, PIL.ImageTk
import cv2
import os
from login import *
from register import *
from baseMethod import *
import voiceAssistant

class Main_Screen:

    def __init__(self, main):
        self.main = main

        self.main_screen()

    def main_screen(self):
        self.mainFrame = Frame(self.main)
        self.registerFrame = Frame(self.main)
        self.loginFrame = Frame(self.main)
        self.mainMenuFrame = Frame(self.main)
        self.modeFrame = Frame(self.mainMenuFrame, height=300)
        self.exerciseFrame = Frame(self.mainMenuFrame)
        self.sideFrame = Frame(self.mainMenuFrame)
        self.avatarFrame = Frame(self.main)
        self.resultFrame = Frame(self.main)
        self.circle_outline = tkinter.PhotoImage(file="score.png")
        self.outline_button = tkinter.Button(self.resultFrame, image=self.circle_outline, borderwidth=0)
        self.outline_button.grid(row=0, column=0, padx=250, pady=50)
        
        self.mainMenu()
        self.mainFrame.pack( fill=BOTH, expand=1)

        self.rightframe = tkinter.Frame(self.mainFrame)
        #self.rightframe['bg'] = "black"
        self.rightframe.pack(side="right", fill=BOTH, expand=1 , pady=250)

        self.leftframe = tkinter.Frame(self.mainFrame)
        #self.leftframe['bg'] = "white"
        self.leftframe.pack(side="left", fill=BOTH, expand=1 , padx=20 , pady=100)

        self.logo = tk.PhotoImage(file='images/elcoach-1.png')
        self.logo_shape = tk.Button(self.leftframe, image=self.logo, borderwidth=0)
        self.logo_shape.grid(row=1, column=1)

        self.login_photo = tk.PhotoImage(file='images/login_sign.png')
        self.login_button = Button(self.rightframe,image=self.login_photo ,
                      borderwidth=0,command= lambda: [self.loginFrame.pack(side="right", fill=BOTH, expand=1, padx=1, pady=1),self.mainFrame.pack_forget(),login(self.loginFrame,self.mainMenuFrame)])
        self.login_button.grid(row=0, column=1)


        self.register_photo = tk.PhotoImage(file='images/register_sign.png')
        self.register_button = Button(self.rightframe,
                      borderwidth=0,image=self.register_photo,command=lambda: [ self.registerFrame.pack(side="right", fill=BOTH, expand=1, padx=75, pady=290),self.mainFrame.pack_forget(),register(self.registerFrame,self.mainFrame)])
        self.register_button.grid(row=1, column=1)



        main.grid_columnconfigure(1, minsize=100)        
        self.activity = StringVar()
        self.activity= ''
        self.mode = StringVar()
        self.mode = '2'
        print("act"+self.activity)
        print("mode"+self.mode)
        
    def hidePack(self, frameShow, frameHide, frameSide):
        frameHide.pack_forget()
        frameShow.pack(side=frameSide, fill=tk.BOTH, expand=1)
    
    def startEx(self):
        print(self.mode +" /////////// "+self.activity)
        main.withdraw()
        print("x")
        text = "take care to perform well"
        voiceAssistant.voice(text)
        baseMethod(self,self.mode,self.activity,self.resultFrame,main,self.avatarFrame,self.activity)   
        
    def avatar(self, videoName,fraaam):
        self.ok = False
        print(videoName)
        print("done")
        videoName += ".mp4"
        print(videoName)
        self.video = cv2.VideoCapture(videoName)
        self.width = self.video.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)
        #Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(fraaam, width=self.width, height=self.height)
        self.canvas.pack()
        
        self.playPhoto = tkinter.PhotoImage(file='images/play.png')
        self.stopPhoto = tkinter.PhotoImage(file='images/stop.png')
        self.startExs = tkinter.Button(fraaam, image=self.playPhoto ,command=lambda: [self.startEx()])
        # self.openavatar = tkinter.Button(fraaam, image=self.stopPhoto ,command =lambda: self.openNewWindow())
        self.startExs.pack()
        # self.openavatar.pack()
        self.delay = 20
        self.update()

    def update(self):
        
        ret, frame = self.video.read()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
        self.avatarFrame.after(self.delay, self.update)
         
    def mainMenu(self):
        # self.modeFrame.pack(side="top", fill=BOTH, expand= False , pady=40 )
        self.exerciseFrame.pack(side="bottom", fill=BOTH, expand= 1,padx=20 , pady= 10)
        self.hidden = 0

        #exercises buttons
        # 1
        self.arm_lifting = tkinter.PhotoImage(file='images/exercies/1.png')
        arm_lifting_button = Button(self.exerciseFrame,image=self.arm_lifting ,command=lambda: [self.hideExercise("arm lifting",'avatarFrame')], borderwidth=0)
        arm_lifting_button.grid(row=0,column=0, padx=50 , pady=35)
        arm_lifting_label = tkinter.Label(self.exerciseFrame, text='Arm lifting',font=("Comic Sans MS", "11"))
        arm_lifting_label.place( x=75, y=290 )
        # 2
        self.shoulder_abduction = tkinter.PhotoImage(file='images/exercies/2.png')
        shoulder_abduction_button = Button(self.exerciseFrame, image=self.shoulder_abduction, command=lambda: [self.hideExercise("shoulder abduction",'sideFrame')],  borderwidth=0)
        shoulder_abduction_button.grid(row=0, column=1, padx=35)
        shoulder_abduction_label = tkinter.Label(self.exerciseFrame, text='shoulder abduction', font=("Comic Sans MS", "11"))
        shoulder_abduction_label.place(x=240, y=290)
        #3
        self.leg_extention = tkinter.PhotoImage(file='images/exercies/3.png')
        leg_extention_button = Button(self.exerciseFrame, image=self.leg_extention,  command=lambda: [self.hideExercise("leg_lifting_extension",'sideFrame')], borderwidth=0)
        leg_extention_button.grid(row=0, column=2, padx=35)
        leg_extention_label = tkinter.Label(self.exerciseFrame, text='leg extention', font=("Comic Sans MS", "11"))
        leg_extention_label.place(x=470, y=290)


        # 4
        self.triceps = tkinter.PhotoImage(file='images/exercies/4.png')
        triceps_button = Button(self.exerciseFrame, image=self.triceps,command=lambda: [self.hideExercise("static_tricep_extension",'sideFrame')], borderwidth=0)
        triceps_button.grid(row=0, column=3, padx=35)
        triceps_label = tkinter.Label(  self.exerciseFrame, text='triceps', font=("Comic Sans MS", "11"))
        triceps_label.place(x=700, y=290)
        # 5
        self.swing_arm = tkinter.PhotoImage(file='images/exercies/5.png')
        swing_arm_button = Button(self.exerciseFrame, image=self.swing_arm,command=lambda: [self.hideExercise("swing_arm",'sideFrame')], borderwidth=0)
        swing_arm_button.grid(row=1, column=0, padx=35, pady=35)
        swing_arm_label = tkinter.Label(self.exerciseFrame, text='swing arm', font=("Comic Sans MS", "11"))
        swing_arm_label.place(x=75, y=530)
        # 6
        self.circle_arm = tkinter.PhotoImage(file='images/exercies/6.png')
        circle_arm_button = Button(self.exerciseFrame, image=self.circle_arm, command=lambda: [self.hideExercise("circle_arm",'sideFrame')], borderwidth=0)
        circle_arm_button.grid(row=1, column=1, padx=35)
        circle_arm_label = tkinter.Label(self.exerciseFrame, text='circle arm', font=("Comic Sans MS", "11"))
        circle_arm_label.place(x=260, y=530)
        # 7
        self.seated_leg_lifting = tkinter.PhotoImage(file='images/exercies/7.png')
        seated_leg_lifting_button = Button(self.exerciseFrame, image=self.seated_leg_lifting,  command=lambda: [self.hideExercise("leg_lifting_extension",'sideFrame')], borderwidth=0)
        seated_leg_lifting_button.grid(row=1, column=2, padx=35)
        seated_leg_lifting_label = tkinter.Label(self.exerciseFrame, text='leg lifting', font=("Comic Sans MS", "11"))
        seated_leg_lifting_label.place(x=490, y=530)
        # 8
        self.seated_hamstring = tkinter.PhotoImage(file='images/exercies/8.png')
        seated_hamstring_button = Button(self.exerciseFrame, image=self.seated_hamstring, command=lambda: [self.hideExercise("seated_hamstring",'sideFrame')], borderwidth=0)
        seated_hamstring_button.grid(row=1, column=3, padx=40)
        seated_hamstring_label = tkinter.Label(self.exerciseFrame, text='seated hamstring', font=("Comic Sans MS", "11"))
        seated_hamstring_label.place(x=700, y=530)

        #side
        self.RightPhoto = tkinter.PhotoImage(file='images/exercies/left.png')
        self.leftPhoto = tkinter.PhotoImage(file='images/exercies/right.png')

        left = tkinter.Button(self.sideFrame, image=self.leftPhoto, borderwidth=0,command=lambda: [self.hideExercise("_left",'avatarFrame')])
        right = tkinter.Button(self.sideFrame, image=self.RightPhoto, borderwidth=0, command=lambda: [self.hideExercise("_right",'avatarFrame')])
        left.grid(row=0, column=0, sticky=W,  padx=220)
        right.grid(row=0, column=0, sticky=W,  padx=490)

        labelLeft = tkinter.Label(self.sideFrame ,text='left',font=("Comic Sans MS", "11"))
        labelRight = tkinter.Label(self.sideFrame ,text='right',font=("Comic Sans MS", "11"))
        labelLeft.grid(row=1, column=0, sticky=W, padx=350)
        labelRight.grid(row=1, column=0, sticky=W, padx=490 )

    def hideMode(self, name, hide):
        hide.pack_forget()
        self.mode=name
        print(self.mode)
        self.mode = name

    def hideExercise(self, name, show):
        self.activity += name
        
        if show == 'avatarFrame':
            text = "you will perfome" + self.activity + "exercise" 
            voiceAssistant.voice(text)
            self.mainMenuFrame.pack_forget()
            self.exerciseFrame.pack_forget()
            self.modeFrame.pack_forget()
            self.avatarFrame.pack(side="right", fill=BOTH, expand=1,padx=1)
            self.avatar("avatar/"+self.activity,self.avatarFrame) 
        else:
            self.sideFrame.pack(side="top", fill=BOTH, expand= False , pady=40 )
            self.exerciseFrame.pack_forget()
            text = "Please choose exercise side"
            voiceAssistant.voice(text)

main = tk.Tk()
main.geometry("900x900+500+100")
main.title("El-Coach")

#main.iconbitmap("images/elcoach.png")
app = Main_Screen(main)
main.mainloop()