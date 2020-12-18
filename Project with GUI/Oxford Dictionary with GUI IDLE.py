import requests
import json
import xlwt
import xlrd
from xlutils.copy import copy
from tkinter import *

def getWord():
     word=wordname.get()
     url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/'  + language + '/'  + word.capitalize()
     patt0 = xlwt.easyxf('font: name Times New Roman,color-index blue ,bold on',num_format_str='#,##0.00')
     patt1 = xlwt.easyxf('font: name Comic Sans MS,color-index black ,bold off')
     rb = xlrd.open_workbook('oxforddata.xls')
      r = rb.sheet_by_index(0) 
     i = r.nrows
     wb = copy(rb) 
     flag = False

     for j in range(i):
          if(r.cell(j,0).value==word.capitalize()):
        
             flag=True
             break
        
     if(flag==True):
          #print("*Word already in the Dictionary File*\nHere's the definition:\n")
          #print(r.cell(j,1).value)
          Output = Label(root,text=r.cell(j,1).value).grid(row=2,column=0,sticky='w',padx=10,pady=10,rowspan=2,columnspan=100)
          #delete label content
          root.mainloop()
    
     else:
          req=requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})
          a=req.json()
          meaning=a['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
          ws=wb.get_sheet(0) 
          ws.write(i,0,word.capitalize(),patt1)
          ws.write(i,1,meaning.title(),patt0) 
          wb.save('oxforddata.xls')
          print("*New Entry entered in the Dictionary File*\n")
          Output = Label(root,text=meaning).grid(row=2,column=0,sticky='w',padx=100,pady=10,columnspan=100,rowspan=10)
          root.mainloop()

root=Tk()
root.grid()
root.geometry("700x500+0+0")
root.title("Oxford Dictionary")
root.configure(background='white')
app_id = '4283f066'
app_key = 'f82c2d77ea9607344c960d7d99bf36b8'
language = 'en'
Label1 = Label(root,text="Enter a Word: ").grid(row=0,column=0,sticky="E",padx=20,pady=20)
wordname = Entry(root,width=20,bd=5)
wordname.grid(row=0,column=1)
submit = Button(text="Get Definition",activebackground='white',activeforeground='black',relief='raised',bg='white',fg='black',command=getWord).grid(row=1,column=1)
