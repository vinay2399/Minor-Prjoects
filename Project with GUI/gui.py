from tkinter import *
def bulb_on():
    print('Bulb turned on')
def bulb_off():
    print('Bulb turned off')
def fan_on():
    print('Fan turned on')
def fan_off():
    print('Fan turned off')
root=Tk()
root.grid()
v=IntVar()
w=IntVar()
root.geometry('600x480') #set window size
root.title('First GUI')
head=Label(text='Bulb',fg='#ff0000',bg='white').grid(row=0,column=0)
button=Radiobutton(text='on',fg='black',bg='white',variable=v,value=1,command=bulb_on)
button.grid(row=0,column=1)
button=Radiobutton(text='off',fg='black',bg='white',variable=v,value=2,command=bulb_off)
button.grid(row=1,column=1)
head=Label(text='Fan',fg='#ff0000',bg='white').grid(row=3,column=0)
button=Radiobutton(text='on',fg='black',bg='white',variable=w,value=1,command=bulb_on)
button.grid(row=3,column=1)
button=Radiobutton(text='off',fg='black',bg='white',variable=w,value=2,command=bulb_on)
button.grid(row=4,column=1)
temp=Button(text='submit',bd=3,activebackground='yellow',activeforeground='green',relief='raised',fg='red',bg='black').grid(row=8,column=0)
