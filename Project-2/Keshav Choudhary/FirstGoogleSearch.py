#Importing all the libraries required 
import requests
from bs4 import BeautifulSoup
import webbrowser
import tkinter as tk
from tkinter import ttk
from tkinter import *
import os

#defining the class
  
def myclass():
    show(ttext.get())    

#creatiing the root window using tkinter
root = tk.Tk()
root.grid_columnconfigure((0,1), weight=1)
root.configure(background="#10D5E2")
root.title("WEB SCRAPPING SEARCH WEBSITE")                #adding the title to the gui box
root.configure(borderwidth="10",relief="sunken",background="#3B3F3F",cursor="arrow")
root.resizable(True,True)
label_head=tk.Label(root,text="URL  OPENER",font=("Comic Sans Ms",35),relief="flat",fg="black",background="#3B3F3F")   #header file for the gui box
label_head.grid(row=0,column=2,pady=20)

#adding image to the gui

Label1 = tk.Label(root)
_img1 = PhotoImage(file="r.png")
Label1.configure(image=_img1,background="#3B3F3F")
Label1.configure(text='''Label''')
Label1.grid(row=2,column=2,padx=250,pady=10)


#defing the entry box to collect data from user
ttext= tk.Entry(root,width=40,bg="white",fg="black",font=("Comic Sans Ms",15),relief="sunken")
ttext.grid(row=7,column=2,pady=10)

#defining the label to let user know what to enter

label1=tk.Label(root,text="Enter the keyword below ",bg="#3B3F3F",fg="white",font=("Comic Sans Ms",15),relief="flat",)
label1.grid(row=6,column=2,pady=10)

#definig a clickable button to start the scrapping process

button_find=tk.Button(root,text="click to get the url of first website",bg="black",fg="white",width=30,pady=5,font=("Comic Sans Ms",18),command=myclass,relief="raised",padx=50)
button_find.grid(row=9,column=2)

label3=label1=tk.Label(root,text="click on the below box to open the first link",bg="#3B3F3F",fg="white",font=("Comic Sans Ms",15),relief="flat",)
label3.grid(row=10,column=2,pady=20)

url=""

#defining the function to process the code

def show(search_text):
    text = search_text
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' }
    res = requests.get("https://www.google.com/search?q="+' '.join(text))
    soup=BeautifulSoup(res.text,"html.parser")
    link_elements=soup.select('.kCrYT a')
    link_length=min(1,len(link_elements))
    for i in range(link_length):
        url=link_elements[i].get('href')

        def myo():
            webbrowser.open('https://google.com/' + url)
            exit()
#setting up the url link button
        button_find2 = tk.Button(root, text=url, bg="cyan", fg="white", pady=5,font=("Comic Sans Ms", 18), command=myo, relief="flat")
        button_find2.grid(row=11, column=2,pady=5)

root.mainloop()