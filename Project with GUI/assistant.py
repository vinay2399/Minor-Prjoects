import speech_recognition as sr
from tkinter import *

def litsen():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print('litsening....')
        label1 = Label(root,text="Litsening..").grid(row=1,column=0)

        #root.mainloop()
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source)
        root.update_idletasks()
        #root.mainloop()
        print('fetching audio....')
        label2 = Label(root,text='Fetching audio..').grid(row=2,column=0)
        root.update_idletasks()
        #root.mainloop()
        transcript = r.recognize_google(audio)
        
        print(transcript)
        label3=Label(root,text=transcript).grid(row=3,column=0)
        root.mainloop()

root=Tk()
root.grid()
root.geometry("700x500+0+0")
root.title("voice assistant")
speak=Button(text="speak",activebackground='green',activeforeground='black',relief='raised',bg='white',fg='black',command=litsen).grid(row=0,column=0)

