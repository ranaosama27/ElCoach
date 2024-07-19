# USAGE : python3 start_here.py --activity "punch - side" --video "test.mp4" --lookup "lookup_test.pickle"
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import os
import time
from Feedback import get_feedback
from Feedback_avr import get_feedback_avr
from calculations import get_Score
from calculations_avr import get_Score_Single
import imageio
from tkinter import Tk, Label
from PIL import ImageTk, Image
from pathlib import Path
import functools
from tkinter import ttk
from tkinter.ttk import *
from PIL import ImageTk
from tkinter import *
import cv2
import PIL.Image, PIL.ImageTk
import tkinter as tkinter
import voiceAssistant

def baseMethod(self,mode,activity,resultFrame,mainWindow,avatarFrame,miniVideo):    
    print("miniVideo/"+miniVideo)
    if mode == '1':
        g = get_Score(str(activity))
        mainWindow.withdraw()
        time.sleep(10)
        mainWindow.deiconify()
        final_score, score_list = g.calculate_Score(str('none'), str(activity),miniVideo)  # list of lists
        r = final_score.index(max(final_score))
        print("Total Score : ", final_score[r])

        f = get_feedback()
        text = f.get_text(activity,score_list)
        print(text)

    if mode == '2':
        g = get_Score_Single('pickle_files_avr/'+str(activity)+'.pickle')
        
        final_score, score_list = g.calculate_Score(str('none'), str(activity),miniVideo)
        
        avatarFrame.pack_forget()
        resultFrame.pack(side="right", fill=BOTH, expand=1, padx=1, pady=1)
        print("Total Score : ", final_score)
        print("Score List : ", score_list)
        f = get_feedback_avr()
        resultText = f.get_text(activity,score_list)
        final_score = str(round(final_score,0))

        self.your_score_label = tkinter.Label(resultFrame, text=final_score ,fg="black" , font='Helvetica 40 bold')
        self.your_score_label.grid(pady=20)
        voiceAssistant.voice("your final score is " + final_score + "percent" )
        voiceAssistant.voice(resultText)
        self.feedback_label = tkinter.Label(resultFrame, text=resultText, fg="black", font=("Helvetica", 16))
        self.feedback_label.grid()
        mainWindow.deiconify()
        print("ds")
        


