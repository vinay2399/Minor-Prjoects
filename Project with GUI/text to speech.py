import pyttsx3 as tts
from tkinter import *

def speech():
    word=wordname.get()
    s=tts.init()
    voices = s.getProperty('voices')
    s.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    s.setProperty('rate', 200)     # setting up new voice rate
    s.say(word)
    s.runAndWait()
 
    rate = s.getProperty('rate')   # getting details of current speaking rate
    print (rate)                        #printing current voice rate
   

root=Tk()
root.grid()
root.geometry("700x500+0+0")
root.title('text to speech')
label=Label(root,text='Enter text: ').grid(row=0,column=0,sticky='E',padx=20,pady=20)
wordname=Entry(root,width=30,bd=2)
wordname.grid(row=0,column=1)
submit = Button(text='litsen',activebackground='white',activeforeground='black',relief='raised',bg='white',fg='black',command=speech).grid(row=1,column=1)
